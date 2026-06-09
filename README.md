Lab 9 — Automatización de Pruebas y Gestión de Defectos

Resultados de Cobertura
- `app/carrito.py`: 100%
- `app/descuentos.py`: 100%
- `app/pagos.py`: 100%
- **Total: 100%**



Respuestas a las Preguntas

k) ¿Qué líneas quedaron sin cubrir al ejecutar el primer reporte? ¿Por qué?

En el primer reporte quedaron sin cubrir:
- "carrito.py línea 11": el raise ValueError para precio negativo. No existía un test que intentara agregar un producto con precio negativo.
- **pagos.py línea 15**: el raise ValueError para monto <= 0. No existía un test que intentara procesar un pago con monto cero o negativo.

Ambas líneas corresponden a validaciones de casos borde que no fueron
consideradas en los tests iniciales. Se corrigió agregando un test específico
para cada caso.



l) ¿Significa cobertura 100% que el software no tiene bugs? Justifica con un ejemplo concreto del laboratorio.

No. La cobertura 100% solo garantiza que cada línea fue ejecutada al menos una vez, pero no garantiza que todos los comportamientos posibles sean correctos.

Ejemplo concreto: en "app/descuentos.py", el código con bugs tenía cobertura alta porque las líneas se ejecutaban, pero la fórmula "total * porcentaje" era incorrecta. El test con "total=0, PROMO10" pasaba (0 * 0.10 = 0.0, que coincidía con el esperado 0.0), dando falsa sensación de corrección. Solo los tests con valores distintos de cero detectaron el error de lógica.
La cobertura mide qué código se ejecuta, no si el resultado es correcto.



o) ¿Cuál fue la severidad que asignaste a cada bug? Justifica tu decisión.

- "BUG-LAB9-001" (fórmula incorrecta): Severidad HIGH.
  Afecta directamente el cálculo del precio final que paga el cliente.
  Un error en el descuento impacta en cada transacción con código promocional, generando pérdidas económicas o cobros incorrectos.

- BUG-LAB9-002 (falta validación total negativo): Severidad MEDIUM.
  Permite entradas inválidas sin lanzar error, lo que puede causar comportamientos inesperados, pero no afecta el flujo normal de compra ya que en condiciones normales el total nunca sería negativo.



p) ¿En qué se diferencia la severidad de la prioridad? Da un ejemplo donde ambas sean distintas.

- Severidad es el impacto técnico del bug en el sistema (cuánto daño causa).
- Prioridad es la urgencia de negocio para corregirlo (cuándo debe corregirse).

Ejemplo donde son distintas: un bug que muestra mal el logo de la empresa en la página de inicio tiene severidad LOW (no afecta funcionalidad) pero prioridad HIGH (el cliente lo ve inmediatamente y daña la imagen de marca).
En cambio, un bug en un módulo de reportes internos usado una vez al mes puede tener severidad HIGH pero prioridad LOW porque hay tiempo para corregirlo antes del próximo uso.