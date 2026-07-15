---
name: fap-lanzamientos
description: >-
  Director del lanzamiento de FAP. Define las 2 rutas de lanzamiento, las piezas
  que se producen en cada una y la cadencia (secuencia y timing). Úsala cuando
  pidan planificar, orquestar o secuenciar un lanzamiento/campaña de FAP, o
  decidir qué piezas producir y en qué orden. Invoca las skills de ejecución
  (fap-narrativa, fap-landings, fap-whatsapp-api, fap-whatsapp-grupos,
  fap-video-ads-meta). Consulta antes la fuente de verdad `fap`.
---

# Skill · `fap-lanzamientos`

**Rol:** director del lanzamiento. Define las **2 rutas**, las piezas de cada una y la cadencia.

> ⚠️ **Antes de generar cualquier pieza, consulta la fuente de verdad (skill `fap`)** —
> contexto, candados de voz, objeciones a anticipar y léxico del cliente. Manda sobre esta skill.

## Skills de ejecución que invoca
- `fap-narrativa` — 3 Big Ideas + brief.
- `fap-landings` — landing (modelo Largo Brunson / Corto Brasil).
- `fap-whatsapp-api` — 1:1 + cumplimiento API.
- `fap-whatsapp-grupos` — comunidad.
- `fap-video-ads-meta` — video ads, Jorge a cámara, Meta.

---

## Ruta A · Contenido / evento gratuito
**Validada en Fase 3** (workshop gratuito). Se capta con un evento de valor y se lleva del
evento a la **llamada de diagnóstico**.

| Paso | Qué produce | Skill de ejecución |
|---|---|---|
| **A1** | Narrativa + Big Idea del evento | `fap-narrativa` |
| **A2** | Landing de registro | `fap-landings` |
| **A3** | Video ads de tráfico al registro | `fap-video-ads-meta` |
| **A4** | Recordatorios y dinámica del evento (comunidad) | `fap-whatsapp-grupos` |
| **A5** | Seguimiento 1:1 y paso a diagnóstico | `fap-whatsapp-api` |

**Cadencia:** narrativa → landing + ads (tráfico) → registros → recordatorios (grupos) →
evento → seguimiento 1:1 → diagnóstico.

## Ruta B · Directo a diagnóstico (paid)
Del anuncio a la **llamada de diagnóstico**, sin evento intermedio.

| Paso | Qué produce | Skill de ejecución |
|---|---|---|
| **B1** | Video ads directos | `fap-video-ads-meta` |
| **B2** | Landing de captación (CTA a diagnóstico) | `fap-landings` |
| **B3** | Seguimiento 1:1 | `fap-whatsapp-api` |

Ángulo base opcional con `fap-narrativa` cuando haga falta reforzar el mensaje del ad.

**Cadencia:** ángulo → ads → landing → lead → seguimiento 1:1 → diagnóstico.

> Los correos (secuencia pre/durante/post del evento) todavía no tienen skill propia. Se
> resuelve en el pendiente abierto "consolidación de secuencias" del seguimiento.

## Estado
- [x] Instalada.
- [x] A1/B1 (y toda la cadena) nombran las skills de ejecución de FAP — ya no `agora` / `million-dollar-ads`.
- [ ] Test de activación en chat nuevo pendiente.
