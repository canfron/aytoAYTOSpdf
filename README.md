# 📁 aytoAYTOSpdf - Índice de Archivos del Proyecto

> **Repositorio original:** https://github.com/canfron/aytoAYTOSpdf  
> **Rama:** `main`  
> **Propósito:** Descarga automatizada de PDFs de sitios municipales (ayuntamientos)  
> **Lenguajes:** Python (27%), HTML (73%)

---

## 🗂️ Estructura de Archivos

### 🐍 Scripts Python (Lógica principal)

| Archivo | Descripción | URL GitHub | URL RAW |
|---------|-------------|------------|---------|
| `capture_login_page.py` | Captura la página de login para análisis | [Ver](https://github.com/canfron/aytoAYTOSpdf/blob/main/capture_login_page.py) | [RAW](https://raw.githubusercontent.com/canfron/aytoAYTOSpdf/main/capture_login_page.py) |
| `download_pdf_real.py` | Descarga real de PDFs (producción) | [Ver](https://github.com/canfron/aytoAYTOSpdf/blob/main/download_pdf_real.py) | [RAW](https://raw.githubusercontent.com/canfron/aytoAYTOSpdf/main/download_pdf_real.py) |
| `download_pdfs.py` | Script principal de descarga | [Ver](https://github.com/canfron/aytoAYTOSpdf/blob/main/download_pdfs.py) | [RAW](https://raw.githubusercontent.com/canfron/aytoAYTOSpdf/main/download_pdfs.py) |
| `download_script.py` | Script genérico de descarga | [Ver](https://github.com/canfron/aytoAYTOSpdf/blob/main/download_script.py) | [RAW](https://raw.githubusercontent.com/canfron/aytoAYTOSpdf/main/download_script.py) |
| `download_software_pdfs.py` | Descarga específica para software | [Ver](https://github.com/canfron/aytoAYTOSpdf/blob/main/download_software_pdfs.py) | [RAW](https://raw.githubusercontent.com/canfron/aytoAYTOSpdf/main/download_software_pdfs.py) |
| `login_and_capture.py` | Login + captura de contenido | [Ver](https://github.com/canfron/aytoAYTOSpdf/blob/main/login_and_capture.py) | [RAW](https://raw.githubusercontent.com/canfron/aytoAYTOSpdf/main/login_and_capture.py) |
| `login_and_save_html.py` | Login y guardado de HTML | [Ver](https://github.com/canfron/aytoAYTOSpdf/blob/main/login_and_save_html.py) | [RAW](https://raw.githubusercontent.com/canfron/aytoAYTOSpdf/main/login_and_save_html.py) |
| `playwright_espacio_clientes.py` | Automatización con Playwright | [Ver](https://github.com/canfron/aytoAYTOSpdf/blob/main/playwright_espacio_clientes.py) | [RAW](https://raw.githubusercontent.com/canfron/aytoAYTOSpdf/main/playwright_espacio_clientes.py) |
| `scrape_software.py` | Scraping específico para software | [Ver](https://github.com/canfron/aytoAYTOSpdf/blob/main/scrape_software.py) | [RAW](https://raw.githubusercontent.com/canfron/aytoAYTOSpdf/main/scrape_software.py) |

### 🌐 Archivos HTML (Snapshots/Capturas)

| Archivo | Descripción | URL GitHub | URL RAW |
|---------|-------------|------------|---------|
| `espacioclientes_login.html` | HTML del login de espacio clientes | [Ver](https://github.com/canfron/aytoAYTOSpdf/blob/main/espacioclientes_login.html) | [RAW](https://raw.githubusercontent.com/canfron/aytoAYTOSpdf/main/espacioclientes_login.html) |
| `login_page.html` | Página de login capturada | [Ver](https://github.com/canfron/aytoAYTOSpdf/blob/main/login_page.html) | [RAW](https://raw.githubusercontent.com/canfron/aytoAYTOSpdf/main/login_page.html) |

### 📄 Documentación y Configuración

| Archivo | Descripción | URL GitHub | URL RAW |
|---------|-------------|------------|---------|
| `README.md` | Documentación principal | [Ver](https://github.com/canfron/aytoAYTOSpdf/blob/main/README.md) | [RAW](https://raw.githubusercontent.com/canfron/aytoAYTOSpdf/main/README.md) |
| `aytoaytospdf.md` | Documentación específica del proyecto | [Ver](https://github.com/canfron/aytoAYTOSpdf/blob/main/aytoaytospdf.md) | [RAW](https://raw.githubusercontent.com/canfron/aytoAYTOSpdf/main/aytoaytospdf.md) |
| `espacioclientes_persistente.md` | Notas sobre persistencia | [Ver](https://github.com/canfron/aytoAYTOSpdf/blob/main/espacioclientes_persistente.md) | [RAW](https://raw.githubusercontent.com/canfron/aytoAYTOSpdf/main/espacioclientes_persistente.md) |
| `proyecto_persistente.md` | Documentación del proyecto persistente | [Ver](https://github.com/canfron/aytoAYTOSpdf/blob/main/proyecto_persistente.md) | [RAW](https://raw.githubusercontent.com/canfron/aytoAYTOSpdf/main/proyecto_persistente.md) |
| `task_problema.md` | Registro de problemas/incidencias | [Ver](https://github.com/canfron/aytoAYTOSpdf/blob/main/task_problema.md) | [RAW](https://raw.githubusercontent.com/canfron/aytoAYTOSpdf/main/task_problema.md) |
| `task_progress.md` | Seguimiento de tareas | [Ver](https://github.com/canfron/aytoAYTOSpdf/blob/main/task_progress.md) | [RAW](https://raw.githubusercontent.com/canfron/aytoAYTOSpdf/main/task_progress.md) |
| `.continue/rules` | Reglas para Continue.dev (IA local) | [Ver](https://github.com/canfron/aytoAYTOSpdf/blob/main/.continue/rules) | [RAW](https://raw.githubusercontent.com/canfron/aytoAYTOSpdf/main/.continue/rules) |

### 📁 Carpetas

| Carpeta | Descripción | URL |
|---------|-------------|-----|
| `html_dump/` | Directorio para volcados HTML (output) | [Ver](https://github.com/canfron/aytoAYTOSpdf/tree/main/html_dump) |

---

## 🔄 Workflow General del Proyecto

```mermaid
graph TD
    A[Login en espacio clientes] --> B[Capturar página/HTML]
    B --> C[Extraer enlaces a PDFs]
    C --> D[Descargar PDFs con playwright/requests]
    D --> E[Guardar en html_dump/ o carpeta destino]
    
    F[Configuración .continue/rules] -.-> A
    G[Documentación md] -.-> H[Mantenimiento y debugging]
