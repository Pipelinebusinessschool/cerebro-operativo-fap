# Cerebro Operativo FAP

Sistema de skills propias para producir las piezas de marketing y captación de **FAP**
(high-ticket B2B, sin precio en captación, CTA a llamada de diagnóstico).

El objetivo del repo es tener el "cerebro" en un solo lugar: las reglas de cada pieza,
los candados que no se pueden romper, los ejemplos ganadores reales (swipe) y las piezas
ya producidas y validadas.

> **Principio de fondo:** construir, no comprar. Cuando el hueco es específico de FAP,
> se construye una skill propia en vez de instalar una genérica del banco.

---

## Estructura

```
cerebro-operativo-fap/
├── README.md                  ← este índice
├── HANDOFF.md                 ← documento de continuidad (contexto completo de la sesión)
├── contexto/                  ← FUENTE DE VERDAD: archivos reales de Jorge (ICP, voz, métricas…)
│   ├── README.md              ← índice + decisiones FAP fijadas (ICP, nombre, 6 pilares, candados)
│   ├── jorge_icp.md · jorge_voice.md · jorge_philosophy.md · jorge_process.md
│   ├── jorge_decisions.md · pbs_metrics.md · pbs_indice.md
├── seguimiento/
│   └── seguimiento.md         ← fases 1–3, hallazgo skills-vs-squad, 5 huecos y reglas
├── skills/                    ← las 7 skills del cerebro (fuente de verdad de cada pieza)
│   ├── fap.md
│   ├── fap-lanzamientos.md
│   ├── fap-narrativa.md
│   ├── fap-landings.md
│   ├── fap-whatsapp-api.md
│   ├── fap-whatsapp-grupos.md
│   └── fap-video-ads-meta.md
├── swipe/                     ← banco de ejemplos ganadores reales (inyección de contexto)
│   ├── README.md
│   ├── swipe-correos.md       ← funnel de correo completo (invitación, recordatorio, venta, postventa) con análisis
│   ├── swipe-ads.md           ← 11 ads reales CON métricas (píldoras, video largo, VSL de FAP) + lecciones
│   ├── swipe-landings.md      ← opt-in de registro: landing GANADORA de PGE (anatomía + promesa + ICP)
│   └── swipe-paginas-venta.md ← páginas de pago: workshop $11 (V1/V2) + OTOs $197/$47 (dx FAP)
└── piezas/                    ← piezas ya producidas y validadas
    └── whatsapp-confirmacion-compra.md
```

---

## Las 7 skills del cerebro

| Skill | Rol |
|---|---|
| [`fap`](skills/fap.md) | Fuente de verdad + candados |
| [`fap-lanzamientos`](skills/fap-lanzamientos.md) | Director (2 rutas, piezas, cadencia) |
| [`fap-narrativa`](skills/fap-narrativa.md) | 3 Big Ideas + brief (Agora, McKee, Edwards, Schwartz, PAS/AIDA) |
| [`fap-landings`](skills/fap-landings.md) | Dos modelos (Largo Brunson / Corto Brasil) |
| [`fap-whatsapp-api`](skills/fap-whatsapp-api.md) | 1:1 + cumplimiento API |
| [`fap-whatsapp-grupos`](skills/fap-whatsapp-grupos.md) | Comunidad |
| [`fap-video-ads-meta`](skills/fap-video-ads-meta.md) | Jorge a cámara, optimizado Meta + segmentación |

---

## Estado del proyecto

- **Fase 1 — Revisión del banco de skills genéricas:** cerrada. Ninguna instalada; se rescató craft.
- **Fase 2 — Construcción del cerebro:** 7 skills propias construidas e instaladas.
- **Fase 3 — Validación:** kit completo de prueba (workshop de Contratación) coherente y con candados intactos → el cerebro generaliza.
- **En curso — Swipe de ganadoras:** piloto en `landings`. La brecha del testeo es la falta de ejemplos reales; el swipe la cierra.

Detalle y pendientes abiertos en [`seguimiento/seguimiento.md`](seguimiento/seguimiento.md).

---

## Por qué skills y no squad (hallazgo validado)

Con el **mismo brief**, skills y squad escriben con calidad casi idéntica — pero el squad
**inventó datos falsos** y hasta "verificó" que eran reales. Las skills no, porque la
fuente de verdad `fap` les obliga a **preguntar si el dato no está** en vez de inventarlo.

> La calidad del copy no depende de skill vs. squad, sino de que el **cerebro** (contexto +
> candados + brief) esté completo. El squad vale como **revisión adversarial**, no como motor.

---

## Los 5 huecos — estado actualizado

1. **Voz de Jorge** — ✅ voz escrita cargada (`contexto/jorge_voice.md`: vocabulario obligatorio/
   prohibido + frases signature). Pendiente opcional: cadencia hablada desde transcripciones.
2. **Swipe de ganadores** — ✅ **cerrado.** Correos, ads (con métricas), landings y páginas en
   [`swipe/`](swipe/).
3. **Mapa de objeciones** — 🟡 material ya disponible (`contexto/jorge_philosophy.md`: framework de
   4 pasos + "concede primero"); pendiente ensamblarlo como pieza.
4. **Banco de prueba claim→evidencia** — 🟡 material ya disponible (`contexto/pbs_metrics.md`);
   pendiente estructurarlo por afirmación.
5. **Discrepancia del ICP** — ✅ **resuelto:** ≥$1M/año + ≥2 vendedores (ver `contexto/README.md`).

Fuente de verdad completa en [`contexto/`](contexto/), craft en [`swipe/`](swipe/), continuidad en
[`HANDOFF.md`](HANDOFF.md).

---

## Arquitectura escalable (cuando haya más de un producto)

Separar **CRAFT** (cómo se escribe: landing, ads, emails, narrativa — reutilizable) de
**CONTEXTO** (qué es verdad de cada producto: verdad + voz + swipe + candados). Hoy las
skills FAP fusionan ambos por diseño (un solo producto); con un segundo producto se extrae
el craft a skills genéricas y lo FAP-específico a una cápsula propia — sin reescribir nada.
