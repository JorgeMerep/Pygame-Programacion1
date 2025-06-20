import pygame, sys
import constantes as constantes
import funciones as funciones
import formularios.menu as menu
import formularios.opciones as opciones


def play_dbz():
    pantalla = pygame.display.set_mode(constantes.TAMAÑO_PANTALLA)
    pygame.display.set_caption(constantes.TITULO_JUEGO)

    icono_pantalla = pygame.image.load(constantes.ICONO_JUEGO)
    pygame.display.set_icon(icono_pantalla)

    fondo_pantalla = pygame.image.load(constantes.FONDO_PANTALLA_PRINCIPAL)
    pygame.mixer.music.load(constantes.MUSICA_PANTALLA_PRINCIPAL)
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
            funciones.mostrar_titulo_y_subtitulo(pantalla, fuente_titulo, fuente_subtitulo, constantes.COLOR_ROJO)
            lista_opciones = ["JUGAR", "OPCIONES", "RANKING", "SALIR"]
            funciones.mostrar_opciones_menu(pantalla, fuente_menu, lista_opciones, constantes.COLOR_NARANJA)
            formulario_actual = menu.mostrar_menu(pantalla, cola_eventos)

        elif formulario_actual == "opciones":
            fondo_pantalla = pygame.image.load(constantes.FONDO_PANTALLA_OPCIONES)
            pygame.mixer.music.load(constantes.MUSICA_PANTALLA_OPCIONES)
            pygame.mixer.music.play(-1)
            formulario_actual = opciones.mostrar_config(pantalla, cola_eventos)  # ✅ Corrección aquí

        elif formulario_actual == "salir":
            ejecutando = False

        pygame.display.flip()  # ✅ Solo una vez al final del ciclo
