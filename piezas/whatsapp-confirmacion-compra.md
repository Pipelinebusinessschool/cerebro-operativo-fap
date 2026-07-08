# Pieza · WhatsApp — Confirmación de compra (entrenamiento $47)

**Skill:** `fap-whatsapp-api` · **Tipo:** transaccional (inicia conversación → va como **HSM / plantilla aprobada**).

> **Nota de candados:** aquí el precio **sí** va. Es la confirmación de una compra ya hecha
> del entrenamiento de $47, **no** captación de FAP, así que los candados de FAP no aplican.

Adaptación del email de confirmación al craft de WhatsApp: burbujas cortas, sin
asunto/preheader, sin "este correo es tu confirmación oficial", con el enlace de acceso como
acción principal.

---

## Versión en burbujas

**Burbuja 1 — confirmación**
> ¡Listo, [Nombre]! 🎉 Tu compra quedó confirmada.
> 💳 US$47 · pago único · acceso inmediato y vitalicio.

**Burbuja 2 — producto + enlace**
> Ya puedes entrar a tu entrenamiento "El método para construir un PIPELINE de +$1M con IA en 60 días" 👇
> [ENLACE_ACCESO]

**Burbuja 3 — lo que desbloqueó**
> Esto es lo que acabas de desbloquear:
> 🎬 3 clases grabadas de 90 min, a tu ritmo
> ♾️ Acceso vitalicio — vuelve cuando quieras
> ⚙️ Pack de prompts de IA (pitch, business case, battle cards)
> 🗺️ Plantilla del plan de prospección 3×3×30 (1 página)

**Burbuja 4 — arranque + soporte**
> Empieza por la clase 1 hoy mismo 🚀 ¿Algún problema para entrar? Respóndeme por aquí y lo resolvemos.
> — Jorge

---

## Opciones de Burbuja 1 (para A/B)

- **A · directa/celebratoria** — ¡Quedaste dentro, [Nombre]! 🎉 Compra confirmada: acceso inmediato y vitalicio a tu entrenamiento.
- **B · orientada a la acción** — Listo [Nombre] ✅ Ya tienes acceso de por vida al entrenamiento. Te paso el enlace 👇
- **C · valor por delante** — [Nombre], tu método para construir un PIPELINE de +$1M ya es tuyo 🔓 Pago confirmado, acceso vitalicio.
- **D · cercana, tono Jorge** — ¡Eso, [Nombre]! 🙌 Acabas de asegurar tu acceso vitalicio al entrenamiento. Vamos a montar tu pipeline.
- **E · mínima** — Compra confirmada, [Nombre] ✅ Acceso inmediato y vitalicio 👇

> Para mantener el dato del precio (US$47 · pago único) sin sonar fría: **A** o **E** lo cargan mejor.
> **C** y **D** empujan más al valor/arranque.

---

## Notas de despliegue

- **Va como HSM (plantilla aprobada)**, no como mensaje de sesión: inicia la conversación
  (llega justo tras la compra), fuera de ventana de sesión.
- La **Burbuja 3** se bajó de carga respecto al email (mismo valor, menos texto): en el
  celular una lista larga se salta.
- **Opción aún más ligera:** partir en dos envíos — enlace primero, stack después — para
  que el acceso llegue solo y limpio.
- **Variante para A/B pendiente de decisión:** versión mínima (solo confirmación + link, sin
  stack).

---

## Email original (fuente)

> **Asunto:** ✅ El entrenamiento de PIPELINE de +$1M con IA ya está disponible
> **Preheader:** Tu compra está confirmada. Aquí los accesos
>
> Producto: Entrenamiento grabado "El método para construir un PIPELINE de +$1M con IA en 60 días" ·
> Monto: US$47 (pago único) · Acceso: Inmediato y vitalicio.
> Incluye: entrenamiento completo (3 clases de 90 min), acceso vitalicio, pack de prompts de IA
> (pitch, business case, battle cards) y plantilla del plan de prospección 3×3×30 (1 página).
> Firma: Jorge Conde.
