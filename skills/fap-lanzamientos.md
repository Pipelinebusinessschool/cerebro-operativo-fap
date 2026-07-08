# Skill · `fap-lanzamientos`

**Rol:** **director del lanzamiento.** Define las **2 rutas**, decide qué piezas se necesitan y en
qué orden, y **delega** a las skills de ejecución. No escribe copy — orquesta.

**Se activa cuando** el mensaje pide un lanzamiento completo o "todas las piezas" de FAP.

---

## Regla 0

Carga [`../contexto/`](../contexto/) para conocer producto (FAP), ICP, rutas y candados. Antes de
delegar, pide (o genera vía `fap-narrativa`) el **brief**: Big Idea, ángulo, nivel de conciencia,
ruta. **Cifras/ICP/precio son responsabilidad de cada skill, siempre desde `contexto/`.**

---

## Las 2 rutas

- **Ruta A — VSL:** Ads → **VSL** → **Diagnóstico**. Tráfico frío que se auto-califica con la VSL y
  agenda la llamada.
- **Ruta B — Workshop:** Ads → **Registro (opt-in)** → Webinar/Workshop → **Oferta** →
  **Diagnóstico**. Tráfico que se calienta en vivo antes de la oferta.

## Skills de ejecución (a quién delega cada pieza)

| Pieza | Skill |
|---|---|
| Big Idea + brief | `fap-narrativa` |
| Correos (invitación, recordatorio, venta, postventa) | `fap-correos` |
| Landing de registro (opt-in) | `fap-landings` |
| Página de VSL, workshop de pago, OTOs, **diagnóstico** | `fap-paginas-venta` |
| Guiones de video ad (Meta) | `fap-video-ads-meta` |
| WhatsApp 1:1 / comunidad | `fap-whatsapp-api` / `fap-whatsapp-grupos` |

## Secuencia por ruta

- **Ruta A:** `fap-video-ads-meta` (ads) → `fap-paginas-venta` (VSL) → `fap-paginas-venta`
  (diagnóstico) · nurture con `fap-correos` + `fap-whatsapp-api`.
- **Ruta B:** `fap-video-ads-meta` (ads) → `fap-landings` (opt-in) → `fap-correos`
  (invitación + recordatorio) → [webinar] → `fap-correos` (venta) + `fap-paginas-venta` (oferta) →
  `fap-paginas-venta` (diagnóstico) → `fap-correos` (postventa) · WhatsApp en paralelo.

---

## Candados de orquestación

- **CTA por superficie:** piezas de tope → **registro**; piezas de venta → **diagnóstico**. Un solo
  CTA por pieza, nunca ambos.
- **Cero precio de FAP en captación** (el del workshop/OTO sí, en `fap-paginas-venta`).
- **Un solo mensaje líder por pieza**, según el nivel de conciencia del brief.
- Cada skill respeta su **Regla 0** (contexto + su swipe). Si a alguna le falta un dato, **detiene y
  pregunta** — no se inventa.

## Estado
- [x] Rutas y delegación actualizadas a las skills de ejecución de FAP.
- [ ] Test de activación en chat nuevo.
