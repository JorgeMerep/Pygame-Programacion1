import pygame
import modulos.constantes as constantes

def fondo_pantalla_opciones():
    fondo_pantalla = pygame.image.load(constantes.FONDO_PANTALLA_OPCIONES)

    return fondo_pantalla

def musica_pantalla_opciones(musica_actual):
    if musica_actual != constantes.MUSICA_PANTALLA_OPCIONES:
        pygame.mixer.music.load(constantes.MUSICA_PANTALLA_OPCIONES)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.4)
        return constantes.MUSICA_PANTALLA_OPCIONES
    
    return musica_actual

def render_texto_opciones(texto, fuente, color, superficie, eje_x, eje_y):
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


def mostrar_titulo_y_subtitulo_opciones(pantalla, fuente_titulo, fuente_subtitulo, color):
    """
    Muestra el título y subtítulo en las coordenadas especificas.

    Args:
        pantalla: superficie destino
        fuente_titulo: fuente del título
        fuente_subtitulo: fuente del subtítulo
        color: color del texto
    """
    render_texto_opciones("DRAGON BALL Z", fuente_titulo, color, pantalla, 500, 80)      
    render_texto_opciones("OPCIONES", fuente_subtitulo, color, pantalla, 550, 150)       


def mostrar_config_menu_opciones(pantalla, fuente_menu, opciones, color):
    """
    Dibuja cada opción en coordenadas fijas estilo tupla.

    Args:
        pantalla: superficie destino
        fuente_menu: fuente usada para el texto
        opciones: lista de strings con las opciones
        color: color del texto
    """
    coordenadas = [
        (550, 310),  # MUSICA ON 
        (550, 360),  # MUSICA OFF
        (550, 580)   # VOLVER ATRAS       
    ]

    for indice in range(len(opciones)):
        texto_render = fuente_menu.render(opciones[indice], True, color)
        pantalla.blit(texto_render, coordenadas[indice])


