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

## Swipe (ejemplos ganadores reales)
**Carga [`swipe/swipe-correos.md`](../../../swipe/swipe-correos.md) antes de redactar.** Es el
banco de correos que de verdad se enviaron en lanzamientos de PBS (PGE, Pipeline Predecible,
Supervisión Comercial, SPG). Aprende de ahí los **ángulos, la estructura y los recursos** que
funcionan en la voz real de Jorge — no frases sueltas.

> 🔒 **Candado del swipe (obligatorio):** ese material es de **otros programas, no de FAP**. Sirve
> de **molde de craft**, nunca de contenido. En concreto:
> - **No transplantar cifras ni promesas** (`$1M en 90 días`, `x10`, `5X`, `100+ oport./mes`…).
>   En FAP solo va lo que esté en la fuente de verdad `fap`. Es la regla anti-invención.
> - Los correos de **venta** del swipe llevan a **checkout con precio/escasez**; en captación de
>   FAP el CTA es a **diagnóstico**. Se copia la *mecánica* (urgencia, contraste ❌/✅), no el destino.
> - **No inventar escasez** (cupos, cuenta regresiva) si no es real.
>
> Moldes reutilizables ya identificados: checklist de falsas soluciones (A9), escena en 2ª persona
> + PD (A6), dos caminos ❌/✅ (B2), reencuadre "no necesitas X, necesitas Y" (A2).

## Relación con las demás skills
- El **ángulo y las Big Ideas** vienen del brief de `fap-narrativa`.
- La **cadencia y en qué paso entra cada correo** la fija `fap-lanzamientos` (Ruta A).
- La landing de destino la produce `fap-landings`.

## Estado
- [x] Instalada.
- [x] Swipe de correos ganadores conectado (`swipe/swipe-correos.md`, 11 fichas: A1–A9 invitación, B1–B2 venta).
- [ ] Métricas por correo pendientes (Jorge) — hoy "por qué ganó" es hipótesis de craft, no dato.
- [ ] Faltan tipos: confirmación de registro, recordatorios/no-show, postventa.
- [ ] Test de activación en chat nuevo pendiente.
