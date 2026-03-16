#!/usr/bin/env python3
"""
AytoAtoyS PDF Downloader - Script automatizado para descargar PDFs desde la plataforma de Berger Levrault.
"""

import os
import time
from playwright.sync_api import sync_playwright

# Configuración
URL_LOGIN = "https://new-espacioclientes.berger-levrault.es/"
CREDENTIALS = {
    "username": "mario@aranjuez.es",
    "password": "Ozd=_X3).e05"
}
DOWNLOAD_DIR = "./downloads"

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Navegar al login
        print("Navegando a la página de inicio...")
        page.goto(URL_LOGIN)
        time.sleep(5)

        # Buscar campos de login (ajustar selectores según estructura real)
        try:
            username_input = page.wait_for_selector('input[name="username"]', timeout=10000)
            password_input = page.wait_for_selector('input[type="password"]', timeout=10000)
            login_button = page.wait_for_selector('button[type="submit"]', timeout=10000)

            username_input.fill(CREDENTIALS["username"])
            password_input.fill(CREDENTIALS["password"])
            login_button.click()

            print("Login enviado...")
            time.sleep(5)
        except Exception as e:
            print(f"Error en el login: {e}")
            browser.close()
            return

        # Navegar a la sección de software
        print("Navegando a la sección de software...")
        page.goto("https://new-espacioclientes.berger-levrault.es/info/root/199344")
        time.sleep(5)

        # Capturar descargas
        downloads = []

        def handle_download(download):
            path = download.path()
            filename = download.suggested_filename
            downloads.append((filename, path))
            print(f"Descargado: {filename}")

        page.on("download", handle_download)

        # Buscar elementos de software (ajustar según estructura real)
        try:
            # Esperar a que cargue la página y buscar enlaces o botones
            page.wait_for_selector('text=software', timeout=10000)
            print("Pestaña 'software' detectada.")
        except Exception as e:
            print(f"Error al encontrar pestaña software: {e}")

        # ... continuar con lógica de navegación y descarga ...

        browser.close()

if __name__ == "__main__":
    main()
