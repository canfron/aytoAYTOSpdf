import os
import time
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout

# Configuración
BASE_URL = "https://new-espacioclientes.berger-levrault.es"
LOGIN_URL = BASE_URL
TARGET_URL = f"{BASE_URL}/info/root/199344"
USER = "mario@aranjuez.es"
PASS = "Ozd=_X3).e05"

OUTPUT_DIR = os.path.join(os.getcwd(), "descargas", "software")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def safe_click(page, selector, timeout=5000):
    try:
        page.wait_for_selector(selector, timeout=timeout)
        page.click(selector)
    except PlaywrightTimeout:
        print(f"⚠️ No se encontró el elemento: {selector}")

def download_pdfs_from_tab(page, tab_name, folder_name):
    safe_click(page, f'text={tab_name}')
    time.sleep(2)  # Esperar carga

    pdf_links = page.query_selector_all("a[href*='.pdf']")
    if not pdf_links:
        print(f"📄 No se encontraron PDFs en '{tab_name}'")
        return

    folder_path = os.path.join(OUTPUT_DIR, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    for i, link in enumerate(pdf_links):
        href = link.get_attribute("href")
        if not href.startswith("http"):
            href = BASE_URL + href
        filename = os.path.basename(href.split("?")[0])
        safe_filename = filename.replace("/", "_")

        print(f"⬇️  Descargando: {safe_filename}")
        try:
            page.goto(href, wait_until="networkidle")
            time.sleep(1)
        except Exception as e:
            print(f"❌ Error descargando {href}: {e}")

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=True para producción
        context = browser.new_context()
        page = context.new_page()

        # Login
        print("🔑 Iniciando sesión...")
        page.goto(LOGIN_URL, wait_until="networkidle")
        page.fill('input[name="username"]', USER)
        page.fill('input[name="password"]', PASS)
        safe_click(page, 'button[type="submit"]')
        time.sleep(3)

        # Ir al recurso
        print(f"📂 Navegando a {TARGET_URL}")
        page.goto(TARGET_URL, wait_until="networkidle")
        time.sleep(2)

        # Ir a pestaña "software"
        safe_click(page, 'text=Software')
        time.sleep(2)

        # Obtener lista de elementos de software
        software_items = page.query_selector_all("a.software-item")  # Ajustar selector según HTML real
        if not software_items:
            print("⚠️ No se encontraron elementos de software. Revisar selectores.")
            return

        for item in software_items:
            name = item.inner_text().strip()
            print(f"➡️ Procesando: {name}")
            
            # Click en el elemento
            safe_click(page, f"a.software-item >> text={name}")
            time.sleep(2)

            # Descargar PDFs de "documentación"
            download_pdfs_from_tab(page, "Documentación", name.lower().replace(" ", "_"))

            # Volver al listado (o navegar a "Versiones")
            safe_click(page, 'text=Volver')
            time.sleep(1)
            
            # Ir a pestaña "Versiones" del software actual
            safe_click(page, 'text=Versiones')
            time.sleep(2)

            # Descargar PDFs de "Versiones"
            download_pdfs_from_tab(page, "Versiones", f"{name.lower().replace(' ', '_')}_versiones")

        print("✅ Proceso completado.")
        browser.close()

if __name__ == "__main__":
    main()
