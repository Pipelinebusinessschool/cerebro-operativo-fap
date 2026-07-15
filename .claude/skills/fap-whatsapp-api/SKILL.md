---
name: fap-whatsapp-api
description: >-
  Redacta mensajes 1:1 de WhatsApp de FAP (nurture, pre-call, recordatorios, reactivación) con cu
  mplimiento de la WhatsApp Business API (plantilla HSM vs. mensaje de sesión). Úsala al escribir
   WhatsApp uno a uno de FAP.
---

# Skill · `fap-whatsapp-api`

**Rol:** mensajes **1:1 por WhatsApp** (invitación, recordatorio, pre-call, reactivación,
transaccional) + **cumplimiento de la API** (plantilla HSM vs. mensaje de sesión).

**Se activa cuando** el mensaje pide un WhatsApp 1:1 para FAP/PBS.

---

## Regla 0 — cargar SIEMPRE antes de escribir

1. **Verdad + candados →** [`../../../contexto/`](../../../contexto/). ICP, voz, métricas, candados.
2. **Craft →** esta skill trae su propia guía (abajo). **No hay swipe de WhatsApp** — por decisión:
   sin data de desempeño no se fabrica un swipe (ver `../../../swipe/README.md`).
3. **Buenas prácticas →** [`../../../swipe/principios-craft.md`](../../../swipe/principios-craft.md) — para
   **optimizar** (específico > genérico, un solo trabajo, CTA que nombra acción o valor).

> Cifras, ICP y precio salen **solo de `contexto/`**. Si falta el dato, PREGUNTA.

---

## Craft — patrones de WhatsApp 1:1

- **Burbujas cortas**, tono humano y conversacional (no email). Sin asunto ni preheader.
- **El enlace de acción es la pieza principal.**
- Cierre con **próximos pasos concretos** (fecha/hora/responsable) — regla universal PBS.

---

## Formato de entrega WhatsApp (paste-ready) — OBLIGATORIO

WhatsApp **no usa markdown**. Tiene su **propia sintaxis** (se escribe literal en el mensaje y la app
la renderiza). El mensaje se entrega **tal cual se pega**:

- `*negrita*` → **un solo asterisco** a cada lado (NO `**` de markdown).
- `_cursiva_` → un guion bajo a cada lado.
- `~tachado~` → una tilde a cada lado. · ` ```monoespaciado``` ` → tres backticks.
- Viñetas: `- ` o `* ` al inicio de línea. Numeradas: `1. `. Cita: `> `.
- **Enlaces:** URL cruda (WhatsApp la vuelve clickable); **no** existe `[texto](url)`. Un solo
  enlace = el CTA.

**Estilo:**
- `*Negrita*` para lo que decide (la idea, la cifra, el CTA). `_Cursiva_` para matices o el guiño
  conversacional. Con intención, no todo.
- **Emojis:** WhatsApp admite tono más cercano — úsalos con propósito (✅ ❌ 🚨 📅 👉 ⏳), **1–2 por
  burbuja**. Nunca infantil ni spam; la voz de Jorge sigue siendo ejecutiva y diagnóstica.
- **MAYÚSCULAS** de marca/énfasis: PIPELINE, FORECAST, EN VIVO, SIN COSTO, HOY.

**Burbujas:** mensajes cortos. Si son varias, **sepáralas con `—— (nueva burbuja) ——`** para que se
peguen una por una. La primera línea gancha; el CTA/enlace va al final.

**HSM (plantilla):** marca las variables como `{{1}}`, `{{2}}`… y **lista debajo qué es cada una**
(nombre, fecha, link). El cuerpo con formato va igual con la sintaxis de WhatsApp.

## Cumplimiento API (candado técnico)

- Un mensaje que **inicia** la conversación (fuera de ventana de sesión) va como **plantilla
  aprobada (HSM)**, no como mensaje de sesión.
- Los mensajes **dentro de la ventana de sesión** (respuesta del usuario) sí van como sesión.

## Candados FAP (de `contexto/`)

- **Sin precio de FAP en captación.** *(Excepción: una pieza transaccional —p. ej. confirmación de
  compra del workshop de $47— sí puede llevar precio; no es captación de FAP. Ver, **solo como
  ejemplo (no fuente)**, [`../../../piezas/whatsapp-confirmacion-compra.md`](../../../piezas/whatsapp-confirmacion-compra.md).)*
- **CTA único** por mensaje (registro o diagnóstico).
- **Cifras solo de `contexto/`** · **voz de Jorge** · **problema sistémico, nunca personal**.

## Proceso

1. Recibe el brief + momento (invitación / recordatorio / pre-call / reactivación / transaccional).
2. Carga `contexto/`.
3. Escribe en burbujas cortas, **en formato WhatsApp paste-ready** (`*negrita*`, `_cursiva_`, emojis,
   URL cruda), define **HSM vs. sesión**, un CTA.
4. **Auto-crítica** (checklist) → corrige.
5. Entrega el mensaje **listo para pegar** (+ variables `{{n}}` si es HSM). Falta de dato →
   `[FALTA: …]` + pregunta.

## Checklist de presión (pre-entrega)
- [ ] **Formato WhatsApp:** `*negrita*` (un asterisco), `_cursiva_`, emojis con propósito, URL cruda;
      nada de markdown `**`/`[texto](url)`.
- [ ] Burbujas cortas separadas (`—— nueva burbuja ——` si son varias). · [ ] HSM vs. sesión definido.
- [ ] Un solo CTA + enlace. · [ ] Próximos pasos concretos.
- [ ] Cifras sourced · sin precio de FAP en captación. · [ ] Voz de Jorge.

## Estado
- [ ] Test de activación en chat nuevo.
