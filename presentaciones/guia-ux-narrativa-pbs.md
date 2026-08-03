# Guía de UX, Diseño y Narrativa — Rediseño Web B2B de PBS

> Síntesis accionable de todo el benchmark hecho hasta ahora. Complementa a
> `estrategia-rediseno-web-b2b.md` (diagnóstico + concepto + plan) y a
> `Benchmark-Web-B2B-PBS.pptx` (fichas por referente). Este documento responde una
> pregunta distinta: **con todo lo visto, ¿qué instrucciones concretas le damos a quien
> diseñe y escriba la web?**
>
> **Fuente de rigor:** 4 referentes auditados con HTML real, verbatim (McKinsey, Winning
> by Design, Accenture, Force Management). Simon-Kucher, Deloitte UK, Japón y V4 Company
> siguen en el benchmark original como recomendación conceptual — no auditados todavía
> con HTML real, así que sus patrones se citan con menos peso de evidencia que los cuatro
> anteriores.

---

## Parte 1 — Narrativa

### 1.1 Elegir una postura (no se puede sonar como los cinco a la vez)

Cada referente audita a una postura narrativa distinta. PBS hoy no tiene ninguna — mezcla
tono de escuela motivacional con datos de consultora sin comprometerse con ningún registro
completo.

| Postura | Referente | Funciona cuando... | ¿Le sirve a PBS hoy? |
|---|---|---|---|
| **Editorial/autoridad silenciosa** ("no vendo, informo") | McKinsey | Ya tienes el capital de marca — la ausencia de venta es creíble porque nadie duda de ti. | **No todavía.** PBS corre pauta paga y necesita conversión; no puede permitirse cero CTA de venta. |
| **Sistema aspiracional** ("tu crecimiento compone") | Winning by Design | Le hablas a alguien que ya está creciendo y quiere escalar sin romperse. | **Parcial** — útil para el tráfico tibio/cálido (newsletter, referidos), no para el frío de pauta. |
| **Civilizacional/movimiento** ("juntos reinventamos todo") | Accenture | Tu marca ya es tan grande que puede hablar en abstracto sin perder especificidad. | **No.** Requiere capital de marca que PBS no tiene — sonaría vacío. |
| **Problema-primero, sistema como respuesta** | Force Management | Tu comprador ya siente el dolor pero no sabe nombrarlo — tú se lo nombras y le muestras el sistema. | **Sí — es la postura recomendada.** Mismo tamaño de empresa, mismo tipo de comprador (fundador/directivo B2B, no Fortune 500), y PBS ya tiene la tabla de diagnósticos sistémicos escrita en `jorge_philosophy.md` — solo falta subirla a la arquitectura de la web. |

**Recomendación:** postura base = **Force Management** (problema nombrado → sistema como
respuesta), con injertos puntuales de Winning by Design (antítesis "viejo vs. nuevo" en
titulares, CTAs por bloque) para el tráfico ya calificado. Nada de la postura de
McKinsey/Accenture hasta que PBS tenga 3-5 años más de autoridad de marca acumulada.

### 1.2 Cristalizar la promesa central

Los cuatro referentes — y la propia voz de Jorge — convergen en la misma tesis con
distintas palabras:

- WbD: *"systems that deliver predictable, compounding growth"*
- Force Management: *"Skills matter—but systems scale"*
- Jorge (`jorge_voice.md`): *"Las ventas son un proceso, no un suceso"*

**La promesa central de PBS ya existe — solo no está en el hero.** Candidatos de titular,
todos derivados de material que ya existe en `contexto/` (ninguno es invención nueva):

- *"No enseñamos habilidades. Instalamos sistemas."* (molde Force Management, voz Jorge)
- *"Las ventas son un proceso, no un suceso. Rediseñamos el tuyo."*
- *"Facturación predecible. No heroísmo de fundador."*

Regla de uso: máximo **una** construcción "no es X, es Y" por pieza (`jorge_voice.md §7`
ya lo exige) — elegir un candidato, no encadenar los tres.

### 1.3 Nombrar bien al villano

Ningún referente de peso culpa al individuo. El villano siempre es un comportamiento o un
vehículo roto:

- WbD: *"feature dumps"*, *"reflex discounts"*, *"reactive firefighting"*
- Force Management: la falta de sistema, nunca el vendedor
- PBS ya tiene esto redactado, mejor que ninguno de los cuatro referentes: la tabla de
  `jorge_philosophy.md` ("el vendedor no cierra" → *"no hay metodología alineada al
  proceso de compra"*) — **es el activo de villano-sistémico más específico de los cinco
  bancos que hemos visto.** Solo falta que deje de vivir enterrada en un archivo interno.

### 1.4 Recursos retóricos a instalar

| Recurso | Ejemplo visto | Aplicación a PBS |
|---|---|---|
| Antítesis en titulares | *"Skills matter—but systems scale"* | *"El talento importa. El sistema escala."* |
| CTA en primera persona / imperativo específico por bloque | *"Reveal My Growth Gaps"*, *"Explore our Solutions"* | Bajo "Prospección con IA": *"Ver cómo prospectamos con IA"*; bajo "Sistema de contratación": *"Entender por qué 1 de cada 4 falla"* |
| Contenido etiquetado por formato + tema | McKinsey (formato: CASO/REPORTE/ARTÍCULO) + Force Mgmt (tema: Scaling Sales/Sales Messaging) | Research Hub de PBS con doble eje: formato (Caso/Reporte/Benchmark) × tema (Forecast/Prospección/Contratación/Comisiones) |
| Caso = métrica + cita + cargo real | Force Management (19% reducción ciclo + cita CRO) | Estudio de caso PBS: SROI/Sales Velocity + cita del fundador + cargo — pendiente del caso ancla |
| Pregunta abierta en el formulario final | *"What would you like to discuss?"* | Reemplazar dropdown genérico por *"¿Qué te está costando más ahora mismo?"* |

### 1.5 Qué NO copiar (errores de escala)

- **No eliminar el CTA de venta del home** (McKinsey/Accenture pueden; PBS no).
- **No dejar el hero sin ICP** — McKinsey/Accenture funcionan sin nombrar audiencia
  porque la marca precede a la oferta; PBS necesita "fundador B2B, +$1M, LATAM" explícito.
- **No inflar métricas para sonar "market share"** como Accenture/WbD si no hay dato
  sourced — el candado #1 de `contexto/README.md` prohíbe inventar cifras, y ya
  encontramos una violación activa en la web actual (el "97% de recomendación" sin
  fuente) que hay que corregir, no repetir con otro número.

---

## Parte 2 — UX / Arquitectura de información

### 2.1 Navegación por problema, no por catálogo

Hallazgo central de Force Management: su primera categoría de nav es **"Problems We
Solve"**, no "Servicios". PBS tiene el insumo perfecto para esto y no lo está usando: la
tabla completa de diagnósticos sistémicos de `jorge_philosophy.md`.

**Nav recomendado (reemplaza al propuesto en la v1 de la estrategia, más afilado):**

```
Problemas que Resolvemos   Metodología (Los 6 Pilares)   Casos de Estudio   Research Hub   Sobre PBS   [Agendar Diagnóstico →]
```

"Problemas que Resolvemos" se abre en submenú con los síntomas tal cual los dice el
cliente (`jorge_icp.md`, sección "frases del avatar"): *"Si yo no vendo, no pasa nada"* ·
*"Un mes bien, tres meses mal"* · *"Contraté vendedores y ninguno funcionó"* · *"Ya
compré el CRM y no cambió nada"* — cada uno linkea a su diagnóstico sistémico
correspondiente y de ahí al pilar que lo resuelve.

### 2.2 Home — estructura de bloques consolidada

Fusiona lo mejor de los cuatro referentes con lo que ya proponía la v1:

1. **Hero** — titular por antítesis (1.2) + ICP explícito en la sub-línea + **un** CTA
   primario ("Agendar Diagnóstico Comercial"). Visual: panel de métricas reales, no foto
   de aula.
2. **¿Te suena familiar?** — 3-4 síntomas del avatar (verbatim de `jorge_icp.md`) → cada
   uno linkea a su fila de la tabla de diagnósticos sistémicos.
3. **A System to Drive Predictable Revenue** (molde Force Management) — 3 columnas: Los 6
   Pilares agrupados en 3 macro-etapas (Diagnóstico → Instalación del sistema →
   Supervisión/AI), cada columna con su micro-CTA temático.
4. **Resultados que hablan solos** (molde Force Management) — 3 tarjetas métrica + cita +
   cargo real. Mientras no haya caso ancla con nombre, usar las citas ya existentes en la
   web actual (Hugo Trejo, Ana Santos, Robert Ferrer — sí tienen cargo real) reformateadas
   a esta estructura, marcando que faltan el nombre de empresa e industria.
5. **Prueba institucional** — alianza Harvard + prensa + muro de logos, en el registro
   sobrio de Accenture/Japón (tarjeta, no logo suelto de footer).
6. **Por qué no somos...** — tabla de diferenciación competitiva de `jorge_decisions.md`
   (curso / agencia / consultor / formación tradicional vs. PBS).
7. **Research Hub** — 4-6 piezas etiquetadas por formato × tema (1.4).
8. **CTA final** — formulario corto con pregunta abierta (1.4), sin precio, sin catálogo.

### 2.3 Jerarquía de CTAs — resolviendo la aparente contradicción

El candado de FAP es "un CTA único por pieza" — pero eso aplica a **piezas del funnel de
captación** (landing, email, ad), no a una home institucional. Los cuatro referentes usan
CTAs jerarquizados, no únicos:

- McKinsey: "Subscribe" (dominante) vs. "Sign In" (discreto)
- WbD: "See Latest Insights" (leer) junto a "Help Me Grow" (hablar) — dos intenciones, sin competir
- Force Management: 1 CTA primario ("Book a Time to Connect") + micro-CTAs temáticos por bloque

**Regla para PBS:** en la home, **"Agendar Diagnóstico"** es el único CTA de *alto
compromiso* y debe dominar visualmente (color sólido, repetido en hero + cierre). Los
micro-CTAs de cada bloque de contenido ("Ver los 6 Pilares", "Leer el caso de X") son de
*bajo compromiso* y visualmente secundarios (texto/outline). Esto no viola el candado —
lo especifica: un solo CTA de venta, cuantos micro-CTAs de exploración hagan falta.

### 2.4 Formulario de calificación final

Reemplazar el link directo a calendario por un formulario corto (nombre, empresa, email +
**una pregunta abierta**: *"¿Qué te está costando más resolver ahora mismo?"*) antes de
mostrar el calendario — da contexto real al equipo comercial antes de la llamada y filtra
mejor que un dropdown de opciones genéricas.

---

## Parte 3 — Dirección de diseño visual (sin wireframes)

- **Paleta y tipografía:** abandonar el registro "curso vibrante" actual (colores muy
  saturados, tono infoproducto) por uno más cercano a Force Management/McKinsey —
  sobrio, con un acento fuerte reservado solo para CTAs y cifras clave, no para decorar.
- **Motivo visual único y repetido:** elegir uno y sostenerlo en todo el sitio — ej.
  tarjetas de "resultado" (métrica + cita) con el mismo formato en home, casos de estudio
  y research hub. Los cuatro referentes repiten su propio molde de tarjeta sin variarlo.
- **Prueba visual, no solo textual:** dashboard/panel de métricas en el hero (como
  sugeríamos con V4 Company) + muro de logos con jerarquía tipo Accenture/Japón (tarjeta
  con contexto, no logo suelto) + bloque de prensa visible, no en footer.
- **Cero elementos de "escuela"** en el sistema visual: sin barra de progreso de curso,
  sin insignias/certificados como elemento decorativo, sin countdown.

---

## Parte 4 — Checklist accionable

- [ ] Decidir destino del catálogo de 5 cursos (ver precedente de Winning by Design en
      `estrategia-rediseno-web-b2b.md`)
- [ ] Retirar la cifra "97% de recomendación" sin fuente de la web en producción
- [ ] Conseguir el caso ancla con nombre (bloqueante para la Sección 2.2 punto 4)
- [ ] Redactar el nav "Problemas que Resolvemos" a partir de `jorge_philosophy.md`
- [ ] Elegir y fijar UN titular de hero (no probar los tres candidatos a la vez)
- [ ] Definir el molde único de tarjeta (resultado / caso / research) y no variarlo
- [ ] Diseñar el formulario de calificación con pregunta abierta

Este documento y el deck de benchmark son vivos — cada referente nuevo que se audite se
incorpora aquí como fila nueva de las tablas, no como documento aparte.
