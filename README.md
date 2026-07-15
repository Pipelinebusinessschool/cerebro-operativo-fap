# Cerebro Operativo FAP

Sistema de skills propias para producir las piezas de marketing y captación de **FAP**
(high-ticket B2B, sin precio en captación, CTA a llamada de diagnóstico).

El objetivo del repo es tener el "cerebro" en un solo lugar: las reglas de cada pieza,
los candados que no se pueden romper, los ejemplos ganadores reales (swipe) y las piezas
ya producidas y validadas.

> **Principio de fondo:** construir, no comprar. Cuando el hueco es específico de FAP,
> se construye una skill propia en vez de instalar una genérica del banco.

> 🧭 **Fuente de verdad para TODA pieza:** la skill [`fap`](.claude/skills/fap/SKILL.md). Lleva
> dentro los candados, la voz del cliente, las objeciones a anticipar y el candado de voz. Toda
> skill la consulta antes de generar contenido y manda sobre cualquier otra.

> ⚙️ **Instaladas como skills del harness:** las 7 viven en `.claude/skills/<nombre>/SKILL.md` y
> se invocan con `/` (p. ej. `/fap`, `/fap-landings`). Claude las descubre por su frontmatter
> (`name` + `description`). Los archivos en `skills/` de la raíz son punteros históricos.

---

## Estructura

```
cerebro-operativo-fap/
├── README.md                   ← este índice
├── .claude/skills/            ← las 8 skills INSTALADAS (invocables con /)
│   ├── fap/SKILL.md           ← FUENTE DE VERDAD: candados + voz + objeciones (toda skill la lee)
│   ├── fap-lanzamientos/SKILL.md
│   ├── fap-narrativa/SKILL.md
│   ├── fap-landings/SKILL.md
│   ├── fap-correos/SKILL.md
│   ├── fap-whatsapp-api/SKILL.md
│   ├── fap-whatsapp-grupos/SKILL.md
│   └── fap-video-ads-meta/SKILL.md
├── skills/                    ← punteros históricos a las skills instaladas
├── seguimiento/
│   └── seguimiento.md         ← fases 1–3, método probado y pendientes abiertos
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

## Las 8 skills del cerebro

| Skill | Invocación | Rol |
|---|---|---|
| [`fap`](.claude/skills/fap/SKILL.md) | `/fap` | **Fuente de verdad** — candados + voz + objeciones |
| [`fap-lanzamientos`](.claude/skills/fap-lanzamientos/SKILL.md) | `/fap-lanzamientos` | Director (2 rutas, piezas, cadencia) |
| [`fap-narrativa`](.claude/skills/fap-narrativa/SKILL.md) | `/fap-narrativa` | 3 Big Ideas + brief (Agora, McKee, Edwards, Schwartz, PAS/AIDA) |
| [`fap-landings`](.claude/skills/fap-landings/SKILL.md) | `/fap-landings` | Dos modelos (Largo Brunson / Corto Brasil) |
| [`fap-correos`](.claude/skills/fap-correos/SKILL.md) | `/fap-correos` | Secuencias de email (invitación, recordatorios, post-evento, reactivación) |
| [`fap-whatsapp-api`](.claude/skills/fap-whatsapp-api/SKILL.md) | `/fap-whatsapp-api` | 1:1 + cumplimiento API |
| [`fap-whatsapp-grupos`](.claude/skills/fap-whatsapp-grupos/SKILL.md) | `/fap-whatsapp-grupos` | Comunidad |
| [`fap-video-ads-meta`](.claude/skills/fap-video-ads-meta/SKILL.md) | `/fap-video-ads-meta` | Jorge a cámara, optimizado Meta + segmentación |

---

## Estado del proyecto

- **Fase 1 — Revisión del banco de skills genéricas:** cerrada. Ninguna instalada; se rescató craft.
- **Fase 2 — Construcción del cerebro:** 8 skills propias construidas e instaladas.
- **Fase 3 — Validación:** kit completo de prueba (workshop de Contratación) coherente y con candados intactos → el cerebro generaliza.
- **Voz del cliente:** 15 llamadas reales destiladas en `voz/` e integradas en la fuente de verdad `fap`.
- **En curso — Swipe de ganadoras:** `landings` (piloto) + `correos` ✅ (cableado a `fap-correos`); `ads` pendiente.

Detalle y pendientes abiertos en [`seguimiento/seguimiento.md`](seguimiento/seguimiento.md).
