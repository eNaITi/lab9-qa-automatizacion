# app/descuentos.py — CORREGIDO
CODIGOS_DESCUENTO = {
    "PROMO10": 0.10,
    "PROMO20": 0.20,
}

def calcular_descuento(total: float, codigo: str) -> float:
    """
    Calcula el total con descuento aplicado.
    Raises ValueError si total es negativo.
    """
    if total < 0:
        raise ValueError("El total no puede ser negativo")
    porcentaje = CODIGOS_DESCUENTO.get(codigo, 0)
    return total - (total * porcentaje)