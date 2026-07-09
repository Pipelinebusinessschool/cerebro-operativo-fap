# Skill · `fap-whatsapp-api`

**Rol:** mensajes **1:1 por WhatsApp** (invitación, recordatorio, pre-call, reactivación,
transaccional) + **cumplimiento de la API** (plantilla HSM vs. mensaje de sesión).

**Se activa cuando** el mensaje pide un WhatsApp 1:1 para FAP/PBS.

---

## Regla 0 — cargar SIEMPRE antes de escribir

1. **Verdad + candados →** [`../contexto/`](../contexto/). ICP, voz, métricas, candados.
2. **Craft →** esta skill trae su propia guía (abajo). **No hay swipe de WhatsApp** — por decisión:
   sin data de desempeño no se fabrica un swipe (ver `../swipe/README.md`).
3. **Buenas prácticas →** [`../swipe/principios-craft.md`](../swipe/principios-craft.md) — para
   **optimizar** (específico > genérico, un solo trabajo, CTA que nombra acción o valor).

> Cifras, ICP y precio salen **solo de `contexto/`**. Si falta el dato, PREGUNTA.

---

## Craft — patrones de WhatsApp 1:1

- **Burbujas cortas**, tono humano y conversacional (no email). Sin asunto ni preheader.
- **El enlace de acción es la pieza principal.**
- Cierre con **próximos pasos concretos** (fecha/hora/responsable) — regla universal PBS.

## Cumplimiento API (candado técnico)

- Un mensaje que **inicia** la conversación (fuera de ventana de sesión) va como **plantilla
  aprobada (HSM)**, no como mensaje de sesión.
- Los mensajes **dentro de la ventana de sesión** (respuesta del usuario) sí van como sesión.

## Candados FAP (de `contexto/`)

- **Sin precio de FAP en captación.** *(Excepción: una pieza transaccional —p. ej. confirmación de
  compra del workshop de $47— sí puede llevar precio; no es captación de FAP. Ver
  [`../piezas/whatsapp-confirmacion-compra.md`](../piezas/whatsapp-confirmacion-compra.md).)*
- **CTA único** por mensaje (registro o diagnóstico).
- **Cifras solo de `contexto/`** · **voz de Jorge** · **problema sistémico, nunca personal**.

## Proceso

1. Recibe el brief + momento (invitación / recordatorio / pre-call / reactivación / transaccional).
2. Carga `contexto/`.
3. Escribe en burbujas cortas, define **HSM vs. sesión**, un CTA.
4. **Auto-crítica** (checklist) → corrige.
5. Entrega. Falta de dato → `[FALTA: …]` + pregunta.

## Checklist de presión (pre-entrega)
- [ ] Burbujas cortas, enlace de acción claro. · [ ] HSM vs. sesión definido. · [ ] Un solo CTA. ·
- [ ] Próximos pasos concretos. · [ ] Cifras sourced · sin precio de FAP en captación. · [ ] Voz de Jorge.

## Estado
- [ ] Test de activación en chat nuevo.
