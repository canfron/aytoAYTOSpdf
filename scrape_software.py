#!/usr/bin/env python3
"""
Explorador inicial: Login, ir a SOFTWARE y guardar HTML para análisis.
"""

from playwright.sync_api import sync_playwright
import os

URL_LOGIN = "https://new-espacioclientes.berger-levrault.es/"
USER = "mario@aranjuez.es"
PASS = "Ozd=_X3).e05"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # 1. Login
        print("Navigating to login...")
        page.goto(URL_LOGIN, wait_until="networkidle")
        
        # Buscar campos de login (ajustar selectores según HTML real)
        try:
            page.fill('input[name="username"]', USER)
            page.fill('input[name="password"]', PASS)
            page.click('button[type="submit"]')
            page.wait_for_load_state("networkidle")
        except Exception as e:
            print(f"Error during login: {e}")
        
        # 2. Ir a la sección de software
        print("Navigating to software section...")
        page.goto("https://new-espacioclientes.berger-levrault.es/info/root/199344", wait_until="networkidle")
        
        # Buscar pestaña "software"
        try:
            # Intentar hacer clic en la pestaña 'software'
            page.click('a:has-text("SOFTWARE")', timeout=5000)
            page.wait_for_load_state("networkidle")
        except Exception as e:
            print(f"Error clicking SOFTWARE tab: {e}")
        
        # Guardar HTML generado
        os.makedirs("html_dump", exist_ok=True)
        with open("html_dump/software_section.html", "w", encoding="utf-8") as f:
            f.write(page.content())
        print("HTML saved to html_dump/software_section.html")
        
        input("Press Enter to close browser...")

        browser.close()

if __name__ == "__main__":
    main()
