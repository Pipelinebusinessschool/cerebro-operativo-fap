# Skill · `fap-whatsapp-api`

**Rol:** mensajes **1:1** por WhatsApp + **cumplimiento de la API**.

## Craft (rescatado de las skills 081/226 del banco)
- Burbujas cortas, tono humano y conversacional.
- Sin asunto ni preheader (no es email).
- Enlace de acción como pieza principal.

## Cumplimiento API
- Un mensaje que **inicia** la conversación va como **plantilla aprobada (HSM)**, no como
  mensaje de sesión.
- Los mensajes dentro de ventana de sesión (respuesta del usuario) sí van como sesión.

## Piezas producidas
- [`../piezas/whatsapp-confirmacion-compra.md`](../piezas/whatsapp-confirmacion-compra.md)
  — adaptación WhatsApp del email de confirmación de compra (va como HSM).

## Estado
- [x] Instalada.
- [ ] Test de activación en chat nuevo pendiente.
