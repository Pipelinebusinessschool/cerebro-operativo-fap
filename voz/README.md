# Voz — capa de tono y lenguaje real

Cierra la brecha del testeo: las skills tenían las *reglas* de las piezas, pero no el
lenguaje real de los clientes. Esta carpeta inyecta ese lenguaje, extraído de **15 llamadas
de venta reales** (transcripciones verbatim, jun–jul 2026), **anonimizado**.

## Archivos

- [`voz-cliente.md`](voz-cliente.md) — quién es el cliente, cómo nombra su dolor (verbatim),
  su léxico/jerga, tono regional, y do/don't para las skills.
- [`mapa-objeciones.md`](mapa-objeciones.md) — las 8 objeciones recurrentes ordenadas por
  frecuencia (sobre 15 llamadas), con citas textuales.

## Origen y privacidad

- Fuente: carpeta privada de Drive *Transcrips FAP (Llamadas)*. Los transcripts crudos NO
  están aquí (tienen datos de clientes) — solo el destilado anonimizado.
- Pendiente (no cubierto aquí): **voz de Jorge** (lado emisor) — requiere otra fuente
  (webinars/lives/notas de voz), ya que en estas llamadas quien vende suele ser el equipo.

## Cómo conectarlo a las skills

Candidato a `fap-landings`, `fap-video-ads-meta`, `fap-whatsapp-api` y `fap-narrativa`:
citar `voz/voz-cliente.md` para el idioma del prospecto y `voz/mapa-objeciones.md` para
anticipar frenos. Decisión de arquitectura (incrustar vs. citar) igual que con el swipe.
