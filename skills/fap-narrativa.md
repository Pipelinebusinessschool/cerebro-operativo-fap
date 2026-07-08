# Skill · `fap-narrativa`

**Rol:** generar las **3 Big Ideas** y el **brief narrativo** del lanzamiento — el contrato que
alimenta a todas las demás skills (correos, landings, ads, páginas).

**Se activa cuando** el mensaje pide la gran idea, el ángulo o el brief de un lanzamiento FAP:
"dame la Big Idea para el webinar de supervisión", "arma el brief del lanzamiento".

---

## Regla 0 — cargar SIEMPRE antes de escribir

1. **Verdad + candados →** [`../contexto/`](../contexto/). El ICP, la voz, las métricas, la
   filosofía y las decisiones definen qué es verdad y qué se puede prometer. **Si un dato no está,
   PREGUNTA — no lo inventes.**
2. **Craft (opcional) →** el [`../swipe/`](../swipe/) del canal, para calibrar ángulos que ya
   funcionaron.

Esta skill es **upstream**: su salida (el brief) es lo que las skills de canal consumen.

---

## Craft — frameworks

- **Agora / Big Idea** — una idea grande, nueva y creíble; mecanismo único con nombre.
- **Schwartz — niveles de conciencia** del tráfico (inconsciente → consciente del problema →
  de la solución → del producto → del trato). Define el mensaje líder.
- **McKee / Story** — estructura de historia cuando el ángulo es narrativo.
- **PAS / AIDA** — armazón de persuasión de cada pieza.

## Salida — el brief (contrato para las demás skills)

1. **3 Big Ideas candidatas** + recomendación de una (con el porqué).
2. **Brief** con: Big Idea elegida · **ángulo** · **ICP** (de `contexto/`) · **nivel de
   conciencia** del tráfico · **promesa** (mecanismo + resultado + plazo, con cifras sourced) ·
   **prueba** (razones para creer, de `pbs_metrics.md`) · **objeción principal a desactivar** ·
   **CTA por pieza** (registro o diagnóstico) · **ruta** (A o B, ver `fap-lanzamientos`).

---

## Candados FAP (de `contexto/`)

- **Cifras/ICP/precio solo de `contexto/`.** Nada inventado.
- **Voz de Jorge** (`jorge_voice.md`): diagnóstica, con cifras, anti-victimización; nunca
  motivacional vacía. Vocabulario obligatorio/prohibido.
- **El problema es sistémico, nunca personal.**
- **Nunca prometer sin condición** ("para quien implementa, ejecuta y sigue el paso a paso").
- **ICP:** ≥$1M/año + ≥2 vendedores, B2B (excluye B2C y bienes raíces).

## Proceso

1. Recibe tema/objetivo del lanzamiento (o pídelo).
2. Carga `contexto/`.
3. Genera 3 Big Ideas (Agora) sobre el dolor real del ICP → recomienda 1.
4. Arma el brief completo (campos de arriba).
5. **Auto-crítica:** ¿la promesa es sourced? ¿el nivel de conciencia calza con el canal? ¿un solo
   mensaje líder? ¿voz de Jorge? → corrige.
6. Entrega. Falta de dato → `[FALTA: …]` + pregunta.

## Estado
- [ ] Test de activación en chat nuevo.
