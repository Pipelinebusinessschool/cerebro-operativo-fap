# Banco de swipe — ejemplos ganadores reales

Este es el frente que cierra la brecha del testeo. Las skills tienen las **reglas** de las
piezas; el swipe les da los **ejemplos ganadores reales**. Un modelo con reglas produce algo
correcto; con ejemplos reales produce algo que se **parece a lo que funcionó**.

## Reglas del banco

1. **Un archivo por canal**, no uno gigante. Cada skill carga el suyo y se mantiene afilada.
   - `swipe-landings.md` → `fap-landings` *(piloto)*
   - `swipe-correos.md` → `fap-correos` ✅ *(11 fichas: A1–A9 invitación, B1–B2 venta; métricas pendientes)*
   - `swipe-ads.md` → `fap-video-ads-meta` ✅ *(6 ads con métricas reales de Meta; A05 = VSL de FAP)*
2. **Cada ejemplo con su "por qué ganó"**, no solo el texto. Copy + métrica + el elemento
   que lo hizo funcionar (hook / oferta / ángulo). Sin anotar, el modelo copia la superficie.
3. **Marcar qué NO copiar.** Si una ganadora tenía precio visible o CTA a checkout (que en
   FAP no van), se anota — el swipe no debe romper un candado.

## Estado

- **Piloto:** `landings`. Validado el formato → replicado a **correos** (`swipe-correos.md`, ✅).
- **Correos:** cargado el banco de PBS (invitación + venta). *Nota: el PDF "Casos de éxito"
  también trae correos de **recordatorio** y **postventa** (onboarding, downsell, upsell) que aún
  NO están en `swipe-correos.md`.*
- **Ads:** ✅ `swipe-ads.md` — 6 ads con métricas reales (A05 = VSL de FAP). Hallazgo clave:
  el **callout de identidad** es el mecanismo #1.
- **Pendiente:** un posible `swipe-paginas-venta.md` (el PDF trae opt-in, tripwire $11,
  diagnóstico $197 —molde directo del diagnóstico de FAP— y downsell $47).
- Con **3–5 ejemplos reales** por canal alcanza para extraer patrones. Importa que sean las
  verdaderas ganadoras, no la cantidad.
