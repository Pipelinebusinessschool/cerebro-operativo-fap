# -*- coding: utf-8 -*-
import html
def esc(s): return html.escape(s)

PHASES = {"INVITACIÓN":"#2563EB","RECORDATORIO":"#0891B2","VENTA":"#059669","POSTVENTA":"#7C3AED"}
ADS_COLOR="#EA580C"
PGE="Prospección a Gran Escala con IA · Nov 2025"
SUP="Supervisión Comercial Predictiva con IA"
PP="Pipeline Predecible con IA"
SPG="AI Strategic Pipeline Generation"
FAP="Forecast Accelerator Program (FAP)"

emails = [
# ---------------- INVITACIÓN ----------------
{"phase":"INVITACIÓN","camp":PGE,"lens":"Interrupción de patrón (contrarian)",
 "subject":"🚫 No abras este correo si ya estás prospectando con IA en 2025…","preheader":"Solo para interesados",
 "copy":[
   "Querido/a estratega comercial…",
   "Sé que hoy más que nunca necesitas resultados concretos, no más teoría ni estrategias obsoletas.",
   "Por eso quiero hablarte de algo que sí puede marcar un punto de inflexión en tu operación comercial: PROSPECCIÓN A GRAN ESCALA CON IA. Y es que:",
   "✅ Si te encuentras frustrado de ver a tu equipo invirtiendo tiempo en “curiosos” que no están calificados ni listos para comprar. 😩",
   "✅ Si estás cansado de la falta de predictibilidad. Vender bien un mes, caer en el siguiente.",
   "✅ Si aún dependes de referidos o del azar para cumplir tu cuota de ventas…",
   "Entonces este entrenamiento es para ti.",
   "[ BOTÓN: JUSTO ME DESCRIBISTE, DEBO ASISTIR ]",
   "Está diseñado para quienes sienten que su sistema de ventas está estancado. Te ayudará a: instalar un sistema de prospección B2B con IA que genere un flujo constante de leads calificados; dejar atrás la dependencia de referidos; estructurar tu operación con IA para escalar tu PIPELINE en 2026; construir un ejército de prospección con IA que trabaje para tu cuota 24/7.",
   "[ BOTÓN: ME UNO AL ENTRENAMIENTO, JORGE ]",
 ],
 "angulo":"Exclusión / psicología inversa. El asunto prohíbe abrir, lo que dispara curiosidad por contradicción y filtra por identificación.",
 "recursos":"Asunto con 🚫 que rompe el patrón de bandeja · botón-espejo que verbaliza la reacción del lector (“Justo me describiste”) · 3 síntomas condicionales (PAS).",
 "mecanismo":"El lector se autoselecciona: al reconocerse en los síntomas, hacer clic deja de sentirse como responder a una venta y pasa a sentirse como levantar la mano."},

{"phase":"INVITACIÓN","camp":PGE,"lens":"Miedo específico y nombrado",
 "subject":"🚫 Ignora este correo si el 80% de tus ingresos NO depende de 3 a 5 clientes... 💣","preheader":"En pocos días aprenderás cómo dejar de hacerlo",
 "copy":[
   "Querido/a estratega comercial…",
   "Si hoy el 80% de tus ingresos depende de 5 clientes... y eso te quita el sueño…",
   "Te encuentras angustiado porque si tu cliente #1 te avisa mañana que no renueva, tu operación entera colapsa, viviendo al borde de una crisis permanente. 😰",
   "Entonces nuestro próximo entrenamiento Prospección a Gran Escala con IA es fundamental para tu operación comercial.",
   "[ BOTÓN: JORGE, ESTO ES URGENTE PARA MÍ ]",
   "Está diseñado para directivos que sienten que su empresa está construida sobre una bomba de tiempo. Te ayudará a: instalar Agentes de IA que generan 100+ oportunidades calificadas por mes; construir un PORTFOLIO EXPONENCIAL donde ningún cliente representa más del 10% de tus ingresos; crear un ejército digital que trabaja 24/7 mientras duermes tranquilo.",
   "Regístrate y obtén el plan de contingencia que convierte tu bomba de tiempo en un motor de crecimiento predecible. 🛡️📈",
   "[ BOTÓN: NECESITO DIVERSIFICAR MI PIPELINE, JORGE ]",
 ],
 "angulo":"Miedo de supervivencia: la concentración de cartera. No habla de “vender más”, sino de no colapsar.",
 "recursos":"Cifra concreta en el asunto (80% / 3–5 clientes) · escena del peor caso (“si tu cliente #1 no renueva mañana”) · metáfora “bomba de tiempo → motor de crecimiento” · botones emocionales.",
 "mecanismo":"Ataca un dolor real que el directivo reconoce en su propia empresa. Al ser un riesgo, no una aspiración, la urgencia es genuina sin inflar la promesa."},

{"phase":"INVITACIÓN","camp":PGE,"lens":"Storytelling en segunda persona",
 "subject":"📊 ¿Puedes predecir cuánto vas a vender en marzo 2026?","preheader":"",
 "copy":[
   "Estratega comercial. 👋 Déjame preguntarte algo...",
   "¿Alguna vez te ha pasado que el CEO te llama el lunes por la mañana y te pregunta: “¿Cuánto vamos a cerrar este trimestre?”",
   "Y tú empiezas a hacer cuentas mentales... revisas tu CRM... miras las oportunidades que “deberían” cerrarse... y terminas respondiendo con un “bueno... creemos que unos... más o menos...”",
   "🤯 Ya sabes lo que viene después. Esa mirada. Esa incómoda pausa. Esa pérdida de credibilidad.",
   "Y lo peor es que llevas meses operando así: ❌ Sin poder proyectar cuánto vas a facturar en 2026. ❌ Con un forecast que cambia cada semana. ❌ Rezando para que “algo grande se cierre” antes de fin de mes.",
   "Mira, yo también viví exactamente eso. Hasta que entendí que no puede haber facturación predecible si no hay generación predecible de leads.",
   "Es matemática simple. Si no controlas cuánto PIPELINE nuevo entra cada semana, no puedes proyectar cuánto vas a cerrar en 3, 6 o 12 meses.",
   "Por eso creamos Prospección a Gran Escala con IA. No es teoría. Es un sistema que te permite: ✅ Saber EXACTAMENTE cuánto PIPELINE entra cada semana. ✅ Proyectar tus ingresos de Q1 2026 desde noviembre 2025. ✅ Responder con CONFIANZA la próxima vez que te pregunten “¿cuánto vamos a cerrar?”",
   "Porque la predictibilidad no es mágica. Es sistema. Y el sistema empieza con la generación de leads.",
   "[ BOTÓN: SÍ, QUIERO PREDICTIBILIDAD → ]",
   "Nos vemos en el entrenamiento. Jorge Conde — CEO, PIPELINE Business School",
   "PD: La próxima vez que el CEO te pregunte por el forecast, imagina poder responder con números concretos.",
 ],
 "angulo":"Historia-escena: dramatiza el dolor (la llamada del CEO) en vez de listarlo. El lector se ve dentro de la escena.",
 "recursos":"Narrativa en 2ª persona · diálogo interno · “yo también viví eso” (autoridad por experiencia) · tesis memorizable (“la predictibilidad no es magia, es sistema”) · PD que revive la escena.",
 "mecanismo":"La emoción precede al argumento: primero siente la vergüenza de no saber responder, luego se le ofrece la salida. El molde de storytelling más reutilizable del lanzamiento."},

{"phase":"INVITACIÓN","camp":SUP,"lens":"Checklist de soluciones fallidas",
 "subject":None,"note":"Invitación a masterclass · asunto no registrado en la fuente (PDF)","preheader":"",
 "copy":[
   "Directivo Comercial, ¿cuántas de estas “soluciones” has intentado para recuperar el control de tus números?",
   "◻️ Implementar un CRM más costoso esperando tener inteligencia comercial.",
   "◻️ Construir dashboards hiper-detallados en Power-BI, que solo muestran lo que ya pasó.",
   "◻️ Reuniones de forecast semanales y presión comercial diaria.",
   "◻️ Microgestionar personalmente a cada vendedor para que cierren.",
   "◻️ Acompañar a tus vendedores a cada reunión (y volverte el cuello de botella).",
   "◻️ Pagar consultorías que terminan en un PDF que nadie usa.",
   "Si has intentado al menos una, ya te diste cuenta de algo: sigues operando a ciegas.",
   "Por eso diseñamos esta MASTERCLASS exclusiva para Directivos, Fundadores y CEOs: SUPERVISIÓN COMERCIAL PREDICTIVA CON IA. En 90 minutos te mostramos cómo instalar tu Modelo de Supervisión Comercial acelerado por IA que: predice tu cash flow · audita cada paso de tu operación comercial · detecta caídas de ventas 2 meses antes de que ocurran · agrega una capa de inteligencia comercial a tu liderazgo.",
   "📅 Martes, 2 de junio · 🕐 7:00 p.m. 🇨🇴🇪🇨🇵🇪 | 6:00 p.m. 🇲🇽 | 8:00 p.m. 🇺🇸🇻🇪🇨🇱",
   "[ BOTÓN: QUIERO MI LUGAR EN LA MASTERCLASS ]",
   "Es momento de dejar de ser el “vendedor más caro” de tu nómina y empezar a dirigir con un sistema que trabaje para ti. Nos vemos en la sesión.",
 ],
 "angulo":"Checklist de soluciones fallidas: nombra todo lo que el directivo ya intentó y lo declara insuficiente (“sigues operando a ciegas”).",
 "recursos":"Checkbox ◻️ que el lector marca mentalmente · panorama de alternativas (CRM, BI, consultorías…) · reencuadre de identidad (“vendedor más caro” → “dirigir con un sistema”) · promesa contraintuitiva (“detecta caídas 2 meses antes”).",
 "mecanismo":"Construye acuerdo antes de proponer nada: al reconocer sus intentos fallidos, el lector concluye por sí mismo que necesita algo distinto. Reposiciona toda alternativa como insuficiente."},

{"phase":"INVITACIÓN","camp":PP,"lens":"Presión macro / timing",
 "subject":None,"note":"Invitación (Bases de Datos, v1) · asunto no registrado en la fuente (PDF)","preheader":"",
 "copy":[
   "🚨 El año arrancó con las CUOTAS DE VENTAS más altas de la historia. 🚨",
   "Y con el mismo mercado saturado, los mismos presupuestos congelados y la misma competencia peleando por precio. Esa combinación no se resuelve con más perseguimiento comercial ni con más presión al equipo.",
   "✅ Se resuelve con un sistema diferente.",
   "En este momento estás a tiempo de reaccionar, escalar tu PIPELINE y cerrar el año con un forecast que el board no esperaba ver. 🥇",
   "Eso es lo que vamos a construir en nuestro próximo entrenamiento comercial avanzado PIPELINE PREDECIBLE CON IA. En tres noches consecutivas construiremos el sistema de prospección con IA que directivos comerciales en Latinoamérica están usando para llenar su PIPELINE en 2026, sin importar que la economía esté contraída o que vendas un producto commodity.",
   "🗓️ Martes 21, Miércoles 22 y Jueves 23 de abril · Formato 100% en vivo — 3 noches consecutivas.",
   "[ BOTÓN: REGÍSTRATE AHORA ]",
   "Los cupos son limitados. Aparta tu lugar y gana el juego de las ventas con el sistema de prospección con IA que hace tu PIPELINE predecible y escalable.",
   "Jorge Conde · CEO · PIPELINE Business School",
 ],
 "angulo":"Presión macro / timing: abre por el contexto de mercado (cuotas más altas de la historia), no por el “yo”.",
 "recursos":"Apertura por contexto adverso (mercado saturado, presupuestos congelados, guerra de precios) · reencuadre “no con más presión, sino con un sistema diferente” · prueba social regional · escasez de cupos · firma institucional.",
 "mecanismo":"Le habla al calendario del directivo (arranque de año, cuotas) y externaliza el problema al mercado: lo vuelve urgente por contexto, no por presión de venta."},

{"phase":"INVITACIÓN","camp":PP,"lens":"PAS estándar (el caballo de batalla)",
 "subject":None,"note":"Invitación (Bases de Datos, v4) · asunto no registrado en la fuente (PDF)","preheader":"",
 "copy":[
   "Sé que hoy más que nunca necesitas resultados concretos. ❌ No más teoría ni estrategias obsoletas.",
   "Por eso quiero hablarte de algo que SÍ puede marcar un punto de inflexión: PIPELINE PREDECIBLE CON IA. Y es que:",
   "✅ Si te frustra ver a tu equipo invirtiendo tiempo en “curiosos” que no están calificados. 😩",
   "✅ Si estás cansado de la falta de predictibilidad. Vender bien un mes, caer en el siguiente.",
   "✅ Si aún dependes de referidos o del azar para cumplir tu cuota…",
   "Entonces este ENTRENAMIENTO COMERCIAL es para ti.",
   "[ BOTÓN: JUSTO ME DESCRIBISTE, DEBO ASISTIR ]",
   "Diseñado para quienes sienten que su sistema de ventas está estancado. Te ayudará a: dejar atrás la dependencia de referidos y crear un PIPELINE escalable y predecible; estructurar tu operación con IA para escalar tu PIPELINE en 2026; construir un ejército de prospección con IA que trabaje para tu cuota 24/7.",
   "🗓️ Martes 21, Miércoles 22 y Jueves 23 de abril · 🔴 Formato 100% en vivo — 3 noches consecutivas.",
   "[ BOTÓN: ME UNO AL ENTRENAMIENTO, JORGE ]",
   "Jorge Conde · CEO · PIPELINE Business School",
 ],
 "angulo":"Problema-Agitación-Solución clásico: la versión más replicable del correo de invitación.",
 "recursos":"Reencuadre “no más teoría” · 3 síntomas condicionales · el mismo botón-espejo “Justo me describiste” que en otros lanzamientos (módulo reciclado y probado) · datos del evento · firma con cargo.",
 "mecanismo":"Su valor está en la fiabilidad, no en la sorpresa: síntomas + autoselección funcionan lanzamiento tras lanzamiento. Por eso este bloque se reutiliza casi idéntico."},

# ---------------- RECORDATORIO ----------------
{"phase":"RECORDATORIO","camp":PGE,"lens":"Cercanía + foco (una hora antes)",
 "subject":"⚠️ 1 Hora para escalar tu PIPELINE con IA ⚠️","preheader":"Comenzamos en 60 minutos… ¿Estás listo?",
 "copy":[
   "🤩 ¡Te confieso que estoy realmente emocionado y un poco nervioso por nuestro encuentro!",
   "🫡 Ahora mismo estamos finalizando pruebas de sonido, video, etc. para que puedas recibir lo mejor de este entrenamiento.",
   "👉 Aquí tienes los detalles del evento en directo:",
   "🗓 Evento: Prospección a gran escala con Inteligencia Artificial · 🕖 6:00 pm 🇲🇽 · 7:00 pm 🇨🇴🇵🇪🇪🇨 · 8:00 pm 🇺🇸🇻🇪 · 9:00 pm 🇨🇱 · 💸 Costo: Gratis",
   "📲 Apaga el móvil, pausa las notificaciones y avisa en casa que no estarás disponible un buen rato, porque necesitarás tener toda tu atención acá durante 90 minutos.",
   "¡Te esperamos!",
 ],
 "angulo":"Anticipación y compromiso: no vende, prepara. Busca asistencia en vivo maximizando el foco del registrado.",
 "recursos":"Vulnerabilidad cercana (“emocionado y un poco nervioso”) · detrás de cámaras · instrucción concreta de foco (“apaga el móvil… 90 minutos”) · recordatorio de gratuidad.",
 "mecanismo":"Al pedir un compromiso pequeño y concreto (bloquear 90 minutos, silenciar) sube la probabilidad de asistir en vivo, que es donde ocurre la conversión."},

{"phase":"RECORDATORIO","camp":PGE,"lens":"Prueba social + escasez de replay",
 "subject":"🔐 Día #1: Repetición desbloqueada 🔐","preheader":"Disponible solo por 24 horas.",
 "copy":[
   "Estratega comercial… Lo que pasó en el día 1 de esta formación es increíble. ⬇️",
   "+14.000 estrategas de ventas B2B se registraron al primer día de Prospección a gran escala con IA. 🤩",
   "En esta sesión revelamos cómo construir un Sistema de Omnipresencia Comercial “AI FIRST” que evangelice el mercado con tu propuesta de valor y genere de 3 a 5 nuevas oportunidades por vendedor a la semana.",
   "🗣️ Si te la perdiste, no te preocupes, hemos grabado la clase #1 para que puedas ponerte al día:",
   "[ BOTÓN: QUIERO VER LA REPETICIÓN DEL DÍA 1 ]",
   "(Esta grabación desaparecerá en 24 horas)",
   "Y recuerda que esto continuará mañana en el día #2.",
 ],
 "angulo":"Prueba social masiva + escasez temporal: “muchos ya están aquí” y “la puerta se cierra en 24h”.",
 "recursos":"Cifra de prueba social (+14.000 registrados) · promesa de valor de la sesión · vencimiento explícito del replay (24h) · gancho al día siguiente.",
 "mecanismo":"El replay con caducidad entrena al lead a actuar rápido cada día; ese reflejo de urgencia diaria es el que luego se activa en la fase de venta."},

{"phase":"RECORDATORIO","camp":PGE,"lens":"El puente recordatorio → venta (apertura de oferta)",
 "subject":"Inscripciones abiertas 💯💪🏻","preheader":"STRATEGIC PIPELINE GENERATION",
 "copy":[
   "Estratega comercial…",
   "¡Las inscripciones a la certificación STRATEGIC PIPELINE GENERATION con bonos exclusivos están oficialmente ABIERTAS! 😱⚠️",
   "[ BOTÓN: QUIERO COMPLETAR MI INSCRIPCIÓN ]",
   "Esto no es un curso de ventas. Es un programa intensivo de desarrollo de habilidades, basado en 5 pilares que garantizan superar tu cuota de 2026:",
   "1️⃣ Un Bootcamp intensivo para desarrollar las 7 habilidades indispensables para escalar tu PIPELINE con IA.",
   "2️⃣ Implementación acelerada en SPRINTS de 7 días, con mentoría semanal y el único Mastermind de escalamiento de PIPELINE con IA de LATAM.",
   "3️⃣ Acceso a +100 herramientas de generación de PIPELINE listas para implementar.",
   "4️⃣ Sistemas de prospección digital pre-construidos y completamente operativos.",
   "5️⃣ Acceso a +25 Agentes de IA que multiplicarán tu productividad comercial.",
   "Además, si te inscribes HOY aseguras el bono exclusivo: 🎁 Workshop “Escala tu Capital Visual”. ¡Pero debe ser RÁPIDO! Antes de que este bono desaparezca.",
   "P.D.: Si tienes dudas, contacta a mi equipo de soporte directamente vía WhatsApp.",
 ],
 "angulo":"Revelación de la oferta en el momento de máxima temperatura (durante la clase más esperada), formalizada por correo.",
 "recursos":"Reencuadre “esto no es un curso, es un programa” · stack de 5 pilares numerado · bono con urgencia (“desaparece hoy”) · PD que abre canal humano.",
 "mecanismo":"La oferta se siembra en vivo y el correo la ancla. El bono que caduca el mismo día crea la primera micro-decisión de compra sin fricción."},

# ---------------- VENTA ----------------
{"phase":"VENTA","camp":PGE,"lens":"Future pacing (proyección del estado deseado)",
 "subject":"Hablemos de tu primer trimestre comercial en 2026. 📆🔮","preheader":"",
 "copy":[
   "Estratega Comercial 👋🏼 Quiero hacer un ejercicio contigo, pero para que funcione, vamos a suponer que ya es febrero de 2026…",
   "✔️ Has dejado de perseguir (rogar) por primeras reuniones, y ahora son los clientes quienes te buscan a ti. Te perciben como la solución a sus problemas de negocio.",
   "✔️ Cuentas con una estructura de ventas que influencia los procesos de compra en los que decides participar.",
   "✔️ Tus clientes te perciben como una autoridad, como un verdadero consejero de confianza. No eres uno más entre la multitud, eres su estratega.",
   "Este es el futuro que puedes construir junto a Strategic PIPELINE Generation.",
   "[ BOTÓN: ESE ES EL FUTURO QUE DESEO EN MI EMPRESA ]",
   "No se trata de sueños inalcanzables; se trata de aplicar un sistema probado que ya funciona en empresas como la tuya. En este programa no aprenderás teorías abstractas: saldrás con un PIPELINE real de +7 cifras y las habilidades para replicarlo una y otra vez.",
   "PD: Cada día que pasa sin un sistema sólido de ventas es una oportunidad perdida. No dejes que este 2026 te sorprenda con los mismos desafíos del pasado. ❌🚨",
 ],
 "angulo":"Future pacing: hace vivir el resultado antes de comprarlo (“supongamos que ya es febrero de 2026”).",
 "recursos":"Salto temporal al estado deseado · inversión del rol (“ahora son los clientes quienes te buscan”) · identidad aspiracional (“consejero de confianza / su estratega”) · PD de costo de oportunidad.",
 "mecanismo":"Proyectar el futuro deseado en presente genera deseo emocional y hace del programa el puente lógico entre el hoy y ese febrero."},

{"phase":"VENTA","camp":PGE,"lens":"Prueba social + escasez + desglose del “cómo”",
 "subject":"🚨 No creerás lo que acaba de pasar 🚨","preheader":"Y la verdad es que no quiero dejarte fuera.",
 "copy":[
   "Estratega comercial, tengo que contarte algo 👇",
   "El 83% de los cupos de la Certificación Strategic Pipeline Generation ya están ocupados.",
   "No te escribo para presionarte. Te escribo porque conozco lo que pasa cuando un estratega deja pasar una oportunidad como esta: otro trimestre más con el mismo PIPELINE estancado, el mismo desgaste.",
   "[ BOTÓN: ASEGURAR MI LUGAR ANTES DE QUE SE AGOTEN ]",
   "¿Por qué tanta demanda? Porque cada semana desbloqueas un Sprint Comercial de Alto Impacto:",
   "✅ Semana 1: Un plan de Forecast a prueba de directivos. ✅ Semana 2: Un mapa de territorios con cuentas prósperas, gracias a IA. ✅ Semana 3: Técnicas de prospección que hoy funcionan en LATAM. ✅ Semana 4: Prospección tradicional sistematizada con IA. ✅ Semanas 5–7: Sistema de prospección digital generando primeras reuniones ultra-calificadas. ✅ Semana 8: Tu propio Agente de Prospección IA. ✅ Semana 9: Convertir PIPELINE a Forecast. ✅ Semana 10: Convertirte en partner clave de tus mejores cuentas.",
   "🚨 Solo quedan los últimos cupos. Las inscripciones cierran mañana. Te veo dentro. — Jorge Conde, PIPELINE Business School",
 ],
 "angulo":"Escasez con cifra (83% ocupado) respaldada por el desglose del programa que justifica la demanda.",
 "recursos":"Cifra de escasez concreta · “no te escribo para presionarte” (baja resistencia) · roadmap semana a semana que hace tangible el valor · cierre con fecha límite.",
 "mecanismo":"La escasez sola sería vacía; al mostrar el “cómo” semana a semana, la demanda se vuelve creíble y el cupo restante, deseable."},

{"phase":"VENTA","camp":PGE,"lens":"Precio sin precio (reencuadre de ROI)",
 "subject":"¿Cuántas ventas necesitas para recuperar tu inversión? 💡","preheader":"Haz la cuenta. Te va a sorprender.",
 "copy":[
   "Estratega Comercial 👋🏼 Hagamos un ejercicio rápido.",
   "Si hoy cierras 1 de cada 10 oportunidades... ¿qué pasaría si con una sola técnica que aprendas en Strategic PIPELINE Generation pasas a cerrar 2 de cada 10?",
   "Así de simple: habrás duplicado (2X) tus ventas.",
   "Y esa es exactamente la promesa de esta certificación: construir un sistema de generación de PIPELINE “AI FIRST” que escale tu FORECAST en los próximos 90 días.",
   "La fría realidad es esta: si pasas de cerrar 1 de cada 10 a cerrar 2 de cada 10, ¿cuántos negocios adicionales representará eso en tu forecast en 2026? Todo lo demás es ganancia.",
   "[ BOTÓN: QUIERO INSCRIBIRME AHORA ]",
   "PD: Estratega, la pregunta no es cuánto cuesta el programa. La pregunta es cuánto te cuesta seguir operando sin sistema.",
 ],
 "angulo":"Manejo de la objeción de precio sin mostrar el precio: lo convierte en un cálculo de retorno que hace el propio lector.",
 "recursos":"Ejercicio de matemática simple (1/10 → 2/10 = 2X) · pregunta que el lector responde solo · PD que reencuadra el costo como costo de inacción.",
 "mecanismo":"Al hacer que el lector calcule su propio retorno, el precio deja de compararse contra cero y pasa a compararse contra lo que gana. Neutraliza la objeción antes de que aparezca."},

{"phase":"VENTA","camp":SPG,"lens":"Escasez horaria + recap de oferta (cierre −6 h)",
 "subject":None,"note":"Correo de venta · cierre (faltan 6 h) · asunto no registrado en la fuente (PDF)","preheader":"",
 "copy":[
   "En menos de 6 HORAS se cierran las inscripciones al programa de aceleración de ventas AI STRATEGIC PIPELINE GENERATION.",
   "Ingresa desde aquí para tomar uno de los últimos cupos >>",
   "Este programa te guiará paso a paso para construir un Sistema de Generación de PIPELINE “AI FIRST” que genere facturación rentable y predecible en los próximos 90 días.",
   "Recuerda, esta oferta exclusiva incluye ⬇️",
   "1️⃣ Entrenamiento comercial enfocado en escalamiento de PIPELINE con IA.",
   "2️⃣ Programa de Harvard Business Education para desarrollar habilidades de negociación y cierre.",
   "3️⃣ Sesiones semanales de implementación para quitar bloqueos y asegurar que avances.",
   "4️⃣ Mastermind One Million PIPELINE.",
 ],
 "angulo":"Escasez horaria + recap del stack de oferta: en el cierre, recuerda el valor y pone reloj.",
 "recursos":"Cuenta regresiva (6 horas) · “uno de los últimos cupos” · stack numerado de la oferta (entrenamiento, Harvard, sesiones, Mastermind).",
 "mecanismo":"En el cierre el correo no convence, recuerda: el stack numerado hace sentir el volumen de lo que se pierde si no se actúa en las próximas horas."},

{"phase":"VENTA","camp":SPG,"lens":"Cierre binario + urgencia real (−2 h)",
 "subject":None,"note":"Correo de venta · cierre (faltan 2 h) · asunto no registrado en la fuente (PDF)","preheader":"",
 "copy":[
   "En 2 horas cierran las inscripciones a AI STRATEGIC PIPELINE GENERATION. Y tienes dos caminos:",
   "❌ Seguir igual: ciclos de venta interminables. Leads de baja calidad. Tu cuota dependiendo de las mismas tres cuentas…",
   "✅ Construir un sistema de escalamiento de PIPELINE con IA: PIPELINE predecible. Agentes IA prospectando por ti. Forecast que no depende de personas, sino de sistemas.",
   "La fría realidad es esta: 2026 es un punto de quiebre. 🔴 Las economías están contraídas. Los mercados, más saturados. Los presupuestos congelados y los conflictos mundiales están acelerando el cambio.",
   "La diferencia está entre quienes tienen un sistema y quienes siguen vendiendo como en 2010.",
   "[ BOTÓN: 👉🏼 SÍ, QUIERO UN SISTEMA QUE ESCALE ]",
   "¿Tienes preguntas? Mi equipo responde ahora: contáctalos aquí >>",
   "Jorge Conde · Chief Executive Officer · PIPELINE Business School",
 ],
 "angulo":"Cierre binario + urgencia real: dos caminos (❌/✅) y una cuenta regresiva de 2 horas.",
 "recursos":"Contraste en dos columnas ❌/✅ con consecuencias concretas · marco macro que externaliza la urgencia (“2026 es un punto de quiebre”) · canal humano de última hora · firma con cargo.",
 "mecanismo":"La urgencia la impone el mercado, no Jorge; y el contraste binario elimina la opción de “lo pienso luego”, que en un cierre equivale a no comprar."},

# ---------------- POSTVENTA ----------------
{"phase":"POSTVENTA","camp":SPG,"lens":"Onboarding del comprador",
 "subject":"Felicitaciones, tu acceso a la certificación ha sido confirmado 🍾","preheader":"",
 "copy":[
   "Estimado(a) estratega comercial… 🤩",
   "Quería aprovechar este momento para darte la bienvenida oficial a la Certificación “Strategic PIPELINE Generation”. 💯🏅 Estamos emocionados de tenerte a bordo.",
   "Ya estamos preparando todo para que comiences a construir un PIPELINE real de más de 7 cifras en menos de 90 días. 💰✅",
   "Pero antes de empezar, aquí los 2 pasos a seguir:",
   "➡️ Paso #1: Agéndate desde ahora para no perderte las sesiones en vivo. Son fundamentales para tu éxito.",
   "➡️ Paso #2: Únete a nuestra comunidad exclusiva de WhatsApp, donde conectarás con otros profesionales y recibirás contenido exclusivo.",
   "[ BOTÓN: UNIRME A LA COMUNIDAD DE WHATSAPP ]",
   "➡️ Línea de soporte para estudiantes: CLIC AQUÍ.",
 ],
 "angulo":"Reducir la fricción del arranque y confirmar la buena decisión (evita el remordimiento de compra).",
 "recursos":"Felicitación + bienvenida · reafirmación de la promesa (+7 cifras / 90 días) · 2 pasos claros y accionables · canal de soporte visible.",
 "mecanismo":"Un onboarding claro convierte la compra en primer avance inmediato; la comunidad y las sesiones en vivo elevan la permanencia y reducen reembolsos."},

{"phase":"POSTVENTA","camp":PGE,"lens":"Downsell a quien no compró (recuperación)",
 "subject":"🚨 Noticia de último momento…","preheader":"",
 "copy":[
   "Mi querido estratega comercial… ¡Qué semana tan increíble fue Prospección A Gran Escala Con IA! 👏💥",
   "En caso de que te hayas perdido alguna parte, quería compartir contigo este video resumen de menos de 15 minutos con los mejores momentos.",
   "🤚 Pero aún hay más… 👀 He decidido lanzar a la venta la grabación 📽️ de estos 4 días potentes, para que tengas el mapa completo para construir tu sistema de prospección AI-First. Además de bonos:",
   "➡️ Acceso a la repetición de los 4 días completos. ➡️ Acceso directo al KIT de ventas (plantillas y recursos): planeación estratégica de cuentas, plan de prospección, guía para liderar una primera reunión, estilos sociales, preguntas impactantes, TOP 10 preguntas para entrevistas de ventas.",
   "[ BOTÓN: ACCEDE A LA REPETICIÓN POR SOLO $67 ]",
   "⏲️ Esta oferta estará disponible hasta mañana viernes a las 11:59 por $67, luego subirá a $97.",
   "Los directivos que más rápido escalan son los que no dependen de la memoria. Tener las grabaciones es como una “biblioteca comercial” a tu alcance.",
 ],
 "angulo":"Downsell: monetiza y recupera al que no compró el programa, con una oferta de bajo riesgo (grabaciones + KIT).",
 "recursos":"Recap emocional del evento · ancla de precio con reloj ($67 hoy → $97 mañana) · KIT como stack de valor tangible · metáfora (“biblioteca comercial”).",
 "mecanismo":"Baja el escalón de compromiso: una micro-conversión de $67 mantiene viva la relación y crea un comprador para el próximo lanzamiento."},

{"phase":"POSTVENTA","camp":PGE,"lens":"Upsell con pregunta incómoda",
 "subject":"Ahora que vas a generar PIPELINE a escala... ¿tienes la estructura comercial para convertirlo?","preheader":"Commercial Structure Builder",
 "copy":[
   "“Buenos vendedores no reparan sistemas de ventas rotos. Sistemas de ventas rotos solo frenan y alejan a buenos vendedores.”",
   "Acabas de adquirir un sistema para generar PIPELINE a escala con IA. Pero déjame hacerte una pregunta incómoda:",
   "¿Tienes un sistema para convertir ese pipeline... o tienes 10 vendedores, cada uno con su propio método inventado?",
   "❌ Juan aprendió a vender en seguros. Andrea en tecnología. Martín trae su método del sector financiero. 10 vendedores, 10 escuelas distintas, 10 métodos imposibles de escalar. Y cuando llega la hora de cerrar, el cliente pide descuento y tu vendedor no sabe justificar el valor.",
   "Con Commercial Structure Builder aprenderás a diseñar un proceso comercial customer-centric, construir tu sistema de habilitación comercial, influir en cada etapa del proceso de compra y crear playbooks para que cada vendedor sepa qué hacer en cada momento.",
   "Antes: $997 USD · HOY: $247 USD (solo hoy).",
   "[ BOTÓN: SÍ, QUIERO SER ARQUITECTO DE ESTRUCTURAS COMERCIALES ESCALABLES ]",
 ],
 "angulo":"Upsell al comprador: abre un problema adyacente que la compra recién hecha deja al descubierto.",
 "recursos":"Cita de apertura que enmarca el dolor · pregunta incómoda · escena del caos (10 métodos distintos) · consecuencia (descuento por no justificar valor) · ancla de precio con urgencia ($997 → $247).",
 "mecanismo":"Justo cuando el cliente resolvió “generar pipeline”, se le muestra el siguiente cuello de botella (“convertirlo”). El deseo de completar el sistema hace natural el segundo sí."},
]

ads = [
{"fmt":"Píldora · video corto","camp":SUP,"tier":"GANADOR","lens":"Callout de identidad — la gran ganadora",
 "metrics":[("Stop Ratio","63.53%"),("Retención","47.47%"),("CTR","3.08%"),("Costo 50%","$0.019")],
 "script":[
   "Tu cargo dice director comercial, pero tu día a día dice que eres el policía de tu operación de ventas. Tú estás detrás de cada vendedor para que prospecte, para que haga seguimiento, para que reporte en el CRM. Y lo único que tienes para dirigir es lo que te cuentan en el comité de forecast, donde te cuentan lo que quieres escuchar, no la realidad.",
   "Un directivo que dirige a ciegas su operación de ventas no sabe cuál es su punto de escala real: qué proceso mejorar, dónde entrenar a su equipo, qué problema resolver primero.",
   "Y si quieres que eso cambie, necesitas instalar un modelo de supervisión comercial predictivo que use IA para detectar caídas de ventas dos meses antes de que impacten tu facturación.",
   "En pocos días inicia la masterclass 'Supervisión comercial con IA', a la que ya te registraste… Da clic aquí abajo y agrega este entrenamiento a tu calendario corporativo. Da clic.",
 ],
 "angulo":"Callout de identidad: contrasta el rol formal con la realidad diaria del directivo (“tu cargo dice X, tu día a día dice Y”).",
 "recursos":"Espejo incómodo en la 1ª frase · metáfora de identidad (“el policía”) · acusación al ritual (comité = “lo que quieres escuchar”) · promesa contraintuitiva (“caídas 2 meses antes”).",
 "mecanismo":"El hook ataca la brecha entre el rol y la realidad en la primera frase: un espejo que obliga a quedarse. Stop del 63.53% y el costo más barato de todo el banco ($0.019) lo confirman."},

{"fmt":"Píldora · video corto","camp":SUP,"tier":"MEJOR CTR","lens":"Autoridad + densidad de valor",
 "metrics":[("Stop Ratio","57.63%"),("Retención","38.95%"),("CTR","3.75%"),("Costo 50%","$0.120")],
 "script":[
   "Voy a comprimir 15 años de ingeniería comercial en 60 segundos. Pon atención: tu comité semanal de ventas no es supervisión, es un ritual donde cada vendedor te cuenta lo que quieres escuchar. Tu CRM no te dice lo que pasa en tu operación, te dice lo que cada vendedor decidió reportar.",
   "Medir la cuota, número de propuestas y número de reuniones no es supervisión, es hacer arqueología comercial: revisar restos de lo que ya pasó. Perseguir a tu equipo los viernes no es liderazgo, es ser el policía más caro de tu operación.",
   "Las operaciones que escalan tienen un sistema de supervisión comercial predictivo que usa agentes de IA para auditar cada paso del proceso. Por eso creamos la masterclass 'Supervisión comercial predictiva con IA'… Da clic y agrega este entrenamiento a tu calendario. Da clic.",
 ],
 "angulo":"Autoridad + densidad de valor: promete comprimir 15 años en 60 segundos.",
 "recursos":"Promesa de densidad (“15 años en 60 seg”) · anáforas de reencuadre (“X no es supervisión, es…”) · frases-sentencia memorizables (“arqueología comercial”, “el policía más caro”).",
 "mecanismo":"La promesa de valor comprimido dispara el CTR más alto del set (3.75%): quien se queda, quiere el clic. Las anáforas hacen el guion citable."},

{"fmt":"Video largo · CPL/ROAS","camp":PGE,"tier":"MÁS VENTAS","lens":"Metáfora de obsolescencia",
 "metrics":[("Ventas","33"),("CPL","$2.77"),("ROAS","2.29"),("ROAS tibio","4.03")],
 "script":[
   "Si eres un gerente comercial B2B y en pleno 2025 tienes un equipo de ventas prospectando con llamadas en frío, eso es como tratar de enviar un mensaje con un telégrafo en plena era de los smartphones.",
   "Dame 4 noches y te voy a mostrar cómo integrar la IA en tu operación de ventas para conseguir un crecimiento exponencial de pipeline en los próximos 90 días.",
   "Mi nombre es Jorge Conde y, según la revista Forbes, soy experto en llenar embudos de ventas B2B. He asesorado a más de 100 compañías y entrenado a más de 40.000 directores de ventas B2B en Latinoamérica; generamos más de 150 millones de dólares en nuevas ventas.",
   "Y hoy quiero invitarte a un entrenamiento comercial avanzado de 4 noches… escala tu pipeline mínimo a 1 millón de dólares en los próximos 90 días. Da clic y regístrate únicamente si quieres crecer tu cartera de clientes rápidamente. Regístrate.",
 ],
 "angulo":"Metáfora de obsolescencia: prospectar en frío hoy = enviar un mensaje con telégrafo en la era del smartphone.",
 "recursos":"Metáfora visual que ridiculiza la práctica actual · “dame 4 noches” (compromiso acotado) · bloque de autoridad (Forbes + 40.000 + $150M) · CTA con filtro.",
 "mecanismo":"La metáfora hace evidente y ridícula la práctica actual del prospecto en una frase. Fue el ad de más ventas (33). Nota el salto de ROAS frío→tibio (1.41 → 4.03)."},

{"fmt":"Video largo · CPL/ROAS","camp":PGE,"tier":"MEJOR CPL","lens":"Reducción del rol a una misión",
 "metrics":[("Ventas","16"),("CPL","$2.07"),("ROAS","2.49"),("ROAS tibio","4.05")],
 "script":[
   "Como director de ventas tienes un solo trabajo: generar facturación predecible. Pero ¿cómo hacerlo cuando tu equipo no cuenta con un sistema de prospección predecible que los mantenga operando a máxima capacidad y conversando con tomadores de decisión?",
   "Dame 4 noches y te voy a mostrar cómo usar la IA para prospectar a gran escala y conseguir que tu equipo deje de depender del mismo pipeline de siempre.",
   "Mi nombre es Jorge Conde, fundador de Pipeline Business School… hemos entrenado a directores que hoy trabajan en Google, Microsoft, Oracle, Sophos, SAP, Fortinet, Cisco, Telmex, Bimbo, Movistar, HubSpot…",
   "Regístrate sin costo únicamente si quieres un sistema de ventas que sí genere facturación predecible. Regístrate.",
 ],
 "angulo":"Reducción del rol a una sola misión (“tienes un solo trabajo: facturación predecible”).",
 "recursos":"Reducción del rol · pregunta que expone el gap · muro de logos (prueba social de marcas) · CTA con filtro.",
 "mecanismo":"El CPL más bajo del set ($2.07). El “un solo trabajo” enfoca al directivo en su responsabilidad #1 y el muro de logos da permiso para confiar."},

{"fmt":"VSL de captación","camp":FAP,"tier":"MEJOR AD · FAP","lens":"Callout de identidad + reencuadre de creencia","highlight":True,
 "metrics":[("Agendas","19"),("Costo/agenda","$64.77"),("CTR","1.33%"),("Rompe scroll","29.43%")],
 "script":[
   "No eres el CEO fundador de tu compañía. En realidad, eres el vendedor más caro que tiene tu empresa. ¿Por qué? Porque cierras los negocios más grandes, rescatas los trimestres de ventas, trabajas más de 70 horas semanales… Tu título dice director general, pero tu realidad grita: vendedor sénior exhausto.",
   "Y lo peor es que lo has normalizado y dices: 'así son las ventas B2B', lo cual es una gran mentira. Las ventas B2B son sistemas y no heroísmos; procesos escalables, no personalidades. Un sistema bien diseñado convierte vendedores toma-pedidos en consultores que venden por valor sin depender de ti.",
   "Mi nombre es Jorge Conde, fundador de Pipeline Business School, y hemos estado en el backstage de más de 100 operaciones comerciales B2B. En el 87% de los casos el problema era idéntico: directivos esclavos de su operación comercial por falta de una estructura de ventas escalable.",
   "Por eso creamos el programa de aceleración de Forecast, donde trabajamos contigo para estructurar todo tu sistema de ventas B2B, de tal forma que genere facturación predecible y elimine la dependencia del directivo para que las ventas sucedan.",
   "Si quieres saber cómo funciona, hemos preparado un video corto… Da clic aquí abajo para verlo únicamente si estás cansado de tener una operación de ventas desgastante e ineficiente. Da clic.",
 ],
 "angulo":"Callout de identidad que niega el autoconcepto (“no eres el CEO… eres el vendedor más caro”) + reencuadre de creencia.",
 "recursos":"Negación del autoconcepto · reencuadre (“'así son las ventas B2B' es una gran mentira”) · antítesis (“sistemas, no heroísmos; procesos, no personalidades”) · dato de autoridad (“87% de los casos”) · CTA a VSL con filtro.",
 "mecanismo":"Rompe scroll casi al 30% y agenda llamadas a $64.77 — muy eficiente para un high-ticket como FAP. Confirma el hallazgo del banco: el callout de identidad es el mecanismo que más rinde."},

{"fmt":"Video largo · CPL/ROAS","camp":SUP,"tier":"APRENDIZAJE","lens":"El mismo ángulo, estirado a video largo, no vendió",
 "metrics":[("Ventas","0"),("ROAS","0.00"),("CPL","$3.45")],
 "script":[
   "Ejemplo (ADS14): “Empresario, si hoy tienes una operación de ventas desgastante, ineficiente, desorganizada y no sabes cómo estructurarla para que venda por valor y no por precio, en los próximos días impartiremos una masterclass avanzada sin costo…”",
   "Tres anuncios de video largo con el ángulo de “supervisión” (ADS13 / ADS10 / ADS14) rindieron 0–1 ventas y CPL alto ($3.4–4.0) — el mismo ángulo que fue la GRAN GANADORA en píldora corta.",
 ],
 "angulo":"Mismo ángulo de “supervisión” de la píldora ganadora, pero en formato de video largo.",
 "recursos":"Estructura larga hook → problema → autoridad, pero el gancho de identidad se diluye al estirarse.",
 "mecanismo":"Lección: el hook de identidad funciona comprimido; estirado a 90 seg pierde fuerza. El formato manda sobre el ángulo. (Ojo: ADS13 tiene ROAS 10.98 pero sobre 1 sola venta — n=1 es ruido, no señal.)"},
]

ADS_LESSONS = [
 "El callout de identidad es el mecanismo #1: gana en la píldora más barata ($0.019) y en la VSL de FAP (el mejor ad). Es el gancho a replicar en FAP.",
 "El formato manda sobre el ángulo: “supervisión” ganó en píldora corta y perdió en video largo. No hay ángulo bueno en abstracto, sino bueno para un formato.",
 "Tibio > frío en ROAS, siempre: el retargeting convirtió 2–3× mejor (ADS25: 4.03 vs 1.41). El frío trae volumen; el tibio, la venta.",
 "El canal cambia el desempeño: una píldora floja en feed fue la mejor en WhatsApp (CTR 4.64%). La misma pieza no rinde igual en todos lados.",
 "Autoridad estandarizada en los ganadores de venta: Forbes + “40.000 entrenados” + muro de logos (Google, Microsoft, Oracle, SAP…) + “$150M en nueva facturación”.",
]

PAGE_COLOR="#4F46E5"
pages = [
{"tcol":"#2563EB","tier":"OPT-IN · gratis","camp":PGE,"lens":"Registro a webinar — fricción mínima",
 "h1":"Cómo estructurar tu sistema de Prospección B2B con IA para lograr un crecimiento exponencial de tu PIPELINE en 2026",
 "anat":["Eyebrow: Entrenamiento EN VIVO","H1 = promesa","Formulario (solo email) + botón en 1ª persona","Prueba social (logos de medios)","Cronograma de 4 clases numeradas","CTA","Antes / Después (tabla)","Bio de Jorge","Footer"],
 "angulo":"Promesa (sistema con IA + resultado + plazo + ventaja) resuelta con una sola decisión: el email.",
 "recursos":"Botón que nombra el deseo (“Quiero escalar mi PIPELINE”) · 4 clases numeradas que hacen tangible el valor gratis · tabla Antes/Después · doble autoridad (medios + Jorge).",
 "mecanismo":"Todo el copy reduce la fricción del único paso (dar el email). No argumenta precio ni oferta: vende el clic de registro. Es la Landing #1, marcada como ganadora."},

{"tcol":"#059669","tier":"VENTA · $11","camp":SUP,"lens":"Tripwire de entrada (versiones V1 y V2)",
 "h1":"Cómo instalar un Sistema de Supervisión Comercial con IA que detecte caídas de ventas 2 meses antes de que impacten la facturación",
 "anat":["Countdown","H1 (mecanismo + resultado + plazo)","CTA $11 + garantía","Prueba social (12.000 directivos)","Modelo bow-tie con métricas","“Para ti si…” (5 dolores)","Tablas de resultados (11.7X · +$553K/año)","Testimonios con nombre","Bio de Jorge + Harvard","Demo del producto (dashboard)","Stack + garantía 7 días","Por qué cuesta solo $11","FAQ"],
 "angulo":"Tripwire: el $11 no busca ganancia, busca convertir un lead en comprador — el primer “sí” con tarjeta, que es el paso más difícil del funnel.",
 "recursos":"Prueba cuantificada (tablas antes/después con % y $) · justificación honesta del precio simbólico · garantía sin riesgo · demo del dashboard. V2 añade escasez (“87% ocupados”) y callout de audiencia.",
 "mecanismo":"Combina autoridad + prueba dura + garantía + precio bajo para bajar al mínimo la barrera del primer pago. Todo lo demás se monetiza en los OTO."},

{"tcol":"#B45309","tier":"OTO · $197 · molde FAP","camp":"Diagnóstico Fábrica de Ingresos","highlight":True,
 "lens":"Upsell 1:1 — el molde del diagnóstico de FAP",
 "h1":"¡ESPERA! ¿Quieres que un Revenue Architect diagnostique TU operación comercial, 1:1?",
 "anat":["Interrupción: “aún NO está completa” + barra 80%","H1 de deseo","Reencuadre: “no es una llamada de ventas, es el diagnóstico…”","Autoridad (+47.000, 120+ operaciones, Harvard)","Demo del Scorecard (6 pilares, Factor Fundador 78%)","Cómo funciona (4 pasos)","Entregables (Scorecard + 1:1 + Plan)","Ancla de precio ($2.000 → $197)","Doble CTA sí / no"],
 "angulo":"Upsell inmediato con reencuadre anti-venta: “no es una llamada de ventas, es un diagnóstico que ningún CRM te dio”.",
 "recursos":"Interrupción + barra de progreso · demo del entregable antes de comprarlo · ancla de precio ($2.000→$197) · honestidad (“sin contadores falsos ni cupos inventados”) · doble CTA con el “no” que reafirma lo que se pierde.",
 "mecanismo":"Es la plantilla DIRECTA de la llamada de diagnóstico de FAP: 6 pilares, Revenue Architect, sesión 1:1, Scorecard, Índice de Dependencia del Fundador y Mapa de Facturación Oculta en USD. Referencia núcleo para la pieza de diagnóstico de FAP."},

{"tcol":"#7C3AED","tier":"OTO · $47","camp":"Pipeline Predecible con IA (grabado)",
 "lens":"Downsell — entrenamiento grabado",
 "h1":"El método para construir un pipeline de +$1M con IA en 60 días",
 "anat":["Interrupción + barra 90%","H1 + “acceso inmediato”","Logos (Google, Microsoft, Oracle…)","El principio (facturación predecible = generación predecible)","“Lo que descubrirás” (8 piezas: 3×3×30, agentes IA, vender al C-Level…)","Stack + ancla ($477 → $47)","Honestidad / escasez real","Doble CTA sí / no"],
 "angulo":"Downsell más barato para quien no tomó el diagnóstico: captura al comprador en otro nivel de compromiso.",
 "recursos":"Barra de progreso · “el principio” como tesis · 8 piezas numeradas · ancla de precio · misma honestidad que el OTO1.",
 "mecanismo":"Segundo upsell/downsell con el mismo patrón de ancla y honestidad. Es el entrenamiento cuya confirmación de compra ya vive en el cerebro (pieza de WhatsApp)."},
]

PATRONES = [
 ("Un ángulo por correo","Cada envío rota un solo gancho —recap, autoridad, futuro, prueba social, tiempo, ROI, escasez— en vez de amontonar varios. Evita fatiga y permite testear qué ángulo mueve más."),
 ("Precio sin argumentar de frente","El número casi nunca se defiende: se reencuadra como ROI (“de 1/10 a 2/10 = 2X”), como costo de inacción (los PD) o con ancla de precio ($997 → $247, $67 → $97)."),
 ("Escaleras de urgencia real","La presión se concentra al final: cupos (83% → 94%) y reloj (6h → 2h → 30 min) en venta; replays que caducan a 24h en el webinar. La urgencia se ancla en las últimas horas, no en todo el lanzamiento."),
 ("Esqueleto de correo PBS","Apelación identitaria (“estratega/directivo comercial”) → síntomas en lista → reencuadre (“no necesitas X, necesitas Y”) → bullets de transformación → doble CTA → firma con cargo, a veces PD que revive el dolor."),
 ("Módulos reciclados","Bloques probados que se reutilizan entre lanzamientos: el botón-espejo “Justo me describiste, debo asistir”, el stack de la oferta, la estructura ❌/✅. Se ven aquí en cuatro campañas distintas."),
 ("Voz de marca consistente","PIPELINE y FORECAST en mayúsculas, “operar a ciegas”, “ejército de prospección”, “AI FIRST”, cierre siempre con Jorge Conde · CEO · PIPELINE Business School."),
]

def card(e, idx):
    color = PHASES[e["phase"]]
    copy_html = "\n".join(f'<p class="line">{esc(l)}</p>' for l in e["copy"])
    if e.get("subject"):
        head = f'<div class="subject">{esc(e["subject"])}</div>'
        if e.get("preheader"):
            head += f'<div class="pre">{esc(e["preheader"])}</div>'
    else:
        head = f'<div class="nosub">{esc(e.get("note","asunto no registrado en la fuente"))}</div>'
    return f"""
    <article class="card">
      <div class="card-top">
        <span class="badge" style="background:{color}">{esc(e['phase'])}</span>
        <span class="num">#{idx:02d}</span>
        <span class="lens">{esc(e['lens'])}</span>
        <span class="camp">{esc(e['camp'])}</span>
      </div>
      {head}
      <div class="email" style="--c:{color}">{copy_html}</div>
      <div class="why">
        <div class="why-row"><span class="k">Ángulo</span><span class="v">{esc(e['angulo'])}</span></div>
        <div class="why-row"><span class="k">Recursos</span><span class="v">{esc(e['recursos'])}</span></div>
        <div class="why-row"><span class="k">Por qué funciona</span><span class="v">{esc(e['mecanismo'])}</span></div>
      </div>
    </article>"""

order = ["INVITACIÓN","RECORDATORIO","VENTA","POSTVENTA"]
phase_desc = {
 "INVITACIÓN":"Captar el registro al entrenamiento gratuito. Cada correo rota el gancho para hablarle al mismo directivo desde un dolor distinto.",
 "RECORDATORIO":"Maximizar la asistencia en vivo —donde ocurre la conversión— y sembrar la oferta en el momento de máxima temperatura.",
 "VENTA":"Retargeting hacia el programa pago: un ángulo por correo y una escalera de urgencia que culmina en el cierre.",
 "POSTVENTA":"El lanzamiento no termina en la venta: onboarding del comprador, downsell al que no compró y upsell al que sí.",
}
idx=0; sections=""
for ph in order:
    body=""
    for e in emails:
        if e["phase"]==ph:
            idx+=1; body+=card(e,idx)
    sections += f"""
    <section class="phase">
      <div class="phase-head" style="--c:{PHASES[ph]}">
        <h2>{esc(ph)}</h2><p>{esc(phase_desc[ph])}</p>
      </div>{body}
    </section>"""
TOTAL=idx
patrones_html = "\n".join(f'<div class="pat"><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for t,d in PATRONES)

TIER_COLOR={"GANADOR":"#059669","MEJOR CTR":"#059669","MÁS VENTAS":"#059669","MEJOR CPL":"#059669",
            "MEJOR AD · FAP":"#B45309","APRENDIZAJE":"#DC2626"}
def adcard(e, idx):
    tcol=TIER_COLOR.get(e["tier"],"#EA580C")
    metrics_html="".join(f'<div class="metric"><span class="mv">{esc(v)}</span><span class="ml">{esc(l)}</span></div>' for l,v in e["metrics"])
    script_html="\n".join(f'<p class="line">{esc(l)}</p>' for l in e["script"])
    hi=" adhi" if e.get("highlight") else ""
    return f"""
    <article class="card adcard{hi}">
      <div class="card-top">
        <span class="badge" style="background:{ADS_COLOR}">ADS</span>
        <span class="num">A{idx:02d}</span>
        <span class="tier" style="background:{tcol}">{esc(e['tier'])}</span>
        <span class="lens">{esc(e['lens'])}</span>
        <span class="camp">{esc(e['camp'])}</span>
      </div>
      <div class="fmt">{esc(e['fmt'])}</div>
      <div class="metrics">{metrics_html}</div>
      <div class="email" style="--c:{ADS_COLOR}">{script_html}</div>
      <div class="why">
        <div class="why-row"><span class="k">Ángulo</span><span class="v">{esc(e['angulo'])}</span></div>
        <div class="why-row"><span class="k">Recursos</span><span class="v">{esc(e['recursos'])}</span></div>
        <div class="why-row"><span class="k">Por qué {'/ qué aprende' if e['tier']=='APRENDIZAJE' else 'funciona'}</span><span class="v">{esc(e['mecanismo'])}</span></div>
      </div>
    </article>"""

adcards="".join(adcard(e,i+1) for i,e in enumerate(ads))
ADS_TOTAL=len(ads)
ads_lessons_html="\n".join(f'<li>{esc(x)}</li>' for x in ADS_LESSONS)
ads_section=f"""
    <section class="phase">
      <div class="phase-head" style="--c:{ADS_COLOR}">
        <h2>ADS · anuncios (con métricas)</h2>
        <p>Anuncios reales en Meta, rankeados por desempeño. A diferencia de los correos, aquí hay
        datos: Stop Ratio y Retención miden el video; CTR, CPL y ROAS miden captación y venta; y en
        la VSL, el costo por agenda. Incluye la VSL de FAP (el mejor ad) y un caso de aprendizaje.</p>
      </div>
      {adcards}
      <div class="databox">
        <h3>Lo que dicen los datos</h3>
        <ul>{ads_lessons_html}</ul>
      </div>
    </section>"""

def pagecard(e, idx):
    anat=" › ".join(e["anat"])
    hi=" adhi" if e.get("highlight") else ""
    return f"""
    <article class="card pagecard{hi}">
      <div class="card-top">
        <span class="badge" style="background:{PAGE_COLOR}">PÁGINA</span>
        <span class="num">P{idx:02d}</span>
        <span class="tier" style="background:{e['tcol']}">{esc(e['tier'])}</span>
        <span class="lens">{esc(e['lens'])}</span>
        <span class="camp">{esc(e['camp'])}</span>
      </div>
      <div class="subject">{esc(e['h1'])}</div>
      <div class="anat"><b>Anatomía de la página</b>{esc(anat)}</div>
      <div class="why">
        <div class="why-row"><span class="k">Ángulo</span><span class="v">{esc(e['angulo'])}</span></div>
        <div class="why-row"><span class="k">Recursos</span><span class="v">{esc(e['recursos'])}</span></div>
        <div class="why-row"><span class="k">Por qué funciona</span><span class="v">{esc(e['mecanismo'])}</span></div>
      </div>
    </article>"""

pagecards="".join(pagecard(e,i+1) for i,e in enumerate(pages))
PAGES_TOTAL=len(pages)
pages_section=f"""
    <section class="phase">
      <div class="phase-head" style="--c:{PAGE_COLOR}">
        <h2>LANDINGS Y PÁGINAS</h2>
        <p>Del opt-in gratuito al funnel de pago. PBS asciende al prospecto por precio: registro
        gratis → workshop $11 (tripwire) → diagnóstico $197 → entrenamiento $47. Las páginas no
        traen métricas por pieza; son las marcadas como ganadoras. El diagnóstico $197 es el molde
        directo de la llamada de diagnóstico de FAP.</p>
      </div>
      {pagecards}
    </section>"""

HTML = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><style>
@page {{ size:A4; margin:16mm 15mm 18mm 15mm; }}
*{{box-sizing:border-box}} html{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{font-family:-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:#0F172A;margin:0;font-size:10.5px;line-height:1.5}}
h1,h2,h3{{margin:0}}
.cover{{height:262mm;display:flex;flex-direction:column;justify-content:space-between;page-break-after:always;padding:6mm 2mm}}
.cover .brandbar{{font-size:11px;letter-spacing:.28em;color:#64748B;font-weight:700;text-transform:uppercase}}
.cover .mid h1{{font-size:40px;line-height:1.05;letter-spacing:-.02em;margin-bottom:14px}}
.cover .mid .accent{{color:#059669}}
.cover .mid p.lead{{font-size:14px;color:#334155;max-width:150mm;line-height:1.6}}
.cover .rule{{height:4px;width:64px;background:#059669;margin:22px 0;border-radius:2px}}
.cover .meta{{font-size:11px;color:#475569}} .cover .meta b{{color:#0F172A}}
.tag-row{{display:flex;gap:8px;margin-top:16px;flex-wrap:wrap}}
.tag{{font-size:9.5px;font-weight:700;padding:5px 10px;border-radius:999px;color:#fff;letter-spacing:.04em}}
.intro{{page-break-after:always}}
.intro h2{{font-size:20px;letter-spacing:-.01em;margin-bottom:6px}}
.intro .sub{{color:#64748B;font-size:11px;margin-bottom:18px}}
.grid2{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:6px}}
.box{{border:1px solid #E2E8F0;border-radius:10px;padding:13px 15px;background:#F8FAFC}}
.box h3{{font-size:11.5px;text-transform:uppercase;letter-spacing:.06em;color:#0F172A;margin-bottom:6px}}
.box p,.box li{{font-size:10px;color:#334155}} .box ul{{margin:0;padding-left:16px}} .box li{{margin-bottom:3px}}
.phase{{page-break-before:always}}
.phase-head{{border-left:5px solid var(--c);padding:2px 0 2px 12px;margin:0 0 12px}}
.phase-head h2{{font-size:19px;letter-spacing:.02em;color:var(--c)}}
.phase-head p{{font-size:10.5px;color:#475569;margin-top:3px;max-width:165mm}}
.card{{border:1px solid #E5E9F0;border-radius:12px;padding:14px 16px 12px;margin-bottom:13px;page-break-inside:avoid;box-shadow:0 1px 2px rgba(15,23,42,.04)}}
.card-top{{display:flex;align-items:center;gap:8px;margin-bottom:8px;flex-wrap:wrap}}
.badge{{color:#fff;font-size:8px;font-weight:800;letter-spacing:.09em;padding:3px 8px;border-radius:5px}}
.num{{font-size:12px;font-weight:800;color:#94A3B8}}
.lens{{font-size:10.5px;font-weight:700;color:#0F172A}}
.camp{{margin-left:auto;font-size:8px;font-weight:700;color:#64748B;background:#F1F5F9;border:1px solid #E2E8F0;padding:3px 8px;border-radius:999px}}
.subject{{font-size:13.5px;font-weight:800;letter-spacing:-.01em;margin:2px 0;color:#0F172A}}
.pre{{font-size:10px;color:#64748B;font-style:italic;margin-bottom:8px}}
.nosub{{font-size:9.5px;color:#94A3B8;font-style:italic;margin:2px 0 6px}}
.email{{border-left:3px solid var(--c);background:#FBFCFE;border-radius:0 8px 8px 0;padding:9px 13px;margin:6px 0 10px}}
.email .line{{margin:0 0 6px;font-size:10px;color:#1E293B;line-height:1.55}} .email .line:last-child{{margin-bottom:0}}
.why{{border-top:1px dashed #DDE3EC;padding-top:8px}}
.why-row{{display:flex;gap:10px;margin-bottom:5px}} .why-row:last-child{{margin-bottom:0}}
.why .k{{flex:0 0 92px;font-size:8.5px;font-weight:800;text-transform:uppercase;letter-spacing:.05em;color:#059669;padding-top:1px}}
.why .v{{flex:1;font-size:9.7px;color:#334155;line-height:1.5}}
.tier{{color:#fff;font-size:8px;font-weight:800;letter-spacing:.06em;padding:3px 8px;border-radius:5px}}
.fmt{{font-size:9px;font-weight:700;color:#EA580C;text-transform:uppercase;letter-spacing:.05em;margin:1px 0 6px}}
.adcard.adhi{{border:1.5px solid #B45309;background:#FFFBEB;box-shadow:0 2px 6px rgba(180,83,9,.10)}}
.metrics{{display:flex;gap:7px;margin:2px 0 8px;flex-wrap:wrap}}
.metric{{flex:1;min-width:70px;border:1px solid #E2E8F0;border-radius:8px;padding:6px 8px;text-align:center;background:#F8FAFC}}
.metric .mv{{display:block;font-size:14px;font-weight:800;color:#0F172A;letter-spacing:-.02em}}
.metric .ml{{display:block;font-size:7.5px;font-weight:700;text-transform:uppercase;letter-spacing:.05em;color:#64748B;margin-top:1px}}
.databox{{border:1px solid #FED7AA;border-left:4px solid #EA580C;background:#FFF7ED;border-radius:10px;padding:12px 16px;margin-top:4px;page-break-inside:avoid}}
.databox h3{{font-size:12.5px;margin-bottom:6px;color:#9A3412}}
.databox ul{{margin:0;padding-left:16px}} .databox li{{font-size:9.7px;color:#7C2D12;margin-bottom:4px;line-height:1.5}}
.anat{{font-size:9.3px;color:#334155;background:#F8FAFC;border:1px solid #E2E8F0;border-radius:8px;padding:8px 12px;margin:6px 0 10px;line-height:1.75}}
.anat b{{color:#4F46E5;text-transform:uppercase;font-size:8px;letter-spacing:.06em;display:block;margin-bottom:3px}}
.patrones{{page-break-before:always}}
.patrones h2{{font-size:20px;margin-bottom:4px}} .patrones .sub{{color:#64748B;font-size:11px;margin-bottom:16px}}
.pat{{border:1px solid #E2E8F0;border-left:4px solid #059669;border-radius:9px;padding:11px 14px;margin-bottom:9px;page-break-inside:avoid}}
.pat h3{{font-size:12px;margin-bottom:3px;color:#0F172A}} .pat p{{font-size:10px;color:#334155}}
.foot{{margin-top:20px;font-size:9px;color:#94A3B8;border-top:1px solid #E2E8F0;padding-top:8px}}
</style></head><body>

<div class="cover">
  <div class="brandbar">PIPELINE Business School · Selección de casos de éxito</div>
  <div class="mid">
    <h1>Casos de éxito en copy<br><span class="accent">correos y anuncios</span></h1>
    <div class="rule"></div>
    <p class="lead">Una selección curada de las piezas con mejor desempeño de los lanzamientos de
    PBS: el <b>funnel de correo</b> completo y los <b>anuncios de Meta con métricas reales</b>. De
    cada pieza: el <b>copy real</b>, el <b>ángulo</b>, los <b>recursos</b> de persuasión y <b>por
    qué funcionó</b>.</p>
    <div class="tag-row">
      <span class="tag" style="background:#2563EB">INVITACIÓN</span>
      <span class="tag" style="background:#0891B2">RECORDATORIO</span>
      <span class="tag" style="background:#059669">VENTA</span>
      <span class="tag" style="background:#7C3AED">POSTVENTA</span>
      <span class="tag" style="background:#EA580C">ADS</span>
      <span class="tag" style="background:#4F46E5">PÁGINAS</span>
    </div>
  </div>
  <div class="meta">
    Preparado para <b>Jorge Conde</b> — CEO, PIPELINE Business School<br>
    {TOTAL} correos + {ADS_TOTAL} anuncios + {PAGES_TOTAL} páginas · Fuentes: Prospección a Gran Escala con IA,
    Pipeline Predecible con IA, Supervisión Comercial Predictiva con IA, AI Strategic Pipeline
    Generation y la VSL del Forecast Accelerator Program (FAP)
  </div>
</div>

<div class="intro">
  <h2>Cómo leer este documento</h2>
  <div class="sub">Qué contiene, cómo está organizado y con qué criterio se eligieron los correos.</div>
  <div class="grid2">
    <div class="box"><h3>Qué es</h3>
      <p>Una muestra de los correos <b>ganadores seleccionados</b> del funnel de correo de PBS
      (varios lanzamientos), presentados para revisión. No es un lanzamiento completo: es la
      curaduría de las piezas que mejor enseñan un mecanismo de persuasión.</p></div>
    <div class="box"><h3>Cómo se organiza</h3>
      <p>Por las <b>4 fases del funnel de correo</b> + una sección de <b>anuncios</b>:</p>
      <ul><li><b>Invitación</b> — registro al entrenamiento/masterclass.</li>
      <li><b>Recordatorio</b> — asistencia en vivo + apertura de la oferta.</li>
      <li><b>Venta</b> — retargeting al programa pago.</li>
      <li><b>Postventa</b> — confirmación, downsell y upsell.</li>
      <li><b>Ads</b> — anuncios de Meta con métricas reales de desempeño.</li>
      <li><b>Landings y páginas</b> — del opt-in al funnel de pago (workshop + OTOs).</li></ul></div>
    <div class="box"><h3>Qué trae cada ficha</h3>
      <ul><li><b>Copy verbatim</b> — el texto real (enlaces y UTMs abreviados).</li>
      <li><b>Ángulo</b> — el gancho psicológico dominante.</li>
      <li><b>Recursos</b> — los dispositivos de copy concretos.</li>
      <li><b>Por qué funciona</b> — la lectura de por qué convierte.</li></ul>
      <p style="margin-top:5px">La etiqueta de la derecha indica la <b>campaña</b> de origen.</p></div>
    <div class="box"><h3>Criterio de selección</h3>
      <p>Se priorizó que <b>cada correo enseñe un mecanismo distinto</b> (interrupción de patrón,
      miedo específico, storytelling, checklist, prueba social, ROI, cierre binario, upsell…) por
      encima de repetir el mismo recurso. Así la muestra cubre todo el repertorio.</p></div>
  </div>
  <p style="font-size:9.5px;color:#94A3B8;margin-top:16px;">Nota: los <b>correos</b> no tienen
  métricas de envío — su “por qué funciona” es análisis de craft sobre piezas ya validadas. Los
  <b>anuncios</b> sí traen métricas reales de Meta (Stop Ratio, CTR, CPL, ROAS, costo por agenda),
  y ahí el desempeño está medido, no inferido. En algunos correos provenientes de PDF no se
  registró la línea de asunto en la fuente; se indica en la ficha.</p>
</div>

{sections}
{ads_section}
{pages_section}

<div class="patrones">
  <h2>El patrón detrás de todos</h2>
  <div class="sub">Lo que se repite en los correos ganadores — el playbook de PBS en una página.</div>
  {patrones_html}
  <div class="foot">PIPELINE Business School · Selección de casos de éxito · Documento de referencia interna.</div>
</div>
</body></html>"""

p="/tmp/claude-0/-home-user-cerebro-operativo-fap/b00aa6ba-713d-55d5-8104-31b7374f93c1/scratchpad/casos.html"
open(p,"w",encoding="utf-8").write(HTML)
print("HTML escrito:",len(HTML),"chars ·",TOTAL,"correos")
