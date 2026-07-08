# Presentaciones

Entregables presentables (para mostrar/compartir), generados a partir del material del cerebro.

## Casos de éxito — Copy del funnel de correo

- **`Casos_de_exito_Copy_Funnel_PBS.pdf`** — documento curado para mostrar a Jorge Conde los
  correos ganadores seleccionados y **por qué** funcionan. 17 correos en 4 fases (invitación,
  recordatorio, venta, postventa), con copy verbatim + ángulo + recursos + mecanismo, y un
  cierre con los patrones transversales.
- **Fuentes:** lanzamientos reales de PBS — *Prospección a Gran Escala con IA* (Nov 2025),
  *Pipeline Predecible con IA*, *Supervisión Comercial Predictiva con IA* y *AI Strategic
  Pipeline Generation*.

### Cómo regenerarlo

El PDF se arma desde `build_casos.py` (contiene los datos de cada correo) → genera
`casos-de-exito-funnel.html` → se imprime a PDF con Chromium:

```bash
python3 build_casos.py
CHROME=/opt/pw-browsers/chromium-1194/chrome-linux/chrome   # ruta del entorno
"$CHROME" --headless --no-sandbox --no-pdf-header-footer \
  --print-to-pdf=Casos_de_exito_Copy_Funnel_PBS.pdf file://$PWD/casos-de-exito-funnel.html
```

Para editar la selección o los textos, se ajusta la lista `emails` en `build_casos.py` y se
vuelve a generar. Nota: no se incluyen métricas (no se inventan); "por qué funciona" es análisis
de craft sobre piezas ya validadas.
