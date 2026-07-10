# Skill · `fap-whatsapp-grupos`

**Rol:** mensajes de **comunidad por WhatsApp** (grupos) — bienvenida, dinamización, anuncios de
sesión, recordatorios de grupo. No es 1:1 (eso es `fap-whatsapp-api`).

**Se activa cuando** el mensaje pide copy para un grupo/comunidad de WhatsApp de FAP/PBS.

---

## Regla 0 — cargar SIEMPRE antes de escribir

1. **Verdad + candados →** [`../contexto/`](../contexto/). ICP, voz, métricas, candados.
2. **Craft →** guía propia (abajo). **Sin swipe** (decisión: sin data no se fabrica — ver
   `../swipe/README.md`).
3. **Buenas prácticas →** [`../swipe/principios-craft.md`](../swipe/principios-craft.md) — para
   **optimizar** (específico > genérico, un solo foco por mensaje, CTA que nombra acción o valor).

> Cifras, ICP y precio salen **solo de `contexto/`**. Si falta el dato, PREGUNTA.

---

## Craft — dinámica de comunidad

- Tono de **comunidad** (pertenencia, ritmo grupal), distinto al 1:1: se habla a "todos", se invita
  a participar, se celebra el avance del grupo.
- Cadencia de anuncios (es hoy / en vivo / repetición) alineada con el evento.
- Mensajes escaneables; un solo foco por mensaje.

---

## Formato de entrega WhatsApp (paste-ready) — OBLIGATORIO

WhatsApp **no usa markdown**. Tiene su **propia sintaxis** (se escribe literal y la app la renderiza).
El mensaje se entrega **tal cual se pega**:

- `*negrita*` → **un solo asterisco** a cada lado (NO `**` de markdown).
- `_cursiva_` → un guion bajo a cada lado.
- `~tachado~` → una tilde. · ` ```monoespaciado``` ` → tres backticks.
- Viñetas: `- ` o `* ` al inicio de línea. Numeradas: `1. `. Cita: `> `.
- **Enlaces:** URL cruda (se vuelve clickable); **no** existe `[texto](url)`. Un solo enlace = CTA.

**Estilo:**
- `*Negrita*` para el foco del anuncio (qué, cuándo, el CTA). `_Cursiva_` para el guiño de comunidad.
- **Emojis:** tono cercano y de pertenencia — con propósito (🔥 ✅ 📅 👏 👉 ⏳ 🎯), **1–2 por mensaje**.
  Nunca infantil ni spam; sigue siendo la voz de Jorge.
- **MAYÚSCULAS** de marca/énfasis: PIPELINE, FORECAST, EN VIVO, HOY.
- Escaneable: primera línea gancha, cuerpo corto, CTA al final. Un solo foco.

## Candados FAP (de `contexto/`)

- **Sin precio de FAP en captación** · **CTA único** por mensaje.
- **Cifras solo de `contexto/`** · **voz de Jorge** · **problema sistémico, nunca personal**.

## Proceso

1. Recibe el brief + momento (bienvenida / dinamización / anuncio / recordatorio).
2. Carga `contexto/`.
3. Escribe con tono de comunidad, un foco por mensaje, **en formato WhatsApp paste-ready**
   (`*negrita*`, `_cursiva_`, emojis, URL cruda).
4. **Auto-crítica** (checklist) → corrige.
5. Entrega el mensaje **listo para pegar**. Falta de dato → `[FALTA: …]` + pregunta.

## Checklist de presión (pre-entrega)
- [ ] **Formato WhatsApp:** `*negrita*` (un asterisco), `_cursiva_`, emojis con propósito, URL cruda;
      nada de markdown `**`/`[texto](url)`.
- [ ] Tono de comunidad, un foco por mensaje. · [ ] Un solo CTA. · [ ] Cifras sourced · sin precio
  de FAP. · [ ] Voz de Jorge.

## Estado
- [ ] Test de activación en chat nuevo.
