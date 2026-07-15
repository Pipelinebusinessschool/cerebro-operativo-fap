---
name: fap-correos
description: >-
  Escribe secuencias de correo (email) para lanzamientos de FAP: invitación /
  registro, recordatorios pre-evento, correos durante y post-evento, paso a la
  llamada de diagnóstico, reactivación de no-shows y nurture de leads que no
  agendan. Craft de email (asunto + preheader, un solo CTA, escaneable), voz
  regional del cliente y candados heredados (sin precio en captación, CTA a
  diagnóstico). Úsala al redactar o revisar correos / secuencias de email de
  FAP. Consulta antes la fuente de verdad `fap`.
---

# Skill · `fap-correos`

**Rol:** producir **secuencias de correo** del lanzamiento — invitación, recordatorios,
post-evento, reactivación y nurture. Es la hermana por email de `fap-whatsapp-api` /
`fap-whatsapp-grupos`: **mismo mensaje, distinto canal.**

> ⚠️ **Antes de generar cualquier pieza, consulta la fuente de verdad (skill `fap`)** —
> contexto, candados de voz, objeciones a anticipar y léxico del cliente. Manda sobre esta skill.

## Candados heredados de `fap`
- ❌ Sin precio visible en correos de **captación**.
- ✅ CTA a agendar **llamada de diagnóstico** (no checkout).
- ✅ Tono B2B high-ticket (autoridad y método, no urgencia de infoproducto).

> **Excepción transaccional:** un correo que **confirma una compra ya hecha** (p. ej. el
> entrenamiento de $47) **sí** lleva precio — no es captación. Es el mismo caso del email
> que originó [`piezas/whatsapp-confirmacion-compra.md`](../../../piezas/whatsapp-confirmacion-compra.md).

## Craft del correo (a diferencia de WhatsApp)
- **Sí** lleva **asunto** y **preheader** (WhatsApp no) — trabájalos como pieza: curiosidad o
  beneficio concreto, sin clickbait de infoproducto.
- **Un solo CTA principal** por correo (a la llamada de diagnóstico o al registro del evento).
- Cuerpo **escaneable**: párrafos cortos, una idea por bloque.
- Voz **regional y humana**, abre desde el dolor con el léxico del cliente
  (`cuello de botella`, `cerrar la pinza`…). Ver checklist de voz en `fap`.
- Anticipa objeciones **dentro** del correo (sobre todo 1–3: costo recurrente, "lo tengo que
  consultar", "mi negocio es especial").

## Tipos de correo / secuencia

**Ruta A · evento gratuito (workshop)** — la secuencia validada en Fase 3:
1. **Invitación / registro** — vende la asistencia al evento (no el producto).
2. **Recordatorios pre-evento** — valor + fricción baja para asistir.
3. **Durante / arranque** — enlace de acceso, qué se llevan.
4. **Post-evento → diagnóstico** — puente del contenido a la **llamada de diagnóstico**.

**Transversales:**
- **Reactivación de no-shows** — quien se registró y no asistió.
- **Nurture** — leads que no agendan aún; mantener el hilo sin quemar.

## Relación con las demás skills
- El **ángulo y las Big Ideas** vienen del brief de `fap-narrativa`.
- La **cadencia y en qué paso entra cada correo** la fija `fap-lanzamientos` (Ruta A).
- La landing de destino la produce `fap-landings`.

## Estado
- [x] Instalada.
- [ ] Conectar swipe de correos ganadores (`swipe/swipe-emails.md`, hoy pendiente).
- [ ] Test de activación en chat nuevo pendiente.
