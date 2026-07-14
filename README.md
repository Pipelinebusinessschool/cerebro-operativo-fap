# Cerebro Operativo FAP

Sistema de skills propias para producir las piezas de marketing y captación de **FAP**
(high-ticket B2B, sin precio en captación, CTA a llamada de diagnóstico).

El objetivo del repo es tener el "cerebro" en un solo lugar: las reglas de cada pieza,
los candados que no se pueden romper, los ejemplos ganadores reales (swipe) y las piezas
ya producidas y validadas.

> **Principio de fondo:** construir, no comprar. Cuando el hueco es específico de FAP,
> se construye una skill propia en vez de instalar una genérica del banco.

> 🧭 **Fuente de verdad para TODA pieza:** la skill [`fap`](skills/fap.md). Lleva dentro los
> candados, la voz del cliente, las objeciones a anticipar y el candado de voz. Toda skill la
> consulta antes de generar contenido y manda sobre cualquier otra.

---

## Estructura

```
cerebro-operativo-fap/
├── README.md                   ← este índice
├── seguimiento/
│   └── seguimiento.md         ← fases 1–3, método probado y pendientes abiertos
├── skills/                    ← las 7 skills del cerebro
│   ├── fap.md                 ← FUENTE DE VERDAD: candados + voz + objeciones (toda skill la lee)
│   ├── fap-lanzamientos.md
│   ├── fap-narrativa.md
│   ├── fap-landings.md
│   ├── fap-whatsapp-api.md
│   ├── fap-whatsapp-grupos.md
│   └── fap-video-ads-meta.md
├── voz/                       ← lenguaje real del cliente (respaldo de la fuente de verdad)
│   ├── README.md
│   ├── voz-cliente.md         ← cómo habla el cliente (15 llamadas reales, anonimizado)
│   └── mapa-objeciones.md     ← las 8 objeciones por frecuencia
├── swipe/                     ← banco de ejemplos ganadores reales
│   ├── README.md
│   └── swipe-landings.md      ← PILOTO: plantilla por ficha
└── piezas/                    ← piezas ya producidas y validadas
    └── whatsapp-confirmacion-compra.md
```

---

## Las 7 skills del cerebro

| Skill | Rol |
|---|---|
| [`fap`](skills/fap.md) | **Fuente de verdad** — candados + voz + objeciones |
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
- **Voz del cliente:** 15 llamadas reales destiladas en `voz/` e integradas en la fuente de verdad `fap`.
- **En curso — Swipe de ganadoras:** piloto en `landings`.

Detalle y pendientes abiertos en [`seguimiento/seguimiento.md`](seguimiento/seguimiento.md).
