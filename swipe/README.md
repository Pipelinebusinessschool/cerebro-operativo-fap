# Banco de swipe — ejemplos ganadores reales

Este es el frente que cierra la brecha del testeo. Las skills tienen las **reglas** de las
piezas; el swipe les da los **ejemplos ganadores reales**. Un modelo con reglas produce algo
correcto; con ejemplos reales produce algo que se **parece a lo que funcionó**.

## Reglas del banco

1. **Un archivo por canal**, no uno gigante. Cada skill carga el suyo y se mantiene afilada.
   - `swipe-landings.md` → `fap-landings` *(opt-in de registro: landing ganadora de PGE + ICP ✅)*
   - `swipe-paginas-venta.md` → `fap-landings` / diagnóstico *(páginas de pago: workshop $11 + OTOs $197/$47 ✅)*
   - `swipe-correos.md` → `fap-correos` *(funnel de correo completo: invitación, recordatorio, venta y postventa ✅)*
   - `swipe-ads.md` → `fap-video-ads-meta` *(11 ads reales CON métricas: píldoras, video largo y la VSL de FAP ✅)*
   - **WhatsApp → sin swipe (decisión).** No hay data de desempeño de los mensajes, así que no se
     construye un swipe (crearlo sería inventar cuál "ganó" y romper la regla de oro). El canal se
     cubre con las skills existentes `fap-whatsapp-api` y `fap-whatsapp-grupos`, que ya cargan la
     guía de mensajes que funcionan.
2. **Cada ejemplo con su "por qué ganó"**, no solo el texto. Copy + métrica + el elemento
   que lo hizo funcionar (hook / oferta / ángulo). Sin anotar, el modelo copia la superficie.
   Sin data (p. ej. WhatsApp), no se fabrica un swipe: se usa la skill del canal.
3. **Marcar qué NO copiar.** Si una ganadora tenía precio visible o CTA a checkout (que en
   FAP no van), se anota — el swipe no debe romper un candado.

## Estado

- **Piloto:** `landings`. Validar el formato con un canal antes de replicar a mails y ads.
- Con **3–5 landings reales** alcanza para extraer patrones. Importa que sean las verdaderas
  ganadoras, no la cantidad.
