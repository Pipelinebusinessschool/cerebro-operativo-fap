---
name: fap-landings
description: >-
  Produce o revisa landings de captación de FAP en dos modelos: Largo (Brunson,
  página larga y estructura completa) o Corto (Brasil, página corta y directa).
  Úsala al escribir, estructurar o auditar una landing / página de captación de
  FAP. Hereda los candados: sin precio visible y CTA a llamada de diagnóstico
  (no checkout). Consulta antes la fuente de verdad `fap`; carga el swipe de
  landings ganadoras si está disponible.
---

# Skill · `fap-landings`

**Rol:** producir landings de captación FAP en **dos modelos**.

> ⚠️ **Antes de generar cualquier pieza, consulta la fuente de verdad (skill `fap`)** —
> contexto, candados de voz, objeciones a anticipar y léxico del cliente. Manda sobre esta skill.

## Modelos
- **Largo (Brunson)** — página larga, estructura completa.
- **Corto (Brasil)** — página corta, directa.

## Candados heredados de `fap`
- Sin precio visible.
- CTA a llamada de diagnóstico (no checkout).

## Swipe (ejemplos ganadores)
Esta skill es la del **piloto del banco de swipe**. Carga
[`swipe/swipe-landings.md`](../../../swipe/swipe-landings.md) para inyectar landings ganadoras
reales (copy + métrica + por qué ganó + qué NO copiar).

> Decisión de arquitectura pendiente: incrustar los ejemplos en la skill vs. citarlos como
> doc de referencia. Se decide tras validar el piloto.

## Estado
- [x] Instalada.
- [ ] Conectar swipe validado.
- [ ] Test de activación en chat nuevo pendiente.
