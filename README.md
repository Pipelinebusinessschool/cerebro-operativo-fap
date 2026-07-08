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
├── seguimiento/
│   └── seguimiento.md         ← fases 1–3, método probado y pendientes abiertos
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
│   └── swipe-landings.md      ← PILOTO: plantilla por ficha (llenar con ganadoras reales)
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
