---
name: fap-landings
description: >-
  Produce o revisa landings de captación de FAP (opt-in de registro) en dos modelos: Largo (Bruns
  on) y Corto (Brasil). Úsala al escribir, estructurar o auditar una landing o página de registro
   de FAP.
---

# Skill · `fap-landings`

**Rol:** producir **landings de registro (opt-in)** de FAP — la página que capta el email para un
webinar/entrenamiento gratuito. **Una sola decisión: dar el correo.** (Las páginas que venden —
workshop de pago, OTOs, diagnóstico — las hace `fap-paginas-venta`.)

**Se activa cuando** el mensaje pide una landing/página de registro, opt-in o de captura para FAP.

---

## Regla 0 — cargar SIEMPRE antes de escribir

1. **Verdad + candados →** [`../../../contexto/`](../../../contexto/). ICP, voz, métricas, candados.
2. **Craft →** [`../../../swipe/swipe-landings.md`](../../../swipe/swipe-landings.md) — anatomía de la landing
   ganadora, ángulos de promesa y la **lectura del ICP** (las 3 narrativas del prospecto).
3. **Buenas prácticas →** [`../../../swipe/principios-craft.md`](../../../swipe/principios-craft.md) — para
   **optimizar, no solo replicar** (el swipe es el piso, no el techo).

> Cifras, ICP y precio salen **solo de `contexto/`**. Si falta el dato, PREGUNTA.

---

## Craft — el esqueleto opt-in (del swipe)

eyebrow (formato en vivo) → **H1 = promesa** → **formulario mínimo** (solo email, botón en 1ª
persona: "Quiero escalar mi PIPELINE", no "Enviar") → **prueba social** (logos de medios) →
**cronograma numerado** (hace tangible el valor gratis) → **CTA** → **Antes/Después** (tabla de
contraste 🚫/✅) → **bio del entrenador** (autoridad con cifras) → footer.

**Fórmula del H1:** `Cómo [construir/estructurar] un sistema de prospección B2B con IA` `+
[beneficio: pipeline/forecast/decisores] + [plazo: 2026 / 90 días] + [ventaja: antes que la
competencia]`. Rota el beneficio/ventaja; el mecanismo ("sistema con IA") es constante.

**Lectura del ICP (enmarca la promesa):** buscan **inmediatez** (nunca vender como algo lento) ·
quieren IA **aplicada, no técnica** (problema estratégico) · quieren **independencia** (sin
depender de más vendedores).

**Modelos:** corto/directo (default de opt-in) o largo (Brunson) si el tráfico es más frío.

---

## Optimización (ir más allá del swipe)

- **Un solo trabajo**; corta cualquier otra acción de la página.
- **Continuidad de entrada es sagrada:** el hero refleja la promesa del ad que trajo al lector (no
  un headline genérico).
- **El hero se gana el scroll** — trátalo como un entregable en sí.
- **Frío ≠ tibio ≠ caliente:** el frío necesita problema + mecanismo; el caliente, oferta + prueba.
  La **longitud = peso de la decisión**, no preferencia.
- **Prueba pegada a su afirmación;** testimonios en los que el lector se reconozca.

## Candados FAP (de `contexto/`)

- **Sin precio** — el opt-in es gratis; su único objetivo es el registro.
- **CTA único → registro.** Nada de checkout ni links secundarios.
- **Cifras solo de `contexto/`** (Set B), como "promedio de clientes que implementaron".
- **Voz de Jorge** y **problema sistémico, nunca personal**.
- **ICP:** ≥$1M/año + ≥2 vendedores.

## Proceso

1. Recibe el brief (de `fap-narrativa`): promesa, nivel de conciencia, ruta.
2. Carga `contexto/` + `swipe-landings.md`.
3. Escribe el H1 (fórmula) + los bloques del esqueleto, en voz de Jorge.
4. **Auto-crítica** (checklist) → corrige.
5. Entrega. Falta de dato → `[FALTA: …]` + pregunta.

## Checklist de presión (pre-entrega)
- [ ] Un solo CTA, a registro. · [ ] H1 = promesa clara (mecanismo+resultado+plazo). ·
- [ ] Fricción mínima (solo email). · [ ] Cronograma tangible. · [ ] Antes/Después escaneable. ·
- [ ] Cifras sourced. · [ ] Voz de Jorge. · [ ] Sin precio.

## Estado
- [ ] Test de activación en chat nuevo.
