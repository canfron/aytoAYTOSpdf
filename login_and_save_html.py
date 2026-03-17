from playwright.sync_api import sync_playwright

def main():
    url = "https://new-espacioclientes.berger-levrault.es/"
    usuario = "mario@aranjuez.es"
    password = "Ozd=_X3).e05"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Navegar a la página
        print("Navegando a:", url)
        page.goto(url)
        
        # Rellenar usuario y contraseña (ajustar selectores según HTML real)
        # Esperamos un momento para que cargue el DOM
        page.wait_for_timeout(3000)
        
        # Intentar encontrar campos de login
        try:
            # Buscamos inputs de texto y contraseña
            inputs = page.locator("input")
            count = inputs.count()
            print(f"Encontrados {count} inputs en la página")
            
            for i in range(count):
                input_elem = inputs.nth(i)
                input_type = input_elem.get_attribute("type") or "text"
                input_name = input_elem.get_attribute("name") or ""
                input_id = input_elem.get_attribute("id") or ""
                
                print(f"Input {i}: type={input_type}, name={input_name}, id={input_id}")
                
                if input_type == "text" and not usuario_encontrado:
                    print(f"Rellenando usuario en input {i}")
                    input_elem.fill(usuario)
                    usuario_encontrado = True
                elif input_type == "password":
                    print(f"Rellenando contraseña en input {i}")
                    input_elem.fill(password)
            
            # Buscar botón de login
            buttons = page.locator("button")
            btn_count = buttons.count()
            print(f"Encontrados {btn_count} botones")
            
            for i in range(btn_count):
                btn = buttons.nth(i)
                btn_text = btn.inner_text()
                print(f"Botón {i}: '{btn_text}'")
                
                if "login" in btn_text.lower() or "entrar" in btn_text.lower():
                    print("Haciendo click en botón de login")
                    btn.click()
                    break
            
            # Esperar a que cargue la página tras login
            page.wait_for_timeout(5000)
            
        except Exception as e:
            print(f"Error durante el login: {e}")
        
        # Guardar HTML resultante
        html_content = page.content()
        with open("espacioclientes_login.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        print("HTML guardado en espacioclientes_login.html")
        
        browser.close()

if __name__ == "__main__":
    main()
