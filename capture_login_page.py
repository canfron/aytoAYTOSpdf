from playwright.sync_api import sync_playwright

def capture_login_html():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Navegar a la página de login
        print("Navegando a la página de login...")
        page.goto("https://new-espacioclientes.berger-levrault.es/")
        
        # Esperar un poco para que cargue todo
        page.wait_for_timeout(5000)
        
        # Guardar el HTML en un archivo
        html_content = page.content()
        with open("login_page.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        print("HTML guardado en login_page.html")
        
        # Esperar para que el usuario pueda ver la página antes de cerrar
        page.wait_for_timeout(3000)
        
        browser.close()

if __name__ == "__main__":
    capture_login_html()
