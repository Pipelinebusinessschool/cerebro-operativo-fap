# De Escuela a Firma: Estrategia de Rediseño Web B2B — PIPELINE Business School

> Documento estratégico para dirección. Nivel: insights + benchmark + arquitectura conceptual.
> **No incluye** wireframes ni prototipos visuales — eso es la fase siguiente, una vez aprobado el concepto.
>
> **Fuente de verdad usada:** `contexto/` (ICP, decisiones, filosofía, métricas y voz reales de Jorge
> Conde / PBS). Ninguna cifra de este documento es inventada — todas están en `pbs_metrics.md`,
> `jorge_decisions.md` o `jorge_philosophy.md`. Donde falta un dato, se marca `[FALTA]` en vez de
> rellenarlo.
>
> **Auditoría de la web viva:** hecha sobre el HTML real de la home actual (pipelinebusinessschool.com)
> el 2026-08-03. Todas las citas de la Sección 0 son texto **verbatim** extraído de esa página — no
> son suposiciones sobre "cómo suelen ser" las webs de curso.

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

### Evidencia exacta — lo que dice la web hoy

| Elemento | Texto/dato real encontrado en la home | Por qué es un problema |
|---|---|---|
| Frase de apertura (H4 sobre el H1 del hero) | *"SOMOS LA PRIMERA ESCUELA DE NEGOCIOS especializada en ESCALAMIENTO DE PIPELINE"* | La primera frase que lee cualquier visitante es "escuela de negocios". Es literalmente la categoría que dirección quiere dejar atrás, puesta en el lugar de más peso semántico de toda la página. |
| Misión declarada | *"Nuestra misión es erradicar la pobreza de las ventas B2B"* | Registro de coach motivacional / infoproducto, no el registro "didáctico-ejecutivo con calidez de colega" que define `jorge_voice.md §4`. |
| Botón de acceso en el header | **"INGRESO"** (portal de estudiante) | Señal estructural de plataforma de cursos (tipo Hotmart/Teachable), no de firma de consultoría — ninguna consultora (Deloitte, Simon-Kucher) tiene un botón de "login de alumno" en su header. |
| Menú "Entrenamientos" | 5 productos individuales: *Escala tu PIPELINE (SPG), Vendiendo al C-Level (SCL), Planeación de FORECAST (FOR), Gerencia Comercial (SOM), Plan de Comisiones (IQ)* | El menú principal completo está organizado como **catálogo de cursos**, no como metodología ni como programa insignia (FAP). |
| Sección "Nuestra Oferta **EDUCATIVA**" | 5 tarjetas de curso con precio público: SPG **997 USD** (cohort, cerrado), SCL **97 USD** (pregrabado, "acceso vitalicio"), FOR (precio no visible en el extracto), SOM **1.497 USD** (cohort, cerrado), IQ **97 USD** (pregrabado, "acceso vitalicio") | Precio público + "acceso vitalicio" + "curso pre-grabado" es exactamente el patrón de infoproducto B2C que el rediseño busca eliminar. Estos 5 productos están dirigidos a **"Vendedores B2B, Gerentes Comerciales, VPs de ventas"** — es decir, al individuo — lo opuesto al ICP real (`jorge_icp.md`: fundador/directivo de empresa ≥$1M USD, equipo de ventas). |
| Branding de programa | *"Conviértete en un Estratega de Forecast «RAINMAKER»"* / *"Gerente de Operaciones Comerciales RAINMAKER"* | Vocabulario de curso de ventas genérico ("rainmaker") ausente por completo de `jorge_voice.md` — no es parte de la voz real de Jorge. |
| Bloque de resultados ("Los Resultados de Nuestros Estudiantes hablan por nosotros") | Contadores animados: **40K+** profesionales entrenados en LATAM · **60%+** directores comerciales que subieron su SROI a 5X · **52%+** de "estudiantes" que "escalaron +2X su pipeline" · **40%+** crecimiento promedio de ventas 1er año · **97%** "de nuestros clientes nos recomendarían" | Dos hallazgos accionables: **(a)** los primeros cuatro números sí **calzan** con `pbs_metrics.md` (SROI>5X ≈ 60% "6 de cada 10"; +40% Sales Growth es idéntico; +52% coincide con Pipeline Growth, aunque aquí se reformula como "+2X" lo cual **distorsiona** la cifra original). **(b)** el **97% de recomendación no existe en ningún archivo de `contexto/`** — es una cifra que viola el candado #1 ("nunca inventar cifras… si falta, se pregunta") y debe removerse o sustentarse antes de que dirección la vea en su propia web. |
| Testimonios | Carrusel de 6 personas (Hugo Trejo, Ana Santos, Jessica Vessi, Natalia Castro, Robert Ferrer, Luis Campbell) con cargo real (Sales Operation Manager, Country Manager, CEO LATAM, Managing Director) pero **sin nombre de empresa, industria ni estructura de caso** | Hay más material B2B del que parece a simple vista (cargos reales, cifras individuales como "+750% prospectos en 90 días") — el problema no es la materia prima, es el **formato** (carrusel de frases sueltas en vez de estudio de caso estructurado). Esto es una buena noticia: no hay que empezar de cero en la Sección "RENOVAR". |
| Alianza Harvard | Ya está en la web ("Hemos Asegurado Una Alianza Exclusiva Con Harvard BPE"), pero enmarcada como *"una vez dentro de nuestra Escuela"* | El activo de mayor autoridad institucional que tiene PBS hoy está **subordinado al marco "escuela"** en vez de ser la prueba central de nivel executive-education. |
| Diferenciadores ("Somos diferentes porque") | IA First · Metodología Probada · Enfoque en Habilidades Estratégicas · Mentalidad de Sistemas | Genéricos y no conectados a los 6 Pilares reales ni a la tabla de posicionamiento competitivo de `jorge_decisions.md` (curso vs. agencia vs. consultor vs. PBS) — esa tabla, que es la diferenciación real y ya redactada, no aparece en ningún lugar de la web. |
| **FAP / Forecast Accelerator Program** | **Cero apariciones** en toda la home (verificado por búsqueda de texto) | Este es el hallazgo más importante del documento: **la web actual y el programa que realmente vende PBS hoy (FAP) son dos negocios que no se tocan.** La web vende 5 cursos de catálogo de $97 a $1.497 a vendedores individuales; el funnel real de captación (ads → VSL/webinar → diagnóstico) vive fuera de la web y nunca aterriza en ella. |
| Pie de página | *"© 2024, GLOBAL INFLUENCE LLC"* / Head Office Miami | Menor, pero a revisar: la razón social visible (Global Influence LLC) no coincide con la marca (PIPELINE Business School) — detalle de credibilidad institucional para una auditoría legal/branding aparte. |

**La conclusión que cambia el alcance del proyecto:** esto no es "refrescar el tono de la web
actual". Es decidir qué pasa con **dos negocios que hoy conviven sin conectarse**: el catálogo de 5
cursos abiertos ($97–$1.497, dirigido a individuos) y el programa insignia real, FAP (6 meses, 1:1,
dirigido a empresas ≥$1M). Antes de tocar una sola página hay que resolver con dirección:

- **¿El catálogo de cursos se mantiene?** Si sí, ¿como línea de entrada de bajo ticket bajo una
  sub-marca separada (ej. "PBS Academy"), o se descontinúa la venta abierta y se convierte en
  contenido de nutrición/autoridad (gratuito) que alimenta el Research Hub en vez de competir por
  precio con Hotmart/Udemy?
- **¿FAP se convierte en el único producto visible en la web principal?** Es la recomendación de este
  documento, consistente con `jorge_decisions.md` ("PBS no capacita vendedores individuales").

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

- **La frase "Somos la primera escuela de negocios..."** del hero — es literalmente la categoría que
  se busca abandonar, hoy en la posición de mayor peso de toda la página.
- **El botón "INGRESO"** (portal de estudiante) del header — señal estructural de plataforma de
  cursos; ninguna consultora tiene login de alumno en su nav principal.
- **Las 5 tarjetas de "Oferta Educativa" con precio público** (SPG $997, SCL $97, SOM $1.497, IQ $97,
  FOR) y su vocabulario asociado: *"curso pre-grabado"*, *"acceso vitalicio"*, *"Inscripciones
  Abiertas/Cerradas"*, *"RAINMAKER"*. Antes de rediseñar hay que decidir con dirección si esta línea
  se mantiene bajo otra sub-marca o se descontinúa (ver recomendación arriba).
- **El vocabulario "escuela": *estudiantes, alumnos, escuela de negocios, matricúlate*** — `jorge_voice.md`
  ya prohíbe el marco "vendemos capacitación" y hoy la web lo usa de forma literal y repetida.
- **La cifra "97% de nuestros clientes nos recomendarían"** — no existe en ningún archivo de
  `contexto/`. Es una violación activa del candado #1 ("nunca inventar cifras") que hoy está en
  producción; se retira o se sustenta con fuente antes de cualquier otro cambio.
- **El framing "+2X su PIPELINE"** sobre la cifra real de +52% Pipeline Growth (`pbs_metrics.md`) —
  es una sobre-interpretación de la métrica original; hay que volver al dato tal como está sourced.
- Doble CTA compitiendo en una misma página (ej. "Agendar diagnóstico" y "Acceder al programa ahora"
  a la vez) — el candado #4 exige **un solo CTA por pieza**; hoy la web mezcla CTAs de compra directa
  de curso con lenguaje de "más información".

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

### Menú actual (auditado) vs. propuesto

| Hoy | Propuesto |
|---|---|
| Entrenamientos ▸ Escala tu PIPELINE · Vendiendo al C-Level · Planeación de FORECAST · Gerencia Comercial · Plan de Comisiones | Metodología ▸ Los 6 Pilares |
| Recursos ▸ Frameworks · Podcast | Research Hub |
| Conócenos ▸ Sobre Nosotros · Medios | Sobre PBS ▸ Alianza Harvard · Prensa · Equipo |
| *(no existe)* | Industrias |
| *(no existe)* | Casos de Estudio |
| **INGRESO** (login de alumno) | *(se retira del nav principal; si el catálogo se mantiene, vive en una sub-marca aparte)* |
| **QUIERO ESCALAR MI PIPELINE AHORA** (CTA a cursos) | **Agendar Diagnóstico** (único CTA, botón) |

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

- **Diagnóstico:** Auditamos la web actual línea por línea. Hoy vende 5 cursos abiertos de $97 a
  $1.497 a vendedores individuales, se presenta como *"la primera escuela de negocios"* y tiene un
  login de alumno en el header — y **FAP, nuestro programa real de $1M+ en facturación por cliente,
  no aparece ni una sola vez.** Son dos negocios que hoy no se tocan. De regalo, encontramos una
  cifra en producción ("97% de recomendación") que no existe en ninguno de nuestros archivos de
  verdad — hay que retirarla ya.
- **Propuesta:** Reposicionar la web bajo un concepto único — *"No enseñamos a vender. Rediseñamos
  cómo tu empresa factura."* — aplicando lo que ya hacen McKinsey, Winning by Design, Simon-Kucher,
  Deloitte UK y V4 Company: metodología propia exhibida como IP, casos con ROI en vez de testimonios,
  research propio, y un solo CTA (diagnóstico, no matrícula). El producto no cambia — cambia qué
  negocio decide mostrar la puerta de entrada.
- **Próximo paso:** Decidir esta semana el destino del catálogo de 5 cursos (sub-marca separada o
  descontinuar la venta abierta) y aprobar la nueva arquitectura de navegación. Para pasar a copy
  final necesitamos de Jorge: al menos un caso de cliente real con nombre autorizado para el primer
  Estudio de Caso.

---

## 5 · Cómo seguimos construyendo este banco de insights

Este documento es v1 — está armado 100% desde `contexto/` (verdad interna) + benchmark internacional
de referencia. Para robustecerlo antes de la reunión, en orden de impacto:

1. **✅ Auditoría de la web viva** — hecha (Sección 0). Pendiente: repetir el mismo ejercicio sobre
   2-3 páginas internas (una landing de curso completa, la página "Sobre Nosotros") para confirmar si
   los hallazgos del home se repiten.
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
