from playwright.sync_api import sync_playwright

URL = "https://new-espacioclientes.berger-levrault.es/"
USER = "mario@aranjuez.es"
PASS = "Ozd=_X3).e05"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Ir a la página de login
        page.goto(URL)

        # Esperar y rellenar formulario (ajustar selectores según HTML real)
        page.wait_for_selector("input[type='email']", timeout=10000)
        page.fill("input[type='email']", USER)
        page.fill("input[type='password']", PASS)
        page.click("button[type='submit']")

        # Esperar redirección y carga de dashboard
        page.wait_for_load_state("networkidle")
        
        # Guardar HTML del dashboard
        with open("dashboard.html", "w", encoding="utf-8") as f:
            f.write(page.content())

        print("✅ HTML guardado en dashboard.html")

        # Navegar a la sección de software
        target_url = "https://new-espacioclientes.berger-levrault.es/info/root/199344"
        page.goto(target_url)
        page.wait_for_load_state("networkidle")
        
        # Guardar HTML de la página de software
        with open("software_page.html", "w", encoding="utf-8") as f:
            f.write(page.content())

        print("✅ HTML de software guardado en software_page.html")

        browser.close()

if __name__ == "__main__":
    main()
