# Espacio Clientes Berger & Levraut - Persistencia y Deliberaciones

## Estado Actual (2025-04-05)

### Objetivo
Automatizar descarga de PDFs desde la sección "Software" del Espacio Clientes.

### URL
https://new-espacioclientes.berger-levrault.es/

### Plan Inicial
1. Usar Playwright para automatización browser
2. Capturar descargas con `page.on("download")`
3. Navegar a sección de software tras login manual
4. Iterar elementos y descargar PDFs

### Problemas Identificados
- Login requiere interacción humana (por ahora)
- Estructura HTML desconocida sin autenticación
- Necesario inspeccionar DOM tras login para encontrar selectores correctos

### Próximos Pasos
1. Inspeccionar estructura de página tras login manual
2. Identificar selectores para navegación a sección software
3. Identificar elementos descargables (PDFs)
4. Implementar lógica de iteración y descarga

### Archivos Creados
- `playwright_espacio_clientes.py` - Script base con captura de descargas
- `espacioclientes_persistente.md` - Este archivo para contexto persistente
