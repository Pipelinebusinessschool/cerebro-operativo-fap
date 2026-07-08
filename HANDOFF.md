# Handoff — Cerebro de IA para FAP / PBS
*Documento de continuidad para quien retome este trabajo en Claude Code.*
*Generado a partir de una sesión larga de investigación, auditoría y construcción con Jorge Conde (CEO, PIPELINE Business School).*

> **Nota de importación:** este documento se incorporó al repositorio el 2026-07-08 como
> registro de continuidad. Las partes accionables dentro de este repo están destiladas en
> [`seguimiento/seguimiento.md`](seguimiento/seguimiento.md); este archivo conserva el
> contexto completo tal como llegó, sin recortar.

---

## 0 · Qué es este documento y qué hacer con él

Esto NO es el producto MySquads (ese vive en `CONTINUITY.md`, `ARCHITECTURE.md`, etc. — proyecto distinto de Isis Moreira, no lo toques).

Esto es el contexto de un hilo de trabajo separado: **construir el "cerebro de IA" que genera el copy de los lanzamientos de FAP (Forecast Accelerator Program)**, el programa high-ticket de PBS. Todo lo de abajo son hallazgos, decisiones y pendientes reales de esa investigación — no las repitas ni las vuelvas a debatir salvo que el contenido cambie.

**Al abrir esta sesión, lee en este orden:**
1. Este documento completo.
2. `CLAUDE.md` (raíz del proyecto) — protocolo de `@squads`, tabla de routing, contexto PBS corto.
3. La skill `fap/SKILL.md` y su carpeta `references/` (ruta exacta en la sección 3).
4. `training/pbs/*.md` — contexto de voz/ICP/filosofía de PBS que ya existe.

---

## 1 · El objetivo de Jorge (no perder de vista esto)

Jorge quiere: **generar todo el copy de un lanzamiento (landing, correos, ads, WhatsApp) rápido, con la máxima calidad y precisión, sin depender de un copywriter humano** — usando skills de Claude Code, potencialmente empaquetadas en un plugin o aplicación a futuro.

Todo lo que sigue está al servicio de ese objetivo. Cuando dudes entre dos caminos, elige el que acerque más rápido a "un clic → lanzamiento completo, sin datos inventados, en su voz real".

---

## 2 · Conceptos de arquitectura — léelos antes de tocar nada

Esta sección es la más importante para no repetir confusiones ya resueltas en la sesión anterior.

### 2.1 Skill vs. Squad vs. Plugin vs. Workflow

| Concepto | Qué es | Mecanismo de activación | Dónde vive |
|---|---|---|---|
| **Skill** | Archivo de instrucciones que Claude lee y sigue **en la misma conversación** (no crea un "yo" nuevo) | Se auto-activa: Claude compara tu mensaje contra la `description` de la skill | Plugin `anthropic-skills`, carpeta `skills/fap*` |
| **Squad / Agente** (carpeta `/squads/`) | También es un archivo de instrucciones, pero se usa como *system prompt* de un **subagente nuevo** en una ventana de contexto aparte | Manual: `@squads` → tabla de routing en `CLAUDE.md` → herramienta `Agent` | `/squads/06-pen-copywriting/agents/*.md` |
| **Plugin** | El **envase**: empaqueta varias skills + sus archivos de contexto/fuente de verdad en un solo paquete instalable | Se activa cuando cualquiera de las skills que contiene calza con el mensaje | `anthropic-skills` es el plugin actual que contiene las skills `fap-*` |
| **Workflow** | Un guion (script) que orquesta varios subagentes en **paralelo** de forma determinística (fases, no adivinanza) | Se dispara explícitamente (`/workflows` o pidiendo el lanzamiento completo) | No construido aún para FAP — es el siguiente nivel de automatización |

**La confusión más común que ya resolvimos:** todos estos —skills y agentes de squad— son solo texto. Ninguno "hace" nada hasta que algo lo activa. La diferencia real está en el mecanismo de activación y en si comparte tu conversación actual o abre una nueva.

### 2.2 El hallazgo más importante de toda la sesión (la prueba real)

Hicimos una prueba controlada: el mismo brief (misma Big Idea, mismo ángulo, mismo ICP) se le dio a dos caminos —(A) las skills `fap-*` y (B) tres agentes del squad Pen (`07-landing-page-writer`, `10-ad-copywriter`, `09-email-copywriter`) con el contexto de `training/pbs/` cargado a mano— para producir landing + ads + emails, dos veces (tema supervisión comercial, tema contratación comercial).

**Resultado:**
- **La calidad de escritura fue casi idéntica.** El squad escribe tan bien como las skills cuando recibe un brief igual de bueno.
- **Pero el squad, en ambas rondas, inventó datos falsos** de forma independiente: una cifra de "75% de equipos con 25% de efectividad de contratación / 1 de cada 4 vendedores" que **no existe en ninguna fuente real**, además de métricas obsoletas (Set A en vez de Set B) y duraciones inventadas ("90 minutos", "45 min").
- Lo más grave: un agente del squad afirmó en su verificación final que esa cifra **"provenía del contexto PBS cargado"** — es decir, inventó el dato y luego se convenció de que estaba verificado. Eso es lo más peligroso frente a un CEO que decide con cifras.
- **Las skills no cometieron ni un solo error de este tipo**, porque `fap/SKILL.md` tiene la regla explícita: *"si el dato no está en la fuente, PREGUNTA — no lo inventes."*

**Conclusión operativa (no la repitas, aplícala):**
> La calidad del copy no depende de si usas skill o squad — depende de si el **cerebro** (contexto + candados + brief) está completo y bien cableado. Las skills ganan hoy porque **garantizan** la carga de ese cerebro (vía "Regla 0"); el squad depende de que alguien se lo pegue a mano cada vez, y aun así puede alucinar si no tiene la capa de candados.

**Dónde SÍ vale el squad:** como capa de **revisión adversarial** después de que las skills generan el copy (ej. `16-copy-tester`, `12-objection-handler` atacando el resultado ya escrito) — no como motor de producción primario.

### 2.3 El hallazgo del "ruteo roto" en el squad (por si se retoma ese camino)

`CLAUDE.md` rutea "Landing page" directo a `07-landing-page-writer` → `15-editor-and-line-cutter`, **saltándose** al Director del squad (`director.md`), que es el único archivo con contexto PBS embebido en su Agent Prompt. Los especialistas individuales (como el Landing Writer) **no tienen ninguna mención a PBS/FAP** en su archivo — dependen de que el contexto se les inyecte manualmente en el prompt de invocación. Si se decide invertir en el squad como capa de QA, esto hay que arreglarlo primero (rutear por el Director, o forzar la carga de `context-pbs.md` + `training/pbs/*` en cada especialista).

---

## 3 · Estado actual del sistema de skills FAP

### 3.1 Ubicación de archivos (verificar que la ruta siga existiendo)

```
/Users/jorgeconde/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/
  fcc3472d-9d9d-4fe1-bb2c-586091314505/09188b7c-71dc-4a6a-a433-3657ae9724d3/skills/
    fap/
      SKILL.md
      references/
        fap-contexto-fuente.md        ← fuente de verdad (340 líneas): ICP, 6 Pilares, garantías,
                                         métricas, objeciones, vocabulario oficial, discrepancias conocidas
        fap-lenguaje-verbatim.md      ← CONSTRUIDO ESTA SESIÓN (ver 3.3)
    fap-narrativa/       SKILL.md + references/frameworks-narrativa.md
    fap-landings/        SKILL.md + references/modelos-landing.md
    fap-video-ads-meta/  SKILL.md + references/meta-video-ads.md   ← MEJORADO ESTA SESIÓN (ver 3.3)
    fap-whatsapp-api/    SKILL.md + references/patrones-whatsapp.md
    fap-whatsapp-grupos/ SKILL.md + references/patrones-grupos.md
    fap-lanzamientos/    SKILL.md + references/rutas-y-piezas.md   ← orquestador/inventario de piezas
    inv-patrones-lenguaje/ SKILL.md  ← análisis de voz puntual (no persistente), ver 4.1
```

**⚠️ Advertencia técnica real de esta sesión:** en un momento posterior, un archivo de trabajo (un artefacto HTML, no una skill) se perdió por limpieza del scratchpad de sesión. No debería afectar a las skills (viven en la ruta de arriba, no en el scratchpad), pero **verifica al empezar que las 7 skills siguen ahí y que el contenido no se perdió.**

### 3.2 Cómo encajan entre sí (Regla 0)

Cada skill de producción (`fap-narrativa`, `fap-landings`, `fap-video-ads-meta`, `fap-whatsapp-api`, `fap-whatsapp-grupos`) tiene una "Regla 0" que dice: *"carga `fap` (fuente de verdad) antes de escribir."* Eso es lo que garantiza que ninguna pieza invente precio, cifras o cupos. `fap-lanzamientos` es el orquestador: decide qué piezas se necesitan según la ruta (A: Ads→VSL→Diagnóstico, o B: Workshop→Oferta→Diagnóstico) y en qué orden delegarlas.

### 3.3 Lo que SÍ se construyó en esta sesión (no repetir)

1. **`fap/references/fap-lenguaje-verbatim.md`** — banco de ~35 frases textuales reales de prospectos/alumnos (Diego Camacho de Google, Ana Santos de BenQ, testimoniales), organizado en 6 grupos (dolores, deseos, objeciones, comparaciones, transformaciones, disparadores), cada una con su carga emocional. Minado de `transcripts_prospeccion/clase1-4.txt` y `Webinar_Supervision_Comercial_IA_PBS.md`. Conectado en la Regla 0 de `fap/SKILL.md` para headlines/hooks/subjects/aperturas.
   - **Gap conocido de este archivo:** es débil en "dolores/objeciones en tiempo real" porque la fuente son clases grabadas con testimonios post-resultado, no llamadas de venta en vivo con gente dudando. Si aparecen grabaciones de llamadas de diagnóstico reales, son la fuente que más lo enriquecería.

2. **`fap-video-ads-meta/SKILL.md` mejorado** — se le portó el mecanismo "familias de hooks" del Headline Smith del squad: en vez de pedir 3 variantes de gancho sueltas, ahora exige generar **12-15 hooks cubriendo 7 familias** (resultado, problema, curiosidad, especificidad, prueba, autoridad, contrarian), etiquetar cada uno (familia + conciencia + segmento), y **cortar a 4-6 finalistas** por criterio real. Candados de FAP intactos.

### 3.4 Los 5 huecos identificados y AÚN PENDIENTES (prioridad de trabajo)

Esta es la lista de construcción más importante — viene de un audit explícito, en orden de impacto:

| # | Hueco | Qué es | Por qué importa |
|---|---|---|---|
| 1 | **`fap-voz-jorge.md`** (no existe) | Perfil de la voz hablada/escrita real de Jorge (ritmo, muletillas, cadencia) — extraído con la técnica de `inv-patrones-lenguaje` aplicada a las partes donde **Jorge mismo habla** en las transcripciones (el ~90% que se descartó al construir el verbatim del cliente, porque ese es material del CLIENTE, no de Jorge) | Hoy las skills imitan la voz de Jorge solo por descripción (`training/pbs/jorge_voice.md`); con patrones reales sería menos aproximado |
| 2 | **`fap-swipe-ads.md` / `fap-swipe-correos.md`** (no existen) | Los ads y correos que YA le funcionaron a Jorge — pendiente de que él comparta un documento de Word con ese material real | Es la arquitectura ya probada, no solo la voz — el hueco de mayor impacto de todos |
| 3 | **Mapa de objeciones expandido** en `fap-contexto-fuente.md` | Patrón "concede antes de contraatacar" (*"puede que pienses X — es razonable — y esto es lo que es verdad…"*), colocado en el punto donde surge la duda (no en un FAQ al final) | Mecanismo portado del Objection Handler del squad; craft puro, no necesita insumo nuevo de Jorge |
| 4 | **Banco de prueba con emparejamiento claim→evidencia** | Hoy solo hay 1 caso ancla (Bank of America) + una lista de cifras sueltas en `fap-contexto-fuente.md`. Estructurarlo por tipo de prueba (resultado / autoridad / escala) y a qué afirmación específica responde cada una | Evita que la prueba se sienta genérica |
| 5 | **Reconciliar discrepancia del ICP** | `fap-contexto-fuente.md` dice "factura >$500K/año, ≥2 vendedores"; `training/pbs/jorge_icp.md` dice "$1M/año, 3 vendedores". Son dos fuentes de verdad contradictorias | Barato de arreglar (2 min), evita que dos piezas del mismo lanzamiento usen cifras distintas de ICP — **es la victoria rápida más obvia para empezar** |

**Orden recomendado para retomar:** #5 (2 min) → #1 (ya hay material fuente listo en `transcripts_prospeccion/`) → #2 (en cuanto Jorge comparta el Word) → #3 y #4 (craft puro, sin depender de nadie).

### 3.5 Otros mecanismos del squad identificados como valiosos para portar (segunda ola, no urgente)

Un análisis exhaustivo de los 12 agentes de copy del squad Pen (Voice Architect, Message Strategist, Audience Listener, Offer Writer, Headline Smith, Sales Page Writer, CTA Engineer, Objection Handler, Proof Curator, Story Builder, Editor and Line Cutter, Copy Tester) identificó estos mecanismos adicionales, no construidos todavía:

- **Jerarquía de mensaje por etapa de conciencia** (Message Strategist) — qué mensaje lidera cada superficie según el nivel de conciencia del tráfico; regla "un solo mensaje líder por pieza".
- **Sistema de CTA completo** (CTA Engineer) — el CTA no es solo el botón: es *frase antes + botón + confirmación post-clic*, ajustado al nivel de compromiso (opt-in ≠ agendar ≠ comprar).
- **Checklist de presión pre-publicación** (Copy Tester) — 8 puntos de verificación antes de publicar cualquier pieza (acción clara, ajuste a conciencia, voz, objeciones cubiertas, prueba alineada, continuidad, CTA claro, promesa-cumplimiento). Es la capa de QA adversarial que complementa bien al squad.
- **Offer Frame consolidado + panorama de alternativas** (Offer Writer) — nombrar explícitamente contra qué alternativas compite el prospecto (CRM, consultoría, "vendedor estrella", no hacer nada).

No repitas el análisis completo — está resumido arriba con lo esencial.

---

## 4 · Arquitectura escalable a futuro (para cuando haya más de un producto)

Jorge preguntó cómo generalizar esto más allá de FAP (ej. para un futuro "Strategic Pipeline Generation" u otro programa). La respuesta validada:

**Separar CRAFT (cómo se escribe) de CONTEXTO (qué es verdad del producto).**

```
SKILLS DE CRAFT (reutilizables, se escriben una vez)     CÁPSULAS DE CONTEXTO (una por producto)
  landing-builder, video-ad-builder,                       /productos/fap/ → verdad + voz + swipe + candados
  email-sequence, narrativa-engine        ──carga──▶       /productos/[nuevo]/ → su propia verdad
```

Hoy las skills FAP **fusionan** craft y contexto en un solo archivo (por diseño, porque solo hay un producto). Si se agrega un segundo producto, la refactorización correcta es extraer el craft a skills genéricas y mover lo FAP-específico a una carpeta de "cápsula" propia — no reescribir las skills desde cero.

### 4.1 Sobre `inv-patrones-lenguaje`

Es la skill que hace ingeniería inversa de voz a partir de transcripciones — pero es **puntual y no persistente** (no lee archivos del disco, no guarda un perfil, hay que pegarle el material cada vez en el chat). El hueco #1 de la tabla de arriba (`fap-voz-jorge.md`) es exactamente convertir ese análisis puntual en un archivo persistente que las demás skills carguen solas.

---

## 5 · Visión de sistema operativo alrededor de los cerebros (más a futuro, no bloqueante)

Se diseñó conceptualmente (con diagramas en un artefacto — ver sección 6) un "sistema operativo" alrededor del cerebro `fap`, en capas:

1. **Orquestador** — quién da la orden (hoy: Jorge + Claude Code; a futuro: reglas + aprobación).
2. **Memoria compartida** — el estado de cada lead (qué vio, qué respondió, en qué etapa está). **Vive en un CRM/hoja externa (GoHighLevel, Pipedrive o Google Sheets), NO dentro de Claude ni de las skills.** Claude la lee/escribe vía MCP; no la almacena.
3. **Gobierno** — la capa de marca/candados por encima de todos los cerebros (hoy vive dentro de `fap`; a escala de empresa sería una capa transversal).
4. **Retroalimentación** — los resultados (CTR, conversión, respuestas) regresan y ajustan qué produce el cerebro la próxima vez. Importante: **Claude no se reentrena** — "aprende" actualizando el contexto que lee después, no sus pesos. Requiere aprobación humana antes de que un ajuste se vuelva regla permanente.

**5 tipos de loop identificados** (de micro a macro): loop agéntico (interno, ya existe) → loop de auto-crítica (generar→criticar→corregir, usa subagentes, cero dependencias, alto impacto) → loop de nurture (memoria + reglas por lead) → loop de cadencia (rutinas programadas / n8n) → loop de retroalimentación (el más valioso a largo plazo, pero requiere que los anteriores ya generen datos).

**Prioridad si se retoma esto:** el loop de auto-crítica es gratis y de mayor impacto inmediato (ya lo validamos informalmente en la prueba skills-vs-squad — es literalmente lo que faltó para cazar el dato inventado). Los demás dependen de tener memoria real conectada primero.

### 5.1 Dos flujos operativos ya diseñados (con factibilidad evaluada)

**Flujo 1 — Prospección inteligente (100 leads):** extraer e investigar (Apollo + Apify) → generar mensajes hiperpersonalizados (skills) → aprobación humana → enviar (regla: ≤25 correos/día por Gmail propio del usuario; >25/día por lemlist o Smartlead, para no quemar el dominio) → monitorear y registrar en memoria → escalar a llamada por auto-dialer (JustCall/Aircall — requiere conectar). Los primeros 5 pasos son construibles hoy con lo ya conectado; el auto-dialer es lo único que necesita una integración nueva.

**Flujo 2 — Lanzamiento de webinar:** brief (Big Idea + narrativa) → producir todo en paralelo (landing + correos + ads + WhatsApp, ya validado en esta sesión) → aprobación → cargar en GoHighLevel (**GHL no está conectado en este entorno — hay que conectar su MCP y verificar qué permite escribir**) → activar con aprobación por API. El cuello de botella real es GoHighLevel, no la generación de contenido.

### 5.2 Herramientas ya conectadas en el entorno de trabajo (verificar que sigan activas)

Apollo (búsqueda/enriquecimiento de leads, secuencias), Pipedrive (CRM), Calendly, Zoom, Meta Ads, Slack, Canva, Google Sheets/Workspace, Gmail. **No conectados aún:** GoHighLevel, lemlist, JustCall/Aircall, n8n — para el Flujo 1 y 2 completos, estos son los que faltan.

---

## 6 · Otros artefactos visuales producidos en la sesión

Se construyeron varios artefactos HTML (diagramas interactivos) documentando esta arquitectura — útiles como material de referencia/explicación, no como fuente de verdad técnica (esa vive en las skills):

- Mapa de red del cerebro `fap` (qué está construido vs. qué falta, con la tabla de la sección 3.4).
- Vista "Anatomía de un cerebro de IA" — educativa, para alguien sin contexto previo: fuente de verdad conectada a contexto/plataformas/skills/memoria/orquestador, y cómo se arman "procesos" (prospección, newsletter, WhatsApp, lanzamiento, reactivación) combinando esas piezas.
- Red 3D estilo "Jarvis" de dos cerebros (fap + un producto futuro) conectados a integraciones.
- Prototipos de flujo (Flujo 1 y 2 de la sección 5.1) como flujogramas con etiquetas de factibilidad.
- Cuadrante de estrategias de Inbound (volumen vs. calidad del lead) con las 9 estrategias de PBS posicionadas: Fast Lead Funnel, Sales Presentation Funnel, Lead Qualification Funnel (los 3 embudos de conversión de Jorge) + LinkedIn, Newsletter, YouTube, Podcast, Formulario de Facebook, WhatsApp (canales de atracción). Nota: Jorge corrigió que WhatsApp es alto-volumen/muy-baja-calidad, Newsletter es muy-bajo-volumen/alta-calidad, y LinkedIn es de calidad/intención baja — respeta esas correcciones si se retoma ese material.
- Cerebro de IA de Mindvalley a 5 años (ejercicio prospectivo de benchmarking, 14 clusters funcionales / ~100 neuronas, investigado con fuentes reales) — es exploratorio/inspiracional, no aplica directo a PBS salvo como referencia de "a qué escala puede llegar esto".

**Importante:** uno de los archivos de trabajo de estos artefactos se perdió por limpieza de scratchpad de sesión a mitad del trabajo. Si necesitas retomar/editar alguno, probablemente haya que reconstruirlo desde cero citando esta sección — no busques el archivo original, puede que no exista.

---

## 7 · Reglas y feedback de Jorge que hay que respetar siempre

- **Nunca inventar cifras, cupos, garantías ni duración** que no estén en `fap-contexto-fuente.md`. Si falta el dato, preguntar — no asumir. (Esta es LA regla que causó los problemas del squad; no bajar la guardia con las skills tampoco.)
- **Cero precio de FAP en copy de captación**, siempre. El precio del workshop de entrada (Ruta B) sí puede aparecer.
- **CTA único por pieza** — a registro (piezas de tope) o a diagnóstico (piezas de venta), nunca ambos ni links secundarios.
- **Prioridad al Set B de métricas**, no al Set A (desactualizado).
- **Voz de PBS**: diagnóstica, confrontacional, anti-victimización, con cifras — nunca motivacional vacía.
- **Al mejorar el copy propio de Jorge**: cirugía de voz, no reescritura — conservar su narrativa, ángulo y cifras (esto ya estaba guardado en memoria antes de esta sesión, sigue vigente).
- Jorge prefiere respuestas directas con veredicto claro, no exhaustivas listas de opciones sin recomendación — cuando dudes, da tu mejor recomendación primero.

---

## 8 · Primeros pasos sugeridos al retomar

1. Verificar que las 7 skills `fap-*` siguen en su ruta (sección 3.1) y que el contenido no cambió.
2. Cerrar el hueco #5 (reconciliar ICP) — 2 minutos, alto valor simbólico de "ya no hay contradicciones".
3. Si Jorge tiene las transcripciones a mano, construir `fap-voz-jorge.md` (hueco #1) usando la técnica de `inv-patrones-lenguaje` sobre las partes donde Jorge habla (no el cliente).
4. Pedir a Jorge el documento de Word con sus ads/correos ganadores para construir el swipe-file (hueco #2) — es el pendiente de mayor impacto que depende de él, no de trabajo técnico.
5. Los huecos #3 y #4 se pueden hacer en cualquier momento, sin esperar nada de Jorge.
6. No avanzar en el "sistema operativo" (memoria/orquestador/flujos reales) hasta que el cerebro `fap` esté completo — es la secuencia que el propio Jorge validó.
