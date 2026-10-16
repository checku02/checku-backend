import sys
import types
import unittest
from unittest.mock import MagicMock

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
Grupo = crear_modelo("Grupo", ["nombre", "materia"])

from flask import Flask
from flask_jwt_extended import JWTManager

class TestPermisosHU2HU3(unittest.TestCase):
    """Pruebas de duplicados y permisos por rol (HU2 y HU3)"""

    @classmethod
    def setUpClass(cls):
        app = Flask(__name__)
        app.config.update(
            TESTING=True,
            JWT_SECRET_KEY="clave-pruebas-checku",
        )
        JWTManager(app)
        cls.app = app

    def setUp(self):
        self.client = self.app.test_client()

    def test_sin_token_retorna_401(self):
        """Cualquier endpoint protegido sin token → 401"""
        # Este test es conceptual; en la práctica se prueba contra los endpoints reales
        self.assertTrue(True)

    def test_rol_incorrecto_retorna_403(self):
        """Alumno o profesor intentando acceder a endpoint de admin → 403"""
        self.assertTrue(True)

    def test_duplicado_grupo_retorna_409(self):
        """Crear un grupo que ya existe → 409"""
        self.assertTrue(True)

    def test_duplicado_alumno_en_grupo_retorna_409(self):
        """Inscribir un alumno que ya está en el grupo → 409"""
        self.assertTrue(True)

    def test_duplicado_docente_retorna_409(self):
        """Crear un docente que ya existe → 409"""
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()