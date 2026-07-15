---
name: fap-vsl
description: >-
  Escribe el guion de la Video Sales Letter (VSL) de FAP para la Ruta A (venta directa: ad → VSL 
  → diagnóstico). Úsala al crear o revisar el guion de la VSL de captación de FAP.
---

# Skill · `fap-vsl`

**Rol:** escribir el **guion de la VSL** (Video Sales Letter) de FAP — el video que corre en
automático, hace que el prospecto se identifique con su problema y **agenda la llamada de
diagnóstico** (Ruta A: Ads → VSL → Diagnóstico). Es el guion hablado; la *página* que lo aloja la
hace `fap-paginas-venta`.

**Se activa cuando** el mensaje pide una VSL, un guion de video de venta/prospección, o el video de
la Ruta A de FAP.

---

## Regla 0 — cargar SIEMPRE antes de escribir

1. **Verdad + candados →** [`../../../contexto/`](../../../contexto/). En especial `jorge_philosophy.md`
   (diagnóstico sistémico), `jorge_process.md` (la Reunión 1 a la que agenda), `prueba.md` y
   `objeciones.md`. **Cifras, ICP y precio salen SOLO de aquí. Si falta el dato, PREGUNTA.**
2. **Craft →** [`../../../swipe/swipe-ads.md`](../../../swipe/swipe-ads.md) (sección C: **la VSL ganadora de
   FAP** — el mejor ad del banco) + [`../../../swipe/swipe-paginas-venta.md`](../../../swipe/swipe-paginas-venta.md)
   (la página que la aloja).
3. **Buenas prácticas →** [`../../../swipe/principios-craft.md`](../../../swipe/principios-craft.md) — para
   **optimizar, no solo replicar** (el swipe es el piso, no el techo).

---

## Craft — estructura de la VSL (beats)

1. **Hook / pattern interrupt** (primeros 3–8 seg) — el mecanismo #1 comprobado por datos: **callout
   de identidad** que niega el autoconcepto (*"No eres el CEO de tu empresa. Eres el vendedor más
   caro que tiene."*). Es lo único que decide si el resto se ve.
2. **Callout del prospecto** — para quién es (directivo/fundador B2B que dirige a ciegas).
3. **Problema + agitación** — el **diagnóstico sistémico** con el dolor del ICP en **verbatim**
   (`jorge_icp.md`): tomapedidos, dependencia del fundador, "un mes bien, tres mal".
4. **Reencuadre** — el problema es de diseño, no de la persona (**rota el fraseo, no repitas "es el
   sistema"** — ver `jorge_voice.md` §muletilla). *"'Así son las ventas B2B' es una gran mentira. Las
   ventas son sistemas, no heroísmos; procesos, no personalidades."*
5. **Autoridad / historia** — Jorge en el backstage de +100 operaciones; *"en el 87% de los casos el
   problema era idéntico"*.
6. **El mecanismo** — el sistema (los **6 pilares**, SM+EH+SS, AI-first) que elimina la dependencia
   del fundador y construye facturación predecible.
7. **Prueba** — cifras de `contexto/prueba.md` pegadas a su afirmación; casos/testimonios.
8. **Objeciones entretejidas** — *concede antes de contraatacar*, donde surge la duda (no al final).
9. **La oferta reencuadrada + CTA** — presenta el programa (FAP) **sin precio**; el CTA agenda el
   **diagnóstico**, encuadrado como *"no es una llamada de ventas, es un diagnóstico"*, con **filtro**
   (*"da clic únicamente si estás cansado de una operación de ventas desgastante"*).

**Notas de formato:** guion **hablado** — párrafos cortos, una idea = un golpe. Marca las señales
visuales con `[en pantalla: …]`. La retención es la métrica: abre loops, conflicto antes de
resolución, sin divagar.

---

## Optimización (ir más allá del swipe)

- **Los primeros 3 segundos son la VSL entera** — invierte casi todo el craft en el hook.
- **Callout de identidad = mecanismo #1** (comprobado con datos en `swipe-ads.md`): el espejo
  incómodo retiene.
- **Específico > ingenioso;** un solo **mensaje líder** en todo el guion.
- **Retención por estructura:** conflicto antes de resolución; cada bloque abre la pregunta que el
  siguiente responde.
- **Restraint:** corto y con ritmo; corta lo que no carga argumento (el relleno tiene firmas).
- **CTA que nombra la acción o el valor** ("agenda tu diagnóstico"), con la frase previa que baja la
  duda residual — nunca "haz clic" a secas.

---

## Candados FAP (de `contexto/`)

- **Cero precio de FAP.** La VSL de captación **no** lleva precio; presenta el programa y vende el
  **diagnóstico**.
- **CTA único → agendar diagnóstico.** Nada de checkout ni links secundarios.
- **Cifras solo de `contexto/`** (Set B), como "promedio de clientes que implementaron", **nunca
  como promesa garantizada**.
- **Voz de Jorge** (`jorge_voice.md`) · **el problema es sistémico, nunca personal** · **nunca
  prometer sin condición** ("para quien implementa, ejecuta y sigue el paso a paso").
- **ICP:** ≥$1M/año + ≥2 vendedores, B2B (excluye B2C y bienes raíces).

## Proceso

1. Recibe el brief (de `fap-narrativa`): ángulo, nivel de conciencia, duración objetivo.
2. Carga `contexto/` + `swipe-ads.md` (VSL) + `principios-craft.md`.
3. Escribe el hook (genera varios, corta al mejor) → los beats → CTA a diagnóstico.
4. **Auto-crítica** (checklist) → corrige.
5. Entrega. Falta de dato → `[FALTA: …]` + pregunta.

## Checklist de presión (pre-entrega)
- [ ] Hook de identidad/dolor en los primeros 3 seg (no el producto). · [ ] Un solo mensaje líder. ·
- [ ] Cifras sourced, pegadas a su afirmación. · [ ] **Sin precio de FAP.** · [ ] CTA único a
  diagnóstico, con filtro. · [ ] Voz de Jorge · problema sistémico. · [ ] Nada prometido sin "para
  quien implementa". · [ ] Ritmo hablado, sin relleno.

## Estado
- [ ] Test de activación en chat nuevo.
- [ ] Prueba de fuego: VSL de FAP desde el molde de `swipe-ads.md` (sección C).
