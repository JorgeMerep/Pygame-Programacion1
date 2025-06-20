# PANTALLA PRINCIPAL
def render_texto(texto, fuente, color, superficie, eje_x, eje_y):
    """
    Renderiza el texto en coordenadas fijas (eje_x, eje_y).

    Args:
        texto: texto a mostrar
        fuente: fuente 
        color: color del texto
        superficie: superficie destino
        eje_x: coordenada de eje_x 
        eje_y: coordenada de eje_y 
    """
    render = fuente.render(texto, True, color)
    superficie.blit(render, (eje_x, eje_y))


def mostrar_titulo_y_subtitulo(pantalla, fuente_titulo, fuente_subtitulo, color):
    """
    Muestra el título y subtítulo en las coordenadas especificas.

    Args:
        pantalla: superficie destino
        fuente_titulo: fuente del título
        fuente_subtitulo: fuente del subtítulo
        color: color del texto
    """
    render_texto("DRAGON BALL Z", fuente_titulo, color, pantalla, 500, 80)      
    render_texto("MAIN MENU", fuente_subtitulo, color, pantalla, 550, 150)       


def mostrar_opciones_menu(pantalla, fuente_menu, opciones, color):
    """
    Dibuja cada opción en coordenadas fijas estilo tupla.

    Args:
        pantalla: superficie destino
        fuente_menu: fuente usada para el texto
        opciones: lista de strings con las opciones
        color: color del texto
    """
    coordenadas = [
        (580, 370),  # JUGAR 
        (580, 430),  # OPCIONES 
        (580, 490),  # RANKING 
        (580, 550)   # SALIR 
    ]

    for indice in range(len(opciones)):
        texto_render = fuente_menu.render(opciones[indice], True, color)
        pantalla.blit(texto_render, coordenadas[indice])

# PANTALLA OPCIONES

