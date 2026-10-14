import sys
import types
import unittest
from unittest.mock import MagicMock, patch
from datetime import timedelta

from flask import Flask
from flask_jwt_extended import JWTManager, create_access_token

# Aislar modelos
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

from controllers.auth_controller import auth_bp


class TestAuthTokensHU1(unittest.TestCase):
    """Pruebas de token expirado e inválido (HU1)"""

    @classmethod
    def setUpClass(cls):
        app = Flask(__name__)
        app.config.update(
            TESTING=True,
            JWT_SECRET_KEY="clave-pruebas-checku",
            JWT_ACCESS_TOKEN_EXPIRES=timedelta(hours=1),
        )
        JWTManager(app)
        app.register_blueprint(auth_bp, url_prefix="/api/auth")
        cls.app = app

    def setUp(self):
        self.client = self.app.test_client()

    def test_verify_sin_token_retorna_401(self):
        """Token faltante → 401"""
        respuesta = self.client.get("/api/auth/verify")
        self.assertEqual(respuesta.status_code, 401)

    def test_verify_con_token_invalido_retorna_401(self):
        """Token inválido o corrupto → 401"""
        respuesta = self.client.get(
            "/api/auth/verify",
            headers={"Authorization": "Bearer token_invalido_123"}
        )
        self.assertEqual(respuesta.status_code, 401)

    def test_me_sin_token_retorna_401(self):
        """Endpoint /me sin token → 401"""
        respuesta = self.client.get("/api/auth/me")
        self.assertEqual(respuesta.status_code, 401)

    def test_me_con_token_invalido_retorna_401(self):
        """Endpoint /me con token inválido → 401"""
        respuesta = self.client.get(
            "/api/auth/me",
            headers={"Authorization": "Bearer este_token_no_es_valido"}
        )
        self.assertEqual(respuesta.status_code, 401)

    def test_verify_con_token_valido_retorna_200(self):
        """Token válido debe devolver 200 y valid: true"""
        with self.app.app_context():
            token = create_access_token(
                identity="DOCENTE01",
                additional_claims={"role": "profesor", "id": 1, "nombre": "Profesor Test"}
            )

        respuesta = self.client.get(
            "/api/auth/verify",
            headers={"Authorization": f"Bearer {token}"}
        )
        self.assertEqual(respuesta.status_code, 200)
        data = respuesta.get_json()
        self.assertTrue(data.get("valid"))
        self.assertEqual(data.get("role"), "profesor")


if __name__ == "__main__":
    unittest.main()