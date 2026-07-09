# Skill · `fap-paginas-venta`

**Rol:** producir **páginas que venden** en el funnel de FAP — la página del **workshop de entrada
(tripwire de pago)**, los **OTOs** (upsell/downsell) y la **página de diagnóstico** (la que agenda
la llamada). A diferencia del opt-in (`fap-landings`), aquí **sí hay precio, oferta y checkout**.

**Se activa cuando** el mensaje pide una página de ventas, un OTO/upsell, la página del workshop de
pago, o la página que vende la llamada de diagnóstico de FAP.

---

## Regla 0 — cargar SIEMPRE antes de escribir

1. **Verdad + candados →** [`../contexto/`](../contexto/). Para la página de diagnóstico, además
   `jorge_process.md` (estructura de la Reunión 1) y los **6 pilares** de `jorge_decisions.md`.
2. **Craft →** [`../swipe/swipe-paginas-venta.md`](../swipe/swipe-paginas-venta.md) — anatomía de
   la página de venta, del OTO, y el **molde del diagnóstico** (OTO1 $197).
3. **Buenas prácticas →** [`../swipe/principios-craft.md`](../swipe/principios-craft.md) — para
   **optimizar, no solo replicar** (el swipe es el piso, no el techo).

> Cifras y precio salen **solo de `contexto/`**. El **precio de FAP NUNCA** aparece; el del
> **workshop/OTO sí**. Si falta un dato, PREGUNTA.

---

## Craft (del swipe)

**Página de venta (tripwire):** countdown → **H1 = mecanismo + resultado + plazo** → CTA con precio
→ prueba social (logos + Nº directivos) → modelo/diagrama → **dolores ("para ti si…")** → **tablas
de resultados cuantificados** → testimonios con nombre → bio de Jorge → demo del producto → stack
"lo que recibes" → **garantía** → **justificación del precio** → FAQ → cierre.

**OTO (upsell inmediato):** interrupción ("aún NO está completa") + barra de progreso → H1 de deseo
→ reencuadre ("no es venta, es X") → **demo del entregable antes de comprarlo** → cómo funciona
(pasos) → **ancla de precio** ("vale ~$X → hoy $Y") → **doble CTA sí/no** (el "no" reafirma lo que
se pierde) → nota de honestidad.

**Página de diagnóstico (molde OTO1 → llamada FAP):** reencuadre "**no es una llamada de ventas,
es un diagnóstico**" → demo del Scorecard (los **6 pilares** + Índice de Dependencia del Fundador) →
cómo funciona (cuestionario → auditoría → scorecard → **sesión 1:1**) → **CTA a agendar
diagnóstico**. Estructura de la sesión: `jorge_process.md` (apertura → calificación MEDIC →
presentación demostrativa → matemática millonaria).

**Recursos que dan confianza:** ancla de precio · **honestidad como diferenciador** ("sin
contadores falsos ni cupos inventados") · garantía sin riesgo · prueba cuantificada (tablas con % y
$) por encima de adjetivos · escasez **real**, nunca fabricada.

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

- **Cero precio de FAP** en cualquier pieza. El del **workshop de entrada / OTO sí** puede ir.
- **CTA único por página** — a checkout (workshop/OTO) **o** a agendar diagnóstico. Nunca ambos.
- **Cifras solo de `contexto/`** (Set B), como "promedio de clientes que implementaron", **nunca
  como promesa garantizada**.
- **Cero descuentos.** La negociación es de modalidad de pago, no de precio.
- **Nunca prometer sin condición** · **problema sistémico, nunca personal** · **voz de Jorge**.

## Proceso

1. Recibe el brief + tipo de página (workshop / OTO / diagnóstico).
2. Carga `contexto/` + `swipe-paginas-venta.md` (+ `jorge_process.md` si es diagnóstico).
3. Escribe con el esqueleto que corresponda, con cifras sourced y ancla de precio.
4. **Auto-crítica** (checklist) → corrige.
5. Entrega. Falta de dato → `[FALTA: …]` + pregunta.

## Checklist de presión (pre-entrega)
- [ ] Un solo CTA (checkout O diagnóstico). · [ ] Precio de FAP ausente. · [ ] Cifras sourced. ·
- [ ] Garantía + honestidad presentes. · [ ] Prueba cuantificada, no adjetivos. · [ ] Sin
  escasez/contadores fabricados. · [ ] Voz de Jorge. · [ ] Nada prometido sin "para quien implementa".

## Estado
- [ ] Test de activación en chat nuevo.
- [ ] Prueba de fuego: página de diagnóstico de FAP desde el molde OTO1 + `jorge_process.md`.
