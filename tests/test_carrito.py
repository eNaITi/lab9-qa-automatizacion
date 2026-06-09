# tests/test_carrito.py
import pytest

from app.carrito import Carrito

def test_carrito_vacio_al_iniciar(carrito_vacio):
    # Arrange: fixture ya nos da un carrito vacío
    # Act + Assert
    assert carrito_vacio.cantidad() == 0

def test_agregar_producto_incrementa_cantidad(carrito_vacio):
    # Arrange
    # Act
    carrito_vacio.agregar("Laptop", 800)
    # Assert
    assert carrito_vacio.cantidad() == 1

def test_total_suma_precios_correctamente(carrito_vacio):
    # Arrange + Act
    carrito_vacio.agregar("Laptop", 800)
    carrito_vacio.agregar("Monitor", 300)
    # Assert
    assert carrito_vacio.total() == 1100

def test_agregar_producto_duplicado_incrementa_cantidad(carrito_vacio):
    # Act
    carrito_vacio.agregar("Laptop", 800)
    carrito_vacio.agregar("Laptop", 800)
    # Assert
    assert carrito_vacio.cantidad() == 2

def test_vaciar_deja_carrito_en_cero(carrito_vacio):
    # Arrange
    carrito_vacio.agregar("Laptop", 800)
    carrito_vacio.agregar("Monitor", 300)
    # Act
    carrito_vacio.vaciar()
    # Assert
    assert carrito_vacio.cantidad() == 0

def test_agregar_precio_negativo_lanza_error(carrito_vacio):
    with pytest.raises(ValueError, match="El precio no puede ser negativo"):
        carrito_vacio.agregar("Laptop", -100)