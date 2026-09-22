# Análisis de las 10 transcripciones de anuncios

*2026-09-22 · Fuente: transcripciones de esta carpeta (Apify + faster-whisper, sin revisar).*
*Muestra: 10 vídeos únicos (FSS 4, CarlosBusch 3, Accrevity 3). Por debajo de 15 → todo lo de aquí es **hipótesis**, no patrón.*
*Sin métricas de rendimiento: la Ads Library no da resultados. "Más reutilizado" = más IDs con el mismo vídeo, que es una señal indirecta de que el anunciante lo sigue pagando, no una prueba de que funcione.*

---

## 0 · Corrección de un dato del brief

- **Dato (Apify):** la única página localizada es "Full Sales System LTDA." (page_id 221505481054641), 80 anuncios activos, casi todos a `mssquiz.fullsalessystem.com`; 1 solo a `fap01.fullsalessystem.com`.
- **Observación:** el brief decía "Full Sales System Inc. — 91 anuncios, landing FAP01, CTA *Aplique para o Diagnóstico Comercial*". Eso **no se reproduce hoy**. Los 4 vídeos analizados venden un producto de ticket bajo ("Master Sales Script" / "script perfeito de vendas") vía quiz, no el embudo de diagnóstico.
- **Consecuencia:** estas 4 transcripciones **no son el embudo de FAP en portugués**. Sirven como swipe de formato, no de posicionamiento high-ticket. El dato "91 anuncios / FAP01" queda como **no verificado / posiblemente desactualizado** hasta tener la URL de la página "Inc.".

---

## 1 · Qué hace cada anunciante

### Full Sales System LTDA. (pt · 76-207 s · copy "Você sabe vender?" → quiz)
- **Dato:** los 4 vídeos terminan con **el mismo bloque de cierre, palabra por palabra** (~35 s): "A gente aqui consegue fazer qualquer vendedor ficar bom, desde que ele queira… script perfeito de vendas… clique saiba mais em algum lugar dessa tela."
- **Dato:** lo que cambia es la apertura: (a) fragmento de una llamada de venta real con números, (b) "Testando meu time de vendas": el fundador pregunta a un vendedor cómo rebatiría una objeción y este lo responde en 2 pasos, (c) caso de resultado narrado (clínica, "177 mil reais em um dia"), (d) roleplay completo de una llamada de cierre.
- **Observación:** es un sistema **modular**: gancho/prueba variable + cola fija. Un bloque de cierre se graba una vez y se reutiliza en decenas de anuncios.
- **Observación:** el ICP es amplio ("se você é empresário"; el caso estrella es una clínica). Es el mismo problema de audiencia no-ICP que tienen los comentarios de Jorge.
- **Observación:** el CTA es un **autodiagnóstico** ("você vai receber um diagnóstico de como tá o seu comercial"), sin fricción: "não vai precisar botar dados".

### CarlosBusch (pt · 30-60 s · copy "3 dias para mudar o resultado da sua empresa. Aplique-se.")
- **Dato:** el CTA del copy es "Aplique-se" / "Aplique para participar e aguarde o contato do nosso time" + "Turmas limitadas".
- **Dato:** tres formatos distintos:
  1. **Arenga a cámara** (30 s): "Olha pra mim. Você tá esperando o quê…? Para de reclamar… não adianta trabalhar mais horas fazendo a mesma coisa."
  2. **Mapa problema → eje** (43 s): "Se você está com problema de atração de leads, trabalha no go-to-market; com problema de conversão, todo o ciclo comercial; com LTV, expansão e experiência."
  3. **Desmontaje de una práctica común con escena dramatizada** (60 s): "Vamos dar um iPad pros dois melhores vendedores… 1 ganha e 99 não ganham. Tu fez o quê? Tu motivou?" + el OTE usado como amenaza → rotación.
- **Dato:** en el copy también aparece "Você não precisa de mais ideias. Precisa de decisões certas" (mecánica de matar la falsa solución, ya registrada).
- **Observación:** el **filtro explícito de R$1M del brief no aparece** en estos 3 vídeos ni en su copy. Puede estar en otros anuncios; con esta muestra no se confirma.

### Accrevity (en · 104-335 s · B2B services)
- **Dato:** el copy lleva el **resultado cuantificado en el titular** ("How Mike added $1.2M sales pipeline with 50+ CEO opportunities"; "$30k new revenue and 3 new opportunities every week").
- **Dato:** el CTA es "DM 'SCALE' **to see if you qualify** to work with us". Es palabra clave con **marco de calificación**, no de regalo.
- **Dato:** 2 de 3 vídeos son testimonios largos con estructura antes → después: "my schedule was wide open… a lead gen firm set one appointment in three months" → "24 booked meetings this week… every call with a C-level owner".
- **Dato:** el tercero es contraintuitivo: "everyone thinks Meta is B2C; in 2026 inboxes are flooded by AI outreach, Meta is where the intent signals are".

---

## 2 · Hipótesis (n=10, sin datos de rendimiento)

1. **H1: la palabra clave convierte distinto según el marco.** Accrevity usa "DM X **to see if you qualify**". Jorge usa "comenta PODCAST" (entrega contenido). El diagnóstico previo ya mostró que el mecanismo de palabra clave funciona pero atrae no-ICP. Enmarcar la palabra clave como **calificación** ("te digo si tu operación califica") en vez de regalo debería filtrar hacia arriba. *No probado; es la prueba más barata que se puede hacer.*
2. **H2: los que aplican el filtro de facturación son high-ticket, los que no, low-ticket.** FSS (ticket bajo, quiz) no filtra y atrae clínicas. CarlosBusch/Accrevity dicen "aplica" / "qualify". Coincide con lo ya observado en la cuenta de Jorge. *Correlación, no causa.*
3. **H3: mostrar el proceso gana a explicarlo.** Los 4 vídeos de FSS abren **demostrando** (una llamada, una objeción rebatida en 2 pasos), no opinando. En el catálogo de Jorge todo es opinión a cámara. *Hipótesis; sin métricas.*

---

## 3 · Mecánicas trasladables a Reels de Jorge (solo cabeza a cámara, sin tomas complejas)

| # | Mecánica | Fuente | Cómo encaja con la fórmula de Jorge | Riesgo |
|---|---|---|---|---|
| M1 | **"Pregúntale hoy a tu vendedor…"**: una objeción concreta y la respuesta correcta en 2 pasos | FSS "Testando meu time" | El sujeto sigue siendo el directivo (él hace la prueba); cierre con absolución: "si no sabe responder, no es su culpa, nadie le dio el proceso" | Deslizarse a enseñar al vendedor. El reel habla **al directivo**. |
| M2 | **Desmontaje de una práctica que el directivo cree buena** (premio al mejor vendedor, meta como amenaza) | CarlosBusch iPad/OTE | Condicional acusatorio + "no es A, es B" | No citar % de rotación sin fuente. CarlosBusch dice "80%" sin respaldo. |
| M3 | **Mapa problema → dónde se arregla** ("si tu problema es X, no es Y, es Z") | CarlosBusch Bluefin | Taxonomía con autodiagnóstico (ya probada por coachcarlosmeza) sobre los 5 dolores del ICP | Solo nombres oficiales de los 6 Pilares; MEDIC no se expone. |
| M4 | **Palabra clave de calificación**: "comenta X y te digo si tu operación califica" + filtro dicho en voz (B2B, ≥2 vendedores, >$500K) | Accrevity "to see if you qualify" | Sustituye PODCAST como CTA de captación | Hace falta que el DM automatizado **califique** y no entregue un PDF. |
| M5 | **Cola fija modular**: un cierre de 15-20 s grabado una vez y reutilizado en muchos anuncios de pago | FSS | Encaja con grabar 30 reels por tanda | En orgánico, repetir la cola idéntica refuerza la "misma apertura sintáctica" ya diagnosticada. **Úsala en ads, no en reels.** |
| M6 | **Resultado cuantificado en el titular/copy** | Accrevity | Solo con cifras verificadas de `contexto/prueba.md` | No inventar. Si no hay cifra verificada, no se usa. |

**Descartado:** la arenga motivacional de CarlosBusch ("para de reclamar") choca con la regla de no hacer motivación vacía. El testimonio largo de Accrevity no encaja con el formato de Jorge solo a cámara.

---

## 4 · ¿Ampliar la muestra?

Disponible: FSS 27 vídeos únicos · CarlosBusch 45 · Accrevity 10. En local cuesta 0 USD en Apify y unos 60 min de CPU.

**Recomendación:** ampliar **CarlosBusch (45) y Accrevity (10)**. Son los dos que usan "aplica" / "qualify", los más cercanos a FAP. Con 13 vídeos entre ambos pasaríamos de hipótesis a conclusión débil. FSS LTDA solo si aparece la página "Inc." con FAP01: su embudo de quiz es de ticket bajo y no sirve de modelo de captación de FAP.
