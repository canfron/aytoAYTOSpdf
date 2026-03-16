#!/usr/bin/env python3
"""
Implementación realista con Playwright + interceptación de red para capturar descargas dinámicas (PDFs).
"""

import asyncio
from pathlib import Path
from playwright.async_api import async_playwright


async def main():
    downloads_dir = Path("./downloads")
    downloads_dir.mkdir(exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Lista para almacenar las descargas capturadas
        downloaded_files = []

        # Interceptación de red: capturar respuestas que sean PDFs
        async def handle_response(response):
            url = response.url
            content_type = response.headers.get("content-type", "").lower()
            
            if "application/pdf" in content_type or url.endswith(".pdf"):
                print(f"[+] Capturado PDF: {url}")
                
                # Crear archivo de descarga simulada (en realidad es una respuesta interceptada)
                # Nota: Playwright no permite guardar respuestas directas, así que usaremos page.on("download")
        
        page.on("response", handle_response)

        # Manejo de descargas reales con page.on("download")
        async def handle_download(download):
            path = await download.path()
            suggested_filename = download.suggested_filename
            print(f"[+] Descarga detectada: {suggested_filename}")
            
            # Guardar en carpeta específica
            target_path = downloads_dir / suggested_filename
            await download.save_as(target_path)
            downloaded_files.append(str(target_path))
        
        page.on("download", handle_download)

        # Navegación y login
        print("[*] Navegando a la URL...")
        await page.goto("https://new-espacioclientes.berger-levrault.es/")
        
        # Esperar a que cargue la página de login (ajustar selector según HTML real)
        # await page.wait_for_selector("#username")  # Ejemplo genérico
        print("[*] Login manual requerido (por ahora). Introduce credenciales y pulsa Enter...")
        input("Pulsa Enter tras hacer login...")

        # Navegar a la sección de software
        print("[*] Navegando a la sección de software...")
        await page.goto("https://new-espacioclientes.berger-levrault.es/info/root/199344")
        
        # Ir a pestaña "software"
        # await page.click("text=software")  # Ajustar selector
        
        # Aquí iría la lógica de iteración sobre elementos y descarga de PDFs
        print("[*] Implementación pendiente: recorrer elementos y descargar PDFs")

        # Cerrar navegador
        await browser.close()
        
        print(f"[+] Descargas completadas: {len(downloaded_files)} archivos")
        for f in downloaded_files:
            print(f"  - {f}")


if __name__ == "__main__":
    asyncio.run(main())
