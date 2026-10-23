import pytest


def test_asistencia_rechaza_codigo_qr_invalido(client):
    """Un código QR inválido no debe registrar asistencia."""
    response = client.post(
        "/api/qr/validar",
        json={"codigo": "QR_INVALIDO"}
    )

    assert response.status_code in (400, 401, 403, 404, 422)


def test_asistencia_rechaza_peticion_sin_codigo(client):
    """La petición sin código QR debe rechazarse."""
    response = client.post(
        "/api/qr/validar",
        json={}
    )

    assert response.status_code in (400, 401, 403, 404, 422)
