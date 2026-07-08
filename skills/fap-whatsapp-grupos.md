# Skill · `fap-whatsapp-grupos`

**Rol:** mensajes de **comunidad por WhatsApp** (grupos) — bienvenida, dinamización, anuncios de
sesión, recordatorios de grupo. No es 1:1 (eso es `fap-whatsapp-api`).

**Se activa cuando** el mensaje pide copy para un grupo/comunidad de WhatsApp de FAP/PBS.

---

## Regla 0 — cargar SIEMPRE antes de escribir

1. **Verdad + candados →** [`../contexto/`](../contexto/). ICP, voz, métricas, candados.
2. **Craft →** guía propia (abajo). **Sin swipe** (decisión: sin data no se fabrica — ver
   `../swipe/README.md`).

> Cifras, ICP y precio salen **solo de `contexto/`**. Si falta el dato, PREGUNTA.

---

## Craft — dinámica de comunidad

- Tono de **comunidad** (pertenencia, ritmo grupal), distinto al 1:1: se habla a "todos", se invita
  a participar, se celebra el avance del grupo.
- Cadencia de anuncios (es hoy / en vivo / repetición) alineada con el evento.
- Mensajes escaneables; un solo foco por mensaje.

## Candados FAP (de `contexto/`)

- **Sin precio de FAP en captación** · **CTA único** por mensaje.
- **Cifras solo de `contexto/`** · **voz de Jorge** · **problema sistémico, nunca personal**.

## Proceso

1. Recibe el brief + momento (bienvenida / dinamización / anuncio / recordatorio).
2. Carga `contexto/`.
3. Escribe con tono de comunidad, un foco por mensaje.
4. **Auto-crítica** (checklist) → corrige.
5. Entrega. Falta de dato → `[FALTA: …]` + pregunta.

## Checklist de presión (pre-entrega)
- [ ] Tono de comunidad, un foco por mensaje. · [ ] Un solo CTA. · [ ] Cifras sourced · sin precio
  de FAP. · [ ] Voz de Jorge.

## Estado
- [ ] Test de activación en chat nuevo.
