# Skill · `fap-correos`

**Rol:** producir los **correos del funnel de FAP** en sus 4 fases — invitación, recordatorio,
venta y postventa — en la voz real de Jorge, sin inventar datos.

**Se activa cuando** el mensaje pide un correo (o secuencia) de FAP/PBS: "escríbeme el correo de
invitación al webinar", "la secuencia de recordatorio", "los correos de venta del cierre", etc.

---

## Regla 0 — cargar SIEMPRE antes de escribir

1. **Verdad + candados →** [`../contexto/`](../contexto/) (ICP, métricas, voz, precio, filosofía).
   **Cifras, ICP, precio y garantías salen SOLO de aquí. Si el dato no está, PREGUNTA — no lo
   inventes.**
2. **Craft →** [`../swipe/swipe-correos.md`](../swipe/swipe-correos.md) (ángulos, esqueleto PBS,
   patrones por fase). Es referencia de *cómo se escribe*, no de qué es verdad.

> **La verdad manda sobre el craft, siempre.** El swipe es de otros lanzamientos (PGE, SPG…): se
> copia la mecánica, **nunca sus cifras, promesas, precios ni nombres de producto**.

---

## Craft — el esqueleto PBS (del swipe)

Estructura base de un correo: **apelación identitaria** ("estratega/directivo comercial") →
**síntomas en lista** ("Si… / Si… / Si…" o checklist) → **reencuadre** ("no necesitas X, necesitas
Y") → **bullets de transformación** (verbo + resultado) → **doble CTA** (arriba + abajo, labels
distintos) → firma con cargo → a veces **PD** que revive el dolor o el costo de inacción.

**Un solo ángulo por correo.** Familias de asunto disponibles (menú para elegir/testear, **no**
fórmula fija — la mejor por etapa se valida con datos): pregunta-diagnóstico · alerta 🚨 ·
exclusión/contrarian 🚫 · historia-escena · resultado cuantificado · escasez con cifra · intriga.

**Recursos que rinden:** CTA en 1ª persona ("HAZME ESCALAR MI PIPELINE"), reencuadre esfuerzo→
sistema (quita la culpa al lector), contraste binario ❌/✅, future pacing ("supongamos que ya es
febrero de 2026"), marco macro que externaliza la urgencia, PD que revive la escena.

### Qué cambia por fase
- **Invitación** — capta el registro; rota el gancho para hablarle al mismo directivo desde un
  dolor distinto en cada envío. CTA a **registro**.
- **Recordatorio** — maximiza asistencia en vivo; cadencia por sesión (es hoy → 1 h antes → en
  vivo → **replay que caduca a 24 h**). Siembra la oferta en la sesión clave.
- **Venta** — retargeting a la oferta; **un ángulo por correo** y **escalera de urgencia real**
  (cupos → horas). El precio no se argumenta de frente: se reencuadra como **ROI** o **costo de
  inacción**.
- **Postventa** — onboarding del comprador + downsell (grabaciones) + upsell.

---

## Candados FAP (de `contexto/`, no se rompen)

- **Cero precio de FAP en captación.** (El precio del workshop de entrada / tripwire sí puede ir;
  el de FAP no.)
- **CTA único por pieza** — a registro (tope) **o** a diagnóstico (venta), nunca ambos ni links
  secundarios.
- **Cifras solo de `contexto/`** (métricas "Set B" de `pbs_metrics.md`), siempre como "promedio de
  clientes que implementaron", **nunca como promesa garantizada**.
- **Voz de Jorge** — respeta `jorge_voice.md`: vocabulario obligatorio (tomapedidos, matemática
  millonaria, pipeline/facturación predecible, SROI…) y **prohibido** (descuento, "es fácil", "te
  garantizo", "barato", "somos los mejores"…).
- **El problema es sistémico, nunca personal** — culpar al sistema, no al vendedor.
- **Nunca prometer sin condición** — "para quien implementa, ejecuta y sigue el paso a paso".
- **ICP:** ≥$1M/año + ≥2 vendedores, B2B (excluye B2C y bienes raíces).

---

## Proceso de escritura

1. **Recibe el brief** (o pídelo): fase, objetivo, ángulo deseado, nivel de conciencia del tráfico.
   Si no hay brief, apóyate en `fap-narrativa`.
2. **Carga** `contexto/` + `swipe-correos.md` (Regla 0).
3. **Elige** una familia de asunto + **un** ángulo.
4. **Escribe** con el esqueleto PBS, en voz de Jorge, con cifras sourced.
5. **Auto-crítica** antes de entregar (abajo) → corrige.
6. **Entrega.** Si faltó un dato de la fuente, **no lo inventes**: entrégalo con `[FALTA: …]` y la
   pregunta concreta para Jorge.

## Checklist de presión pre-entrega (8 puntos)

- [ ] **Acción clara:** un solo CTA, coherente con la fase (registro o diagnóstico).
- [ ] **Ajuste a conciencia:** el mensaje líder calza con el nivel de conciencia del tráfico.
- [ ] **Voz:** vocabulario obligatorio presente, ninguno prohibido.
- [ ] **Cifras sourced:** toda cifra sale de `contexto/`; nada inventado ni "Set A".
- [ ] **Candado de precio:** sin precio de FAP en captación.
- [ ] **Objeción cubierta / prueba alineada:** si afirma valor, hay razón para creer.
- [ ] **Un ángulo:** no amontona varios ganchos.
- [ ] **Promesa-cumplimiento:** nada que prometa resultados sin la cláusula de implementación.

---

## Estado
- [ ] Test de activación en chat nuevo.
- [ ] Prueba de fuego: generar la secuencia de invitación FAP y pasar el loop de auto-crítica.
