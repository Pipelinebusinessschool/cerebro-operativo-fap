---
name: fap-narrativa
description: >-
  Genera el Documento de Concepción de un lanzamiento FAP: 3 Big Ideas + avatar, enemigos, falsas
   creencias, vehículos rotos, dolores y promesas — el brief maestro que alimenta todas las pieza
  s. Úsala al arrancar el ángulo o concepto de una campaña FAP. La concepción se genera fresca aq
  uí, no se recicla de piezas anteriores.
---

# Skill · `fap-narrativa`

**Rol:** conducir la **investigación → reflexión → concepción** de un lanzamiento FAP y producir el
**Documento de Concepción** — el documento maestro del que se escribe *toda* pieza posterior
(correos, landings, ads, VSL, páginas). No entrega "3 ideas y un brief"; entrega la narrativa
completa del lanzamiento con cada aspecto evaluado (momento de mercado, avatar, conciencia,
enemigos, dolores, falsas creencias, vehículos rotos, munición, Gran Idea, promesas).

**Se activa cuando** el mensaje pide la concepción, la gran idea, el ángulo, la narrativa o el brief
de un lanzamiento FAP: "concibe el lanzamiento del workshop de supervisión", "dame la Big Idea y la
promesa", "arma la narrativa para estos correos".

> Esta skill es **upstream de todo**. Su salida —la concepción— es lo que consumen las skills de
> canal. Una concepción floja produce piezas flojas; por eso el listón es **igualar y superar** el
> nivel de los documentos de concepción reales de PBS.

---

## Regla 0 — cargar SIEMPRE antes de concebir

1. **Verdad + candados →** [`../../../contexto/`](../../../contexto/). ICP, voz, métricas, filosofía,
   objeciones, prueba, decisiones. **Define qué es verdad y qué se puede prometer.** Si un dato no
   está, se marca `[FALTA]` y se pregunta — **jamás se inventa.**
2. **Modelo de concepción →** [`../../../swipe/modelo-concepcion.md`](../../../swipe/modelo-concepcion.md) — el
   **molde, el estándar de razonamiento y el mapa concepción→copy.** Es la referencia obligatoria:
   define las secciones, la profundidad exigida y cómo cada elemento alimenta a las piezas.
3. **Craft →** el [`../../../swipe/`](../../../swipe/) relevante (correos, ads, landings, páginas) para calibrar
   ángulos que ya funcionaron.
4. **Buenas prácticas →** [`../../../swipe/principios-craft.md`](../../../swipe/principios-craft.md) — para
   **optimizar, no solo replicar** (el swipe es el piso, no el techo).

---

## El proceso — investigar, reflexionar, conceibir

La diferencia entre un brief pobre y una concepción real está en las **dos primeras fases**. No se
salta a escribir la Gran Idea: se llega a ella como conclusión.

### Fase 1 — INVESTIGAR (minar antes de afirmar)
Antes de escribir una sola sección del documento:
1. **Extrae de `contexto/`** todo lo relevante al tema: ICP y avatar, cifras y su fuente, objeciones
   mapeadas, prueba disponible, voz (obligatorio/prohibido), decisiones FAP, pilares.
2. **Mina el lenguaje del avatar (voice-of-customer):** recoge las frases **literales** que el avatar
   usa (de `contexto/`, transcripciones, encuestas si las hay). Esas frases serán hooks; no las
   parafrasees.
3. **Inventario de munición:** lista los datos duros, casos y analogías disponibles, cada uno con
   fuente. Lo que falte, a la lista de `[FALTA]`.
4. **Declara los huecos:** antes de conceibir, enuncia qué NO tienes (caso ancla con nombre, métrica
   específica del producto, dato de mercado). Eso evita que el razonamiento se apoye en aire.

### Fase 2 — REFLEXIONAR (razonar cada dimensión)
Para cada sección del modelo, **razona, no listes**:
- ¿Cuál es la **tensión** real? (lo que el avatar dice que quiere vs. lo que en verdad le duele).
- ¿Cuál es el **enemigo sistémico** detrás de cada dolor? (nunca "es malo vendiendo").
- ¿En qué **nivel de conciencia** está el tráfico y en qué **orden** hay que venderle?
- ¿Qué **mecanismo del problema** explica por qué el modelo viejo falla, y qué **mecanismo de la
  solución** (con nombre) lo resuelve distinto?
- ¿Qué **falsa creencia** bloquea cada objeción, y cuál es la **verdad** que la desarma (anclada)?
  Usa `contexto/objeciones.md` y `contexto/prueba.md`.

### Fase 3 — CONCEBIR (producir el documento)
Escribe el **Documento de Concepción** con las secciones del modelo, al volumen y profundidad que el
modelo exige (10+ declaraciones de problema, 10–12 dolores en escena, 10–12 falsas creencias en
tabla, 8–10 vehículos rotos, banco de munición con analogías). La **Gran Idea y las promesas van al
final**, como destilación de todo lo anterior — nunca como punto de partida.

### Fase 4 — AUTO-CRÍTICA (presión antes de entregar)
Somete el documento al **checklist de presión** (abajo). Corrige. Solo entonces entrega.

---

## Salida — el Documento de Concepción

Estructura completa (detalle, profundidad y mapa a copy en
[`../../../swipe/modelo-concepcion.md`](../../../swipe/modelo-concepcion.md)):

- **A · Momento del Mercado** — 3–4 fuerzas del "por qué ahora", cada una con dato/fuente.
- **B · Avatar en Profundidad** — quién es, su día, qué le miden, qué teme; perfiles por rol si aplica.
- **C · Categorización por Conciencia** — nivel de conciencia del tráfico + grupos + **orden de venta**
  + nombre funcional del avatar (4 filtros) si aplica.
- **D · Enemigo Común** — 5–6 enemigos con nombre, sistémicos y externos.
- **D.2 · 10 Declaraciones de Problema** — en primera persona, lenguaje literal del avatar.
- **D.3 · 3 Capas Emocionales** — dice / piensa / siente a las 3 AM.
- **E · Dolores** — operativos (escenas en 2ª persona) + personales/emocionales.
- **F · Falsas Creencias** — tabla *Creencia → Verdad → Enemigo* (vehículo / sí mismo / externo).
- **G · Vehículos Rotos** — *Lo que intentó · Por qué falló · Cómo lo hacemos diferente*.
- **H · Banco de Munición** — autoridad + métricas duras + estadísticas externas + analogías.
- **I · La Gran Idea + Desarrollo de la Gran Verdad** — la tesis + su prueba encadenada + mecanismos.
- **J · Nombres** — candidatos con análisis + recomendado.
- **K · Promesas + Sub-promesas** — mecanismo + resultado + plazo (sourced), con condición.
- **Mapa de uso** — recordatorio de cómo cada elemento alimenta a las piezas (del modelo, §3).

> Escalado: si el pedido es acotado ("solo la Gran Idea y la promesa para este ad"), se ejecutan las
> Fases 1–2 igual (investigar/reflexionar) pero se entregan **solo las secciones pedidas**, dejando
> constancia de qué del resto del documento las sostiene. La calidad del razonamiento no se recorta;
> el volumen sí.

---

## Optimización (ir más allá del swipe)

- **Un solo mensaje líder por pieza.** Los demás bajan a prueba de apoyo, no compiten por la posición
  líder. El orden de los mensajes es estratégico: un reclamo secundario revelado primero puede matar
  al principal.
- **Empareja el mensaje al nivel de conciencia**, no al feature list. Vende en el orden que el avatar
  pide (para FAP suele ser Resultado → Proceso → IA — nunca al revés).
- **Sofisticación de mercado:** en mercado saturado, lidera con **mecanismo único con nombre**, no con
  promesa desnuda (ya la oyeron).
- **La Gran Idea es tesis, no slogan:** si el avatar la acepta, comprar es la conclusión lógica.
- **Nombra las alternativas reales** (CRM, agencia, más SDRs, consultor, "vendedor estrella", no hacer
  nada) y posiciona contra cada una en los vehículos rotos.
- **Voice-of-customer:** cita el lenguaje literal del avatar; no lo pulas hasta volverlo genérico.
- **Story = estructura, no adorno:** conflicto antes de resolución; específico o córtalo.

## Candados FAP (de `contexto/`)

- **Cifras / ICP / precio / casos solo de `contexto/`.** Nada inventado. Falta → `[FALTA: …]` + pregunta.
- **Voz de Jorge** (`jorge_voice.md`): diagnóstica, con cifras, anti-victimización, sistémica; nunca
  motivacional vacía. Vocabulario obligatorio/prohibido.
- **El problema es sistémico, nunca personal** (culpa al sistema, no al avatar).
- **Nunca prometer sin condición** ("para quien implementa, ejecuta y sigue el paso a paso"). Sin
  garantías, sin "es fácil", sin "descuento/barato".
- **ICP:** ≥$1M/año + ≥2 vendedores, B2B (excluye B2C y bienes raíces).

## Checklist de presión (antes de entregar)

- [ ] ¿Investigué (Fase 1) antes de conceibir? ¿Hay lista explícita de `[FALTA]`?
- [ ] ¿Cada afirmación de cifra/caso está anclada en `contexto/` o marcada `[FALTA]`?
- [ ] ¿Hay ≥10 declaraciones de problema, ≥10 dolores en escena, ≥10 falsas creencias, ≥8 vehículos rotos?
- [ ] ¿Cada dolor tiene su enemigo **sistémico** detrás? ¿Ninguna culpa al avatar?
- [ ] ¿La Gran Idea es una **tesis** (no un slogan) y trae mecanismo del problema + de la solución?
- [ ] ¿El desarrollo de la Gran Verdad **prueba** la tesis encadenando enemigos + falsas creencias + munición?
- [ ] ¿El orden de venta calza con el nivel de conciencia del canal?
- [ ] ¿Las promesas tienen mecanismo + resultado + plazo *sourced* y condición? ¿Nada prohibido?
- [ ] ¿El **mapa de uso** deja claro cómo cada elemento alimenta correos/landings/ads/VSL/páginas?
- [ ] ¿Voz de Jorge en todo? ¿Vocabulario obligatorio presente, prohibido ausente?
- [ ] Prueba de suficiencia: ¿un copywriter que no conoce FAP podría escribir un email, un ad y una
      sección de landing solo con este documento (salvo datos `[FALTA]`)?

## Estado
- [ ] Test de activación en chat nuevo.
- [ ] Concepción de prueba contra un lanzamiento real (comparar contra brief de PBS).
