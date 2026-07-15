---
name: fap-whatsapp-api
description: >-
  Redacta mensajes 1:1 de WhatsApp para FAP con cumplimiento de la WhatsApp
  Business API. Burbujas cortas, tono humano conversacional, sin asunto ni
  preheader, enlace de acción como pieza principal. Distingue plantilla aprobada
  (HSM) para mensajes que INICIAN la conversación vs. mensajes de sesión (dentro
  de ventana). Úsala al escribir WhatsApp uno a uno, difusión iniciada o
  confirmaciones por WhatsApp de FAP. Consulta antes la fuente de verdad `fap`.
---

# Skill · `fap-whatsapp-api`

**Rol:** mensajes **1:1** por WhatsApp + **cumplimiento de la API**.

> ⚠️ **Antes de generar cualquier pieza, consulta la fuente de verdad (skill `fap`)** —
> contexto, candados de voz, objeciones a anticipar y léxico del cliente. Manda sobre esta skill.

## Craft (rescatado de las skills 081/226 del banco)
- Burbujas cortas, tono humano y conversacional.
- Sin asunto ni preheader (no es email).
- Enlace de acción como pieza principal.

## Cumplimiento API
- Un mensaje que **inicia** la conversación va como **plantilla aprobada (HSM)**, no como
  mensaje de sesión.
- Los mensajes dentro de ventana de sesión (respuesta del usuario) sí van como sesión.

## Piezas producidas
- [`piezas/whatsapp-confirmacion-compra.md`](../../../piezas/whatsapp-confirmacion-compra.md)
  — adaptación WhatsApp del email de confirmación de compra (va como HSM).

## Estado
- [x] Instalada.
- [ ] Test de activación en chat nuevo pendiente.
