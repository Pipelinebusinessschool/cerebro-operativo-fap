# De Escuela a Firma: Estrategia de Rediseño Web B2B — PIPELINE Business School

> Documento estratégico para dirección. Nivel: insights + benchmark + arquitectura conceptual.
> **No incluye** wireframes ni prototipos visuales — eso es la fase siguiente, una vez aprobado el concepto.
>
> **Fuente de verdad usada:** `contexto/` (ICP, decisiones, filosofía, métricas y voz reales de Jorge
> Conde / PBS). Ninguna cifra de este documento es inventada — todas están en `pbs_metrics.md`,
> `jorge_decisions.md` o `jorge_philosophy.md`. Donde falta un dato, se marca `[FALTA]` en vez de
> rellenarlo.
>
> **Pendiente de auditoría:** no fue posible acceder a la web viva (pipelinebusinessschool.com)
> durante la construcción de este documento (bloqueada por firewall del entorno). El diagnóstico de
> "síntomas de escuela" se basa en el patrón estándar de webs de infoproductos B2C (curso → precio →
> testimonio → matrícula) contrastado contra lo que `contexto/` dice que PBS **realmente** es.
> Recomiendo una auditoría de 30 min tomando screenshots de la home actual antes de la reunión, para
> reemplazar el diagnóstico genérico por ejemplos textuales exactos ("dice X, debería decir Y").

---

## 0 · La paradoja de fondo (el insight que sostiene todo el documento)

PBS **no tiene un problema de producto ni de prueba.** Tiene un problema de **traducción**.

En `jorge_decisions.md` ya está escrito, con fecha, que PBS:
- No capacita vendedores individuales — vende transformación de operaciones comerciales completas.
- No es agencia ni curso — es un sistema de 6 pilares con acompañamiento 1:1 de 6 meses.
- Tiene alianza con Harvard Business Publishing Education.
- Opera 100% AI-first (agentes de IA sobre N8N, no PowerPoint de los 2000).
- Sirve exclusivamente a empresas B2B ≥$1M USD/año con equipo comercial — descalifica explícitamente
  al que "vende solo" o busca capacitar a una persona.

Es decir: **la firma de consultoría + aceleradora que dirección quiere proyectar ya existe en el
papel.** El rediseño de la web no es inventar un posicionamiento nuevo — es dejar de esconder el que
ya está decidido detrás de una interfaz que parece Hotmart. Esto cambia el encargo: no es "reinventar
quiénes somos", es "dejar de traicionar en la web lo que ya somos en el contrato".

### Diagnóstico del problema actual

Una web con forma de "catálogo de cursos" limita la venta B2B de alto ticket por cuatro razones
concretas:

1. **Señala el ticket equivocado.** Un comprador que factura +$1M USD/año y evalúa una inversión de
   6 meses con acompañamiento 1:1 espera ver lo que ve al evaluar Deloitte o Simon-Kucher: metodología
   propietaria, casos con cifras, credenciales institucionales. Si ve grid de cursos con precio y
   estrellas, su cerebro lo clasifica como compra de bajo riesgo/bajo compromiso — y sale a buscar
   quien sí hable su idioma (consultoría).
2. **Convierte al comprador equivocado.** El formato "escuela" atrae al que busca aprender una
   habilidad (el vendedor, el individuo) — exactamente el perfil que `jorge_icp.md` **descalifica**
   ("no captura", "no tiene equipo que transformar"). El formato "firma" atrae al fundador/directivo
   que sí es el ICP real.
3. **Contradice la prueba que ya tienen.** +$150M USD en nueva facturación, SROI >5X, alianza Harvard,
   +120 proyectos de re-ingeniería — son credenciales de nivel McKinsey/Deloitte. Puestas en el marco
   visual de una escuela ("nuestros egresados dicen...") se leen como marketing de curso, no como
   prueba de transformación empresarial. La autoridad real queda subutilizada por el envase.
4. **Fuerza a competir en el terreno equivocado.** En el terreno "escuela", PBS compite por precio y
   producción de contenido contra Hotmart/Udemy. En el terreno "firma de arquitectura de ingresos",
   compite por metodología y resultados contra consultoras — terreno donde **el candado de "cero
   descuentos" y el argumento precio-vs-costo** (`jorge_philosophy.md`) finalmente tienen sentido
   visual y no solo verbal.

### Concepto central / posicionamiento

PBS ya tiene, en su propio vocabulario (`jorge_voice.md`), el nombre exacto de lo que Winning by
Design llama "Revenue Architecture": Jorge se refiere a sí mismo como **"arquitecto de ingresos"** y
al área comercial como **"la fábrica de ingresos"**. No hay que importar un concepto — hay que
subir uno que ya existe en su lenguaje a categoría de marca.

> ## **PBS es la firma de Arquitectura de Ingresos B2B de Latinoamérica.**
> **No enseñamos a vender. Rediseñamos cómo tu empresa factura.**

Slogans alternos (mismo concepto, distinto registro):
- *"Sistema. No suceso."* — usa la tesis signature #1 de Jorge tal cual ("las ventas son un proceso,
  no un suceso") como titular de marca.
- *"De ventas heroicas a ingresos predecibles."*
- *"La ingeniería detrás del pipeline predecible en LATAM."*

Categoría a reclamar en la mente del comprador: **Revenue Architecture Firm** (no "escuela", no
"academia", no "capacitadora" — palabras que `jorge_voice.md` ya prohíbe explícitamente en el copy y
que hoy probablemente sigan vivas en el arquitecto de información de la web).

---

## 1 · Matriz de Benchmark Global

| País / Referente | Práctica clave (qué hacen) | Cómo aplicarlo a la web de PBS |
|---|---|---|
| **EE. UU. — Winning by Design** | Convierten su metodología en un framework propietario con nombre y diagrama ("Revenue Architecture", "Bowtie Funnel") que se enseña y se vende como IP, no como curso. | Subir **"Los 6 Pilares"** (ya documentados en `jorge_decisions.md`) al centro de la marca: página propia por pilar, diagrama visual único, nombre registrable ("Sistema PBS de Arquitectura de Ingresos"). Deja de ser "temario" y pasa a ser propiedad intelectual exhibida. |
| **EE. UU. — McKinsey** | Hub editorial (*McKinsey Quarterly*) con research propio y data de industria, sin presión de "compra" en el contenido — la autoridad vende, no el CTA. | Crear un **Research Hub / Revenue Intelligence** que publique los benchmarks reales de PBS (Pipeline Coverage >3.5X, Forecast Accuracy 85%, Sales Velocity +35%) como *reportes de industria*, no como "resultados de mis alumnos". Reposiciona la métrica de prueba social a research propietario. |
| **Alemania — Simon-Kucher & Partners** | Autoridad en estrategia comercial y de precios; páginas por sector/industria; comunicación sobria de "valor, no descuento". | PBS ya tiene el candado "cero descuentos, negociamos modalidad de pago, nunca precio" (`jorge_decisions.md`) — hoy es una regla interna invisible en la web. Hacerla **visible como principio de marca** ("Trabajamos por valor. No negociamos precio.") + páginas de aterrizaje por industria (tecnología, manufactura, servicios profesionales) en vez de una sola home genérica. |
| **Reino Unido — Deloitte UK** | Narrativa de "transformación" con fases visibles (diagnosticar → diseñar → implementar) y casos de cliente como *historias de transformación* cuantificadas. | Reencuadrar FAP como un **"Engagement de Transformación Comercial de 6 meses"** con línea de tiempo visible (mentoría semanal, advisory quincenal, implementación de IA, mastermind semestral — ya está todo definido en `jorge_decisions.md §4`). Los testimonios pasan de frase suelta a *caso de transformación* con antes/después. |
| **Japón — consultoras tech/B2B (confianza institucional)** | Diseño sobrio, poco "hype", con énfasis fuerte en historia institucional, prensa, alianzas y relación de largo plazo por encima de la venta inmediata. | Subir el **bloque de autoridad de Jorge** (`contexto/autoridad.md`, ya escrito verbatim) y la **alianza con Harvard Business Publishing Education** a un lugar mucho más prominente y sobrio — hoy probablemente vive como un logo pequeño al fondo. Muro de logos de empresas donde han quedado directivos formados (Google, Claro, Telmex, SAP, Cisco, Bimbo, Coomeva) cerca del hero, no en el footer. Paleta y tipografía menos "curso vibrante", más "informe institucional". |
| **Brasil — V4 Company** | Narrativa de "motor de crecimiento", visuales tipo dashboard de resultados, energía de aceleradora — el performance como hero visual. | Un **"Revenue Dashboard"** como pieza visual del hero de home: las métricas reales agregadas (SROI >5X, +40% crecimiento en ventas, +52% pipeline) presentadas como panel de resultados de industria, no como testimonios sueltos. Aporta la energía de "motor" sin caer en hype — siempre con la cláusula candado *"promedio de clientes que implementaron"* (`pbs_metrics.md`), nunca como promesa. |

**Patrón transversal en los cinco referentes:** ninguno vende "conocimiento" en su home — todos venden
**método propio + prueba cuantificada + institución detrás**. Es exactamente la fórmula que PBS ya
tiene por escrito y no está mostrando.

---

## 2 · Reestructuración de la Web — Plan de Acción

### QUITAR

- Cualquier vestigio de vocabulario de "escuela": *cursos, clases, matricúlate, estudiantes, alumnos,
  temario, certificado de finalización*. `jorge_voice.md` ya prohíbe el marco "vendemos capacitación"
  — hay que auditar si la web lo respeta.
- Grids tipo catálogo (tarjetas de curso con precio + estrellas + botón "Inscribirme").
- Testimonios sueltos de "alumnos felices" sin empresa, cargo ni cifra — contradice el candado
  "siempre con cifras" y sirve al comprador equivocado (individuo, no fundador).
- Urgencia de lanzamiento tipo infoproducto (countdown, "cupos limitados", "oferta se cierra hoy") si
  existiera — no encaja con el registro "consejero de confianza" ni con el candado de cero descuentos.
- Cualquier mención de precio de FAP en páginas de captación — el candado #3 (`contexto/README.md`)
  ya lo prohíbe; verificar que la web no lo esté violando.
- Doble CTA compitiendo en una misma página (ej. "agenda una llamada" y "compra el curso" a la vez) —
  el candado #4 exige **un solo CTA por pieza**.

### CAMBIAR

- **Tono:** de "motivacional B2C" a **"colega ejecutivo"** — el registro real de Jorge es "didáctico-
  ejecutivo con calidez de colega" (`jorge_voice.md §4`), trato de par ("queridos colegas", "de
  persona de negocios a persona de negocios"), nunca condescendiente ni tipo coach motivacional.
- **Titulares:** de "Aprende a vender más" a **diagnóstico provocador**, usando las tesis signature de
  Jorge tal cual están documentadas:
  - *"El 75% de los equipos comerciales en LATAM opera con 25% de efectividad de contratación."*
  - *"Si las ventas dependen de ti como fundador, no tienes un negocio: tienes un trabajo."*
  - *"Las ventas son un proceso, no un suceso."*
- **CTA:** de "Inscríbete" / "Comprar" a **"Agenda tu Diagnóstico Comercial"** — coherente con el
  proceso real (`jorge_process.md`): el punto de entrada del funnel es una llamada de diagnóstico, no
  una compra directa.
- **Propuesta de valor:** de "aprende técnicas de venta" a **"instalamos los 6 pilares de un sistema
  de ventas B2B escalable, con acompañamiento 1:1 e implementación de IA"** — a nivel de propuesta,
  no de temario.

### RENOVAR (testimonios → Estudios de Caso B2B con ROI)

Estructura fija por caso, usando exclusivamente las categorías de `pbs_metrics.md` (nunca inventar
una cifra fuera de esa lista):

1. **Perfil de empresa** — industria, banda de facturación, tamaño del equipo comercial (sin nombre si
   no hay autorización).
2. **Diagnóstico sistémico** — cuál de los 7 síntomas de `jorge_philosophy.md` presentaba (ej. "las
   ventas dependían 100% del fundador").
3. **Pilares activados** — cuáles de los 6 se implementaron.
4. **Resultado cuantificado** — usando el set oficial: SROI, Sales Velocity, Pipeline Coverage,
   Forecast Accuracy, Sales Growth, etc. — siempre con la cláusula "promedio de clientes que
   implementaron", nunca como garantía.
5. **Cita del ejecutivo** — en primera persona, con cargo.

**Acción pendiente crítica:** `contexto/prueba.md` señala que falta el **caso ancla con nombre** —
sin al menos 1-2 casos reales identificados (empresa + directivo dispuesto a dar cita on-the-record),
esta sección no se puede construir con material real. Es el insumo #1 que hay que pedirle a Jorge
antes de pasar a redacción.

### INCLUIR (secciones nuevas)

- **Los 6 Pilares (Metodología Propietaria)** — página ancla del sitio, un diagrama + una sub-página
  por pilar (Metodología de ventas · Habilitación comercial · Prospección con IA · Supervisión
  comercial · Sistema de comisiones · Sistema de contratación). Es el activo de marca más valioso que
  hoy no existe como página propia.
- **Diagnóstico Interactivo** — un scorecard corto en la home ("¿Qué tan dependiente de ti es tu
  operación de ventas?") que puntúa contra los 6 pilares y termina en CTA a agendar el diagnóstico
  real de 45 min. *Nota: no confundir con el diagnóstico gratuito de la llamada — este es una
  herramienta de calificación en el sitio, previa y separada, y no debe prometer el scorecard/Índice
  de Dependencia del Fundador que `contexto/README.md` reserva para otra etapa.*
- **Research Hub / Revenue Intelligence** — reportes propios con los benchmarks reales (Pipeline
  Coverage, Forecast Accuracy, Sales Velocity) posicionados como investigación de industria LATAM,
  no como folleto de ventas.
- **Página "Por qué no somos [X]"** — convertir la tabla de posicionamiento competitivo de
  `jorge_decisions.md` (curso online / agencia / consultor independiente / formación corporativa
  tradicional) en contenido público. Es diferenciación que ya está escrita y no se está usando.
- **Alianza Harvard + Prensa** — página/sección institucional propia (Forbes Colombia, Business
  Insider México, CIO Times + Harvard Business Publishing Education), tratada como credencial de
  primer nivel, no como logo de footer.
- **Equipo / Autoridad** — bloque de Jorge Conde verbatim desde `contexto/autoridad.md` (no
  reescribir), con foto oficial.

---

## 3 · Arquitectura de Navegación Recomendada

### Menú principal

```
Metodología (Los 6 Pilares)   Industrias   Casos de Estudio   Research Hub   Sobre PBS   [Agendar Diagnóstico →]
```

- "Sobre PBS" agrupa: alianza Harvard, prensa, equipo/autoridad, filosofía ("el problema es el
  sistema, no el vendedor").
- El único CTA del nav es **"Agendar Diagnóstico"** — botón, no link de texto, consistente con el
  candado de CTA único.
- Sin "Precios" en el nav — coherente con el candado "cero precio de FAP en captación".

### Home page — bloques en orden

1. **Hero** — titular de diagnóstico provocador (una de las tesis signature) + sub-línea de posicionamiento
   ("Firma de Arquitectura de Ingresos B2B") + un único CTA ("Agendar Diagnóstico Comercial").
   Visual: dashboard/panel de métricas agregadas, no foto de "aula" ni de "curso".
2. **¿Te suena familiar?** — tabla síntoma → diagnóstico sistémico (directo de `jorge_philosophy.md`),
   formato editorial, sin venta todavía. Aquí es donde el comprador se auto-identifica.
3. **Los 6 Pilares** — framework visual propio, con link a la página de metodología completa.
4. **Prueba institucional** — panel de métricas oficiales (`pbs_metrics.md`) + alianza Harvard + muro
   de logos de empresas donde hay directivos formados por PBS + prensa.
5. **Casos de Estudio** — 2–3 tarjetas de transformación con cifra destacada (pendiente de casos
   ancla reales).
6. **Por qué no somos...** — tabla de diferenciación competitiva (curso / agencia / consultor /
   formación tradicional vs. PBS).
7. **Research Hub (teaser)** — último reporte/benchmark publicado.
8. **CTA final** — repetición del diagnóstico, sin precio, sin urgencia artificial.

---

## 4 · Script para la Reunión del Lunes (resumen ejecutivo, <2 min)

- **Diagnóstico:** Hoy nuestra web se percibe como escuela de ventas B2C, pero nuestro negocio real
  ya es una firma de arquitectura de ingresos B2B — sistema de 6 pilares, acompañamiento 1:1 de 6
  meses, alianza Harvard, +$150M en facturación generada para clientes. La brecha no es de producto:
  es que la web no muestra lo que el contrato ya es, y eso le cuesta credibilidad frente a un
  comprador C-level que factura +$1M al año.
- **Propuesta:** Reposicionar la web bajo un concepto único — *"No enseñamos a vender. Rediseñamos
  cómo tu empresa factura."* — aplicando lo que ya hacen McKinsey, Winning by Design, Simon-Kucher,
  Deloitte UK y V4 Company: metodología propia exhibida como IP, casos con ROI en vez de testimonios,
  research propio, y un solo CTA (diagnóstico, no matrícula). No se toca el producto — se corrige el
  envase.
- **Próximo paso:** Aprobar este concepto y la nueva arquitectura de navegación esta semana. Para
  avanzar a diseño necesitamos dos insumos de Jorge: (1) al menos un caso de cliente real con nombre
  autorizado para el primer Estudio de Caso, y (2) acceso para auditar la web viva con capturas reales
  antes de escribir el copy final.

---

## 5 · Cómo seguimos construyendo este banco de insights

Este documento es v1 — está armado 100% desde `contexto/` (verdad interna) + benchmark internacional
de referencia. Para robustecerlo antes de la reunión, en orden de impacto:

1. **Auditoría de la web viva** — capturas de pantalla (o acceso) de la home y 2-3 páginas clave
   actuales, para reemplazar el diagnóstico genérico de la Sección 0 por comparaciones exactas
   ("hoy dice X, debería decir Y").
2. **Caso ancla con nombre** — pedir a Jorge 1-2 clientes dispuestos a dar cita on-the-record; sin
   esto, la Sección 2 ("Renovar testimonios") no puede pasar de plantilla a contenido real.
3. **Benchmark visual directo** — 3-4 capturas de home de Winning by Design, Simon-Kucher, Deloitte UK
   y V4 Company, anotadas, para que dirección vea el patrón en vez de solo leerlo (útil para la
   reunión, no imprescindible para este documento).
4. **Analytics de la web actual** (si existen) — qué páginas convierten hoy y con qué tráfico, para
   priorizar qué se rediseña primero.
5. **Validación de vocabulario** — pasar el copy actual de la web por la lista de prohibidos de
   `jorge_voice.md §2` para cuantificar cuántas violaciones existen hoy (esto es un dato concreto y
   contundente para la reunión: "la web viola N de nuestras propias reglas de marca").

Cada punto que se resuelva se incorpora como sección nueva o anexo a este mismo archivo — el banco de
insights crece por versión, no por documentos sueltos.
