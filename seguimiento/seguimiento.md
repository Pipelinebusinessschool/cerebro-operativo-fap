# Seguimiento — Proyecto Cerebro Operativo FAP

## Fase 1 · Revisión del banco de skills genéricas (no instaladas)

Revisamos ~25 skills descargadas del banco (las 15 iniciales + tandas de landings,
WhatsApp y video). **No instalamos ninguna**: eran genéricas B2C/infoproducto de origen
brasileño, con precio y checkout en el esqueleto — chocaban con FAP (high-ticket B2B, sin
precio en captación, CTA a llamada) y varias duplicaban skills propias superiores.

Sí rescatamos el **craft** de algunas y lo metimos en skills propias:
- Estructura de ad pago de la de YouTube.
- Las reglas de WhatsApp de las 081/226.
- El formato escena-por-escena de video.

### Método que quedó probado
1. **Mapear** antes de instalar.
2. **Cribar por descripción** (muere el 90%).
3. **Activación + lift.**
4. **Revoicear.**

> Construir, no comprar, cuando el hueco es específico de FAP.

---

## Fase 2 · Construcción del cerebro (8 skills propias, instaladas)

- `fap` — fuente de verdad + candados
- `fap-lanzamientos` — director (2 rutas, piezas, cadencia)
- `fap-narrativa` — 3 Big Ideas + brief (Agora, McKee, Edwards, Schwartz, PAS/AIDA)
- `fap-landings` — dos modelos (Largo Brunson / Corto Brasil)
- `fap-correos` — secuencias de email (invitación, recordatorios, post-evento, reactivación)
- `fap-whatsapp-api` — 1:1 + cumplimiento API
- `fap-whatsapp-grupos` — comunidad
- `fap-video-ads-meta` — Jorge a cámara, optimizado Meta + segmentación

---

## Fase 3 · Validación

Kit completo de prueba (**workshop gratuito de Contratación**): narrativa + 2 landings +
6 correos + WhatsApp + 2 ads. Coherente y con candados intactos → **el cerebro generaliza.**

---

## Pendientes abiertos

- [x] **Actualizar `fap-lanzamientos`** para nombrar las skills de ejecución nuevas.
      Cerrado: se desplegaron las 2 rutas con sus pasos (A1–A5 / B1–B3), cada uno apuntando
      a `fap-narrativa` / `fap-landings` / `fap-video-ads-meta` / `fap-whatsapp-api` /
      `fap-whatsapp-grupos`. A1/B1 ya no dicen `agora` / `million-dollar-ads`.
- [ ] **Test de activación** de cada skill en chat nuevo (que disparen sin nombrarlas).
- [x] **Consolidación de secuencias en skill propia.** Cerrado: se creó `fap-correos`
      (invitación, recordatorios, post-evento, reactivación de no-shows, nurture) y se cableó
      como paso A4 en `fap-lanzamientos`.
- [ ] **Confirmar duración real de la llamada de diagnóstico** (hoy placeholder).

---

## Frente nuevo · Banco de swipe (ejemplos ganadores reales)

Diagnóstico: las skills tienen las **reglas** de las piezas, pero les faltan los
**ejemplos ganadores reales**. Un modelo con reglas produce algo correcto; con ejemplos
reales produce algo que se parece a lo que funcionó. Esa es la brecha del testeo.

Decisiones tomadas:
- **Formato:** primero se reúne el material crudo en un doc; después se decide cómo
  conectarlo a las skills (incrustado vs. doc de referencia citado). Elegido: **doc citado**
  (la skill carga el archivo del canal).
- **Piloto:** arrancó por **landings**; validado → replicado a **correos**.

Cada ficha del swipe debe traer, además del copy:
1. **Métrica** que logró (CTR, conversión, registros).
2. **Por qué ganó** (el hook, la oferta, el ángulo) — lo más importante.
3. **Qué NO copiar** (red de seguridad contra romper un candado de FAP, p. ej. precio visible).

Estado por canal:
- **Landings** — [`../swipe/swipe-landings.md`](../swipe/swipe-landings.md) *(piloto)*.
- **Correos** — [`../swipe/swipe-correos.md`](../swipe/swipe-correos.md) ✅, cableado a
  `fap-correos`. 11 fichas (A1–A9 invitación + B1–B2 venta) de lanzamientos reales de PBS
  (no-FAP; molde de craft con candado anti-cifras). **Falta:** métricas por correo (Jorge) y los
  tipos confirmación / recordatorio-no-show / postventa.
- **Ads** — [`../swipe/swipe-ads.md`](../swipe/swipe-ads.md) ✅, cableado a `fap-video-ads-meta`.
  6 ads con **métricas reales de Meta** (A01–A06); **A05 es la VSL de FAP** (el mejor ad).
  Hallazgo: el *callout de identidad* es el mecanismo #1. Fuente: PDF "Casos de éxito Copy Funnel PBS".
- **Material del PDF aún sin cargar:** correos de **recordatorio** y **postventa** (extienden
  `swipe-correos`) y **páginas** (opt-in, tripwire $11, diagnóstico $197 = molde del diagnóstico
  de FAP, downsell $47) → posible `swipe-paginas-venta.md`.

### Siguiente paso
> Cerrados: rutas de `fap-lanzamientos`, skill `fap-correos` y su swipe de correos. Siguiente:
> **test de activación** de las 8 skills en un chat nuevo — que disparen solas, sin nombrarlas.
> Y pedir a Jorge las **métricas por correo** para rankear el swipe.
