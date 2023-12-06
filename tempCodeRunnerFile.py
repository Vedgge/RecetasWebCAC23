    # Estilo 'modificarElementos'
    with open('RecetasWebCAC23/formulariosweb/estilos-modificarElementos.html', 'r', encoding='utf-8') as archivo_estilos_modificar_elementos:
        pagina = pagina.replace("{{estilos-modificarElementos}}", archivo_estilos_modificar_elementos.read())