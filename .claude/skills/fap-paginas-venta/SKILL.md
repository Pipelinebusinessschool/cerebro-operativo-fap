---
name: fap-paginas-venta
description: >-
  Produce o revisa las páginas de venta y OTOs de FAP: la página que aloja la VSL, el workshop de
   pago (tripwire), upsells y la página del diagnóstico. Úsala al crear páginas de venta u oferta
   del funnel de FAP.
---

# Skill · `fap-paginas-venta`

**Rol:** producir **páginas que venden** en el funnel de FAP — la página del **workshop de entrada
(tripwire de pago)**, los **OTOs** (upsell/downsell) y la **página del diagnóstico pago (OTU)**. Aquí
**sí hay precio, oferta y checkout**. *El diagnóstico gratuito post-workshop **no** lleva página: se
agenda directo por link (fuera del alcance de esta skill).*

**Se activa cuando** el mensaje pide una página de ventas, un OTO/upsell, la página del workshop de
pago, o la página del diagnóstico pago (OTU) de FAP.

> **Siempre se entregan DOS versiones (corta + larga) y siempre se evalúa la UX.** Ver la sección
> [Dos versiones + UX](#dos-versiones-siempre--evaluación-ux).

---

## Regla 0 — cargar SIEMPRE antes de escribir

1. **Verdad + candados →** [`../../../contexto/`](../../../contexto/). Incluye **`contexto/README.md` §Los dos
   diagnósticos** (no confundir gratuito vs pago) y, para páginas de venta, los **6 pilares** de
   `jorge_decisions.md`.
2. **Autoridad (verbatim) →** [`../../../contexto/autoridad.md`](../../../contexto/autoridad.md). **La sección de
   autoridad y la foto de Jorge se toman de aquí sin reescribir** — la misma que la landing de
   Supervisión Comercial con IA. Si el bloque exacto está `[FALTA]`, se deja marcado, no se rellena.
3. **Craft →** [`../../../swipe/swipe-paginas-venta.md`](../../../swipe/swipe-paginas-venta.md) — anatomía de
   la página de venta, del OTO y de la página de diagnóstico.
4. **Buenas prácticas →** [`../../../swipe/principios-craft.md`](../../../swipe/principios-craft.md) — para
   **optimizar, no solo replicar** (el swipe es el piso, no el techo).

> Cifras y precio salen **solo de `contexto/`**. El **precio de FAP NUNCA** aparece; el del
> **workshop/OTO sí**. Si falta un dato, PREGUNTA.

---

## Craft (del swipe)

**Página de venta (tripwire):** countdown → **H1 = mecanismo + resultado + plazo** → CTA con precio
→ prueba social (logos + Nº directivos) → modelo/diagrama → **dolores ("para ti si…")** → **tablas
de resultados cuantificados** → testimonios con nombre → **bio de Jorge (de `contexto/autoridad.md`,
verbatim, con la foto oficial)** → demo del producto → stack "lo que recibes" → **garantía** →
**justificación del precio** → FAQ → cierre.

**OTO (upsell inmediato):** interrupción ("aún NO está completa") + barra de progreso → H1 de deseo
→ reencuadre ("no es venta, es X") → **demo del entregable antes de comprarlo** → cómo funciona
(pasos) → **ancla de precio** ("vale ~$X → hoy $Y") → **doble CTA sí/no** (el "no" reafirma lo que
se pierde) → nota de honestidad.

### Los dos diagnósticos (ver `contexto/README.md`)

**A · Diagnóstico GRATUITO (post-workshop) — NO lleva página.** La llamada breve de 45 min se
**agenda directo** (link de calendario al cierre del workshop y en el correo de confirmación). **Esta
skill no produce una landing para el gratuito.** Lo único que puede hacer, si se pide, es el copy de
una **pantalla de confirmación mínima** ("gracias, agenda aquí") — nunca una página de ventas, sin
precio, sin scorecard ni Mapa de Facturación Oculta.

**B · Diagnóstico PAGO (oferta de única vez / OTU) — esta SÍ es una página.** Es el único diagnóstico
que esta skill maquina como página: usa el **molde OTO** (arriba) con su ancla de precio. **En
captación no se ahonda**; tratamiento mínimo y **sin mezclarlo** con el gratuito.

**Recursos que dan confianza:** ancla de precio · **honestidad como diferenciador** ("sin
contadores falsos ni cupos inventados") · garantía sin riesgo · prueba cuantificada (tablas con % y
$) por encima de adjetivos · escasez **real**, nunca fabricada.

---

## Dos versiones siempre + evaluación UX

**Toda página se entrega en DOS versiones**, no una:

- **Versión CORTA** — la mínima que convierte: promesa + prueba + oferta/CTA + autoridad + cierre.
  Para tráfico caliente, mobile, o cuando la decisión es simple (agendar el diagnóstico gratuito
  suele vivir bien en corta). Menos scroll, una sola idea por pantalla.
- **Versión LARGA** — la que argumenta a fondo: agrega dolores en escena, tablas de resultados,
  testimonios, demo, manejo de objeciones, FAQ, justificación de precio. Para tráfico frío/tibio o
  decisiones de mayor fricción (workshop de pago, OTU).

> La larga **no es la corta estirada**: cada sección extra se gana su lugar. La corta **no es la
> larga recortada al azar**: es una pieza con su propia arquitectura completa.

**Evaluación UX (obligatoria, se entrega junto a las páginas)** — revisa y deja constancia de:
- **Jerarquía visual:** una sola idea dominante por pantalla; el H1 y el CTA se entienden en 3 seg.
- **Un CTA, repetido:** misma acción arriba, medio y cierre; nada compite con él.
- **Escaneabilidad:** bloques cortos, subtítulos que cuentan la historia solos, viñetas, negritas
  con intención (estilo PBS: MAYÚSCULAS de marca/énfasis).
- **Mobile-first:** el pliegue superior comunica promesa + CTA sin hacer scroll; botones tocables.
- **Fricción del formulario/checkout:** pide lo mínimo; el botón nombra el valor, no la acción.
- **Confianza:** autoridad + prueba visibles cerca de cada CTA; nada fabricado.
- **Velocidad de comprensión:** si un directivo ocupado no capta la oferta en 10 seg, corrige.

---

## Optimización (ir más allá del swipe)

- **Largo no es corto estirado:** cada sección se gana su longitud. **"El medio es donde mueren las
  páginas"** — edítalo con más dureza que el hook o el cierre.
- **Precio y garantía son set pieces** con arquitectura propia — nunca un precio soltado al final.
- **Nombra las alternativas** contra las que compite el prospecto (CRM, agencia, consultor, no hacer
  nada) y demuestra con la matemática millonaria que la parcial cuesta más.
- **Los bonos no parchan una oferta débil** — primero afila el núcleo.
- **CTA que nombra acción o valor** + la frase previa que baja la duda residual.

## Candados FAP (de `contexto/`)

- **Cero precio de FAP** en cualquier pieza. El del **workshop de entrada / OTO / OTU sí** puede ir.
- **CTA único por página** — a checkout (workshop/OTO/OTU) **o** a agendar diagnóstico. Nunca ambos.
- **Diagnóstico gratuito ≠ pago.** El gratuito (post-workshop, 45 min) **no** promete scorecard/6
  pilares/Mapa de Facturación Oculta ni lleva precio. El pago (OTU) no se ahonda en captación.
- **Autoridad y foto = `contexto/autoridad.md`**, verbatim, idéntica en todas las piezas. Si está
  `[FALTA]`, se marca — no se rellena con una variante.
- **Cifras solo de `contexto/`** (Set B), como "promedio de clientes que implementaron", **nunca
  como promesa garantizada**.
- **Cero descuentos.** La negociación es de modalidad de pago, no de precio.
- **Nunca prometer sin condición** · **problema sistémico, nunca personal** · **voz de Jorge**.

## Proceso

1. Recibe el brief + tipo de página (workshop / OTO / **diagnóstico pago OTU**). *El diagnóstico
   gratuito no lleva página — si lo piden, aclara que se agenda por link.*
2. Carga `contexto/` (+ `autoridad.md` + §Los dos diagnósticos) + `swipe-paginas-venta.md`.
3. Escribe con el molde que corresponda, con cifras sourced, autoridad verbatim y (si aplica) ancla
   de precio.
4. Genera **las dos versiones (corta + larga)** y **evalúa la UX** (secciones de arriba).
5. **Auto-crítica** (checklist) → corrige.
6. Entrega ambas versiones + la nota de UX. Falta de dato → `[FALTA: …]` + pregunta.

## Checklist de presión (pre-entrega)
- [ ] **Dos versiones** entregadas (corta + larga), cada una con arquitectura propia.
- [ ] **Nota de UX** entregada (jerarquía, un CTA, escaneabilidad, mobile, fricción, confianza).
- [ ] **Autoridad + foto de `contexto/autoridad.md`**, verbatim; nada reescrito ni mezclado.
- [ ] **Diagnóstico correcto:** el gratuito NO se maquina como página (va por link); si es OTU, molde OTO, tratamiento mínimo.
- [ ] Un solo CTA por página. · [ ] Precio de FAP ausente. · [ ] Cifras sourced.
- [ ] Garantía + honestidad presentes (en las de pago). · [ ] Prueba cuantificada, no adjetivos.
- [ ] Sin escasez/contadores fabricados. · [ ] Voz de Jorge. · [ ] Nada prometido sin "para quien implementa".

## Estado
- [ ] Test de activación en chat nuevo.
- [ ] Prueba de fuego: página de diagnóstico de FAP desde el molde OTO1 + `jorge_process.md`.
