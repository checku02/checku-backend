import sys
import types
import unittest
from unittest.mock import MagicMock

# Aislar el controlador de los modelos que faltan en el repositorio.
models = types.ModuleType("models")
models.__path__ = []
sys.modules["models"] = models

class Campo:
    def __eq__(self, other):
        return self

    def __or__(self, other):
        return self

def crear_modelo(nombre, campos):
    modulo = types.ModuleType(f"models.{nombre.lower()}")
    clase = type(nombre, (), {})
    for campo in campos:
        setattr(clase, campo, Campo())
    clase.query = MagicMock()
    modulo.__dict__[nombre] = clase
    sys.modules[modulo.__name__] = modulo
    setattr(models, nombre, clase)
    return clase

Profesor = crear_modelo("Profesor", ["matricula", "email"])
Alumno = crear_modelo("Alumno", ["matricula", "email"])
Administrador = crear_modelo("Administrador", ["usuario", "email"])

from flask import Flask
from flask_jwt_extended import JWTManager
from controllers.auth_controller import auth_bp

class TestAuthHU1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app = Flask(__name__)
        app.config.update(
            TESTING=True,
            JWT_SECRET_KEY="clave-pruebas-checku",
        )
        JWTManager(app)
        app.register_blueprint(auth_bp, url_prefix="/api/auth")
        cls.app = app

    def setUp(self):
        self.client = self.app.test_client()
        for modelo in (Administrador, Profesor, Alumno):
            modelo.query.reset_mock()
            modelo.query.filter.return_value.first.return_value = None

    def test_login_sin_identificador_retorna_400(self):
        respuesta = self.client.post(
            "/api/auth/login",
            json={"password": "ClavePrueba123"},
        )
        self.assertEqual(respuesta.status_code, 400)
        self.assertFalse(respuesta.get_json()["success"])

    def test_login_con_usuario_inexistente_retorna_401(self):
        respuesta = self.client.post(
            "/api/auth/login",
            json={
                "identificador": "usuario_inexistente",
                "password": "ClaveIncorrecta123",
            },
        )
        self.assertEqual(respuesta.status_code, 401)
        self.assertFalse(respuesta.get_json()["success"])

    def test_login_con_password_vacio_retorna_400_si_hay_profesor(self):
        profesor = MagicMock()
        Profesor.query.filter.return_value.first.return_value = profesor
        Administrador.query.filter.return_value.first.return_value = None
        respuesta = self.client.post(
            "/api/auth/login",
            json={"identificador": "DOCENTE01", "password": ""},
        )
        self.assertEqual(respuesta.status_code, 400)

    def test_alumno_no_puede_iniciar_sesion_en_web(self):
        alumno = MagicMock()
        alumno.id = 1
        alumno.nombre = "Alumno de prueba"
        alumno.matricula = "ALUMNO01"
        alumno.carrera = "Prueba"
        Administrador.query.filter.return_value.first.return_value = None
        Profesor.query.filter.return_value.first.return_value = None
        Alumno.query.filter.return_value.first.return_value = alumno

        respuesta = self.client.post(
            "/api/auth/login",
            json={
                "identificador": "ALUMNO01",
                "password": "ClavePrueba123",
                "origen": "web",
            },
        )
        self.assertEqual(respuesta.status_code, 403)
        self.assertEqual(
            respuesta.get_json()["code"],
            "ALUMNO_WEB_RESTRICTED",
        )

if __name__ == "__main__":
    unittest.main()

    def test_login_correcto_de_profesor_retorna_200_y_su_rol(self):
        profesor = MagicMock()
        profesor.id = 7
        profesor.nombre = "Profesor de prueba"
        profesor.matricula = "DOCENTE01"
        profesor.email = "docente@example.com"
        profesor.check_password.return_value = True
        profesor.to_dict.return_value = {
            "id": 7,
            "nombre": "Profesor de prueba",
            "matricula": "DOCENTE01",
            "email": "docente@example.com",
        }

        Administrador.query.filter.return_value.first.return_value = None
        Profesor.query.filter.return_value.first.return_value = profesor

        respuesta = self.client.post(
            "/api/auth/login",
            json={
                "identificador": "DOCENTE01",
                "password": "ClaveValida123",
                "origen": "web",
            },
        )

        datos = respuesta.get_json()
        self.assertEqual(respuesta.status_code, 200)
        self.assertTrue(datos["success"])
        self.assertEqual(datos["role"], "profesor")
        self.assertEqual(datos["dashboard"], "/dashboard")
        self.assertIn("access_token", datos)
