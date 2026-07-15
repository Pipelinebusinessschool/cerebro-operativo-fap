# Piezas · SALIDAS / TESTS — NO son fuente de nada

Esta carpeta guarda **piezas que el cerebro produjo** (tests, validaciones, ejemplos). Es el
**output**, no el input.

## 🔒 Regla (candado de arquitectura)

- **Ninguna skill carga `piezas/` como fuente.** Ni concepción, ni ángulos, ni voz, ni cifras,
  ni "el nombre del workshop" salen de aquí.
- Las **dos únicas fuentes** son:
  - `contexto/` → **la verdad** (ICP, métricas, voz, filosofía, objeciones…).
  - `swipe/` → **el craft** (moldes, ejemplos ganadores, `modelo-concepcion.md`).
- La **concepción de cada lanzamiento se genera FRESCA** con `fap-narrativa` (desde `contexto/` +
  `swipe/modelo-concepcion.md`). **No se reutiliza** la concepción de un funnel-test de aquí como
  si fuera canónica — hacerlo propaga la deriva (así se colaron "fichar/figuritas", vocabulario
  que no es de Jorge).

> Si necesitas un ejemplo de referencia, cítalo **como ejemplo**, nunca como verdad. Un test puede
> tener errores; la fuente de verdad, no.

## Qué hay aquí (todo es test/output)

- `funnel-contratacion-alto-rendimiento.md` — **test** del cerebro (Ruta B). *No es fuente.*
- `funnel-tomapedidos.md` — test.
- `landing-*.html` — landings de prueba renderizadas.
- `whatsapp-confirmacion-compra.md` — ejemplo de la **excepción transaccional** (una confirmación
  de compra ya hecha sí lleva precio). Se cita como ejemplo en `fap` y `fap-whatsapp-api`, **no
  como fuente de datos**.
