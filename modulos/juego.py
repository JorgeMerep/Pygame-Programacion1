import pygame, sys
import modulos.constantes as constantes
import modulos.funciones_menu as funciones_menu
import modulos.funciones_opciones as funciones_opciones
import modulos.formularios.menu as menu
import modulos.formularios.opciones as opciones


def play_dbz():
    pantalla = pygame.display.set_mode(constantes.TAMAÑO_PANTALLA)
    pygame.display.set_caption(constantes.TITULO_JUEGO)

    icono_pantalla = pygame.image.load(constantes.ICONO_JUEGO)
    pygame.display.set_icon(icono_pantalla)

    fondo_pantalla = pygame.image.load(constantes.FONDO_PANTALLA_PRINCIPAL)
    musica_actual = constantes.MUSICA_PANTALLA_PRINCIPAL
    pygame.mixer.music.load(musica_actual)
    pygame.mixer.music.play(-1)

    fuente_titulo = pygame.font.Font(constantes.FUENTE_TITULO, 64)
    fuente_subtitulo = pygame.font.Font(constantes.FUENTE_TITULO, 54)
    fuente_menu = pygame.font.Font(constantes.FUENTE_MENU, 44)

    reloj = pygame.time.Clock()
    ejecutando = True
    formulario_actual = "menu"

    while ejecutando:
        cola_eventos = pygame.event.get()
        reloj.tick(constantes.FPS)

        # Pintar fondo antes de todo
        pantalla.blit(fondo_pantalla, (0, 0))

        if formulario_actual == "menu":
            funciones_menu.mostrar_titulo_y_subtitulo(pantalla, fuente_titulo, fuente_subtitulo, constantes.COLOR_ROJO)
            lista_opciones_menu = ["JUGAR", "OPCIONES", "RANKING", "SALIR"]
            funciones_menu.mostrar_opciones_menu(pantalla, fuente_menu, lista_opciones_menu, constantes.COLOR_NARANJA)
            formulario_actual = menu.mostrar_menu(pantalla, cola_eventos)

        elif formulario_actual == "opciones":
            fondo_pantalla = funciones_opciones.fondo_pantalla_opciones()
            funciones_opciones.mostrar_titulo_y_subtitulo_opciones(pantalla,fuente_titulo, fuente_subtitulo, constantes.COLOR_ROJO)
            lista_config_opciones = ["MUSICA ON", "MUSICA OFF", "VOLVER ATRAS"]
            funciones_opciones.mostrar_config_menu_opciones(pantalla,fuente_menu,lista_config_opciones, constantes.COLOR_NARANJA)
            musica_actual = funciones_opciones.musica_pantalla_opciones(musica_actual)
            formulario_actual = opciones.mostrar_config(pantalla, cola_eventos)  

        elif formulario_actual == "salir":
            ejecutando = False

        pygame.display.flip()  
