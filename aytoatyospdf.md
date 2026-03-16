# AytoAtoyS PDF Downloader

## Proyecto
Script automatizado para descargar PDFs desde la plataforma de Berger Levrault (Espacio Clientes).

---

## Acceso
- **URL**: https://new-espacioclientes.berger-levrault.es/
- **Usuario**: mario@aranjuez.es  
- **Password**: Ozd=_X3).e05

---

## Flujo de trabajo
1. Login en la plataforma.
2. Navegar a: `https://new-espacioclientes.berger-levrault.es/info/root/199344`
3. Ir a pestaña **"software"**
4. Para cada elemento (gestión documental, interoperabilidad...):
   - Entrar en el detalle
   - Ir a pestaña **"documentación"** → descargar todos los PDFs
   - Guardar en carpeta: `./downloads/{nombre_elemento}/`
5. Volver al listado de software y repetir con pestaña **"versiones"**

---

## Requisitos técnicos
- Playwright (navegador controlado)
- Interceptación de red para capturar descargas dinámicas
- Manejo de sesiones y cookies

---

## Pendiente
- [ ] Validar estructura HTML/JS de la web  
- [ ] Ajustar selectores dinámicos  
- [ ] Implementar lógica de descarga con `page.on("download")`
