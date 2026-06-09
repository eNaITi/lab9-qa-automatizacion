# tests/test_pagos.py
#
# RESPUESTAS A LAS PREGUNTAS DE LA TAREA:
#
# f) ¿Por qué es incorrecto usar la PasarelaPago real en los tests automáticos?
#    Porque realizaría cobros reales cada vez que se ejecute la suite, generando transacciones falsas, costos económicos y dependencia de una red/servicio externo.
#    Los tests deben ser rápidos, aislados y repetibles sin efectos secundarios.
#
# g) ¿Qué diferencia existe entre un Stub y un Mock?
#    Un Stub solo devuelve respuestas predefinidas (simula el comportamiento).
#    Un Mock además verifica que fue llamado con los argumentos correctos.
#    En test_pago_exitoso_retorna_txn_id usamos el MagicMock como STUB, porque solo nos importa la respuesta, no verificamos cómo fue llamado.

import pytest
from unittest.mock import MagicMock
from app.pagos import ProcesadorPago

@pytest.fixture
def procesador_con_mock():
    """Fixture que provee ProcesadorPago con pasarela mockeada."""
    mock_pasarela = MagicMock()
    mock_pasarela.cobrar.return_value = {"estado": "ok", "txn_id": "TXN-TEST-001"}
    return ProcesadorPago(pasarela=mock_pasarela), mock_pasarela

def test_pago_exitoso_retorna_txn_id(procesador_con_mock):
    # Arrange
    procesador, mock_pasarela = procesador_con_mock
    # Act
    resultado = procesador.procesar(monto=150.0, cliente="ana@mail.com")
    # Assert
    assert resultado["txn_id"] == "TXN-TEST-001"
    assert resultado["estado"] == "ok"

def test_pago_llama_pasarela_con_monto_correcto(procesador_con_mock):
    # Arrange
    procesador, mock_pasarela = procesador_con_mock
    # Act
    procesador.procesar(monto=250.0, cliente="ana@mail.com")
    # Assert — aquí el MagicMock actúa como MOCK (verifica la llamada)
    mock_pasarela.cobrar.assert_called_once_with(monto=250.0)

def test_pago_sin_duplicados(procesador_con_mock):
    """Verifica que no se realizan cobros duplicados."""
    procesador, mock_pasarela = procesador_con_mock
    # Act
    procesador.procesar(monto=100.0, cliente="juan@mail.com")
    # Assert
    assert mock_pasarela.cobrar.call_count == 1

def test_pago_falla_cuando_pasarela_lanza_excepcion():
    # Arrange
    mock_pasarela = MagicMock()
    mock_pasarela.cobrar.side_effect = ConnectionError("Pasarela no disponible")
    procesador = ProcesadorPago(pasarela=mock_pasarela)
    # Act + Assert
    with pytest.raises(ConnectionError):
        procesador.procesar(monto=50.0, cliente="luis@mail.com")

def test_pago_falla_con_monto_cero():
    mock_pasarela = MagicMock()
    procesador = ProcesadorPago(pasarela=mock_pasarela)
    with pytest.raises(ValueError, match="El monto debe ser mayor que cero"):
        procesador.procesar(monto=0, cliente="ana@mail.com")