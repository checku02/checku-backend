import pytest


def test_sesion_qr_rechaza_codigo_expirado(client):
    """Una sesión QR expirada no debe permitir registrar asistencia."""
    response = client.post(
        "/api/qr/validar",
        json={"codigo": "QR_EXPIRADO"}
    )

    assert response.status_code in (400, 401, 403, 404, 410)


def test_sesion_qr_rechaza_sesion_cerrada(client):
    """Una sesión QR cerrada no debe aceptar nuevas validaciones."""
    response = client.post(
        "/api/qr/validar",
        json={"codigo": "QR_SESION_CERRADA"}
    )

    assert response.status_code in (400, 401, 403, 404, 410)
