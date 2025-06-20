import pygame, sys
import constantes as constantes
import funciones as funciones
import formularios.menu as menu

def play_dbz():

    # Pantalla
    pantalla = pygame.display.set_mode(constantes.TAMAÑO_PANTALLA)
    pygame.display.set_caption(constantes.TITULO_JUEGO)

    #Icono Ventana
    icono_pantalla = pygame.image.load(constantes.ICONO_JUEGO)
    pygame.display.set_icon(icono_pantalla)

    # Fondo
    fondo_pantalla_principal = pygame.image.load(constantes.FONDO_PANTALLA_PRINCIPAL)

    # Música
    pygame.mixer.music.load(constantes.MUSICA_PANTALLA_PRINCIPAL)
    pygame.mixer.music.play(-1)#Se repite en bucle indefinidamente

    # Fuente
    fuente_titulo = pygame.font.Font(constantes.FUENTE_TITULO, 64)
    fuente_subtitulo = pygame.font.Font(constantes.FUENTE_TITULO, 54)
    fuente_menu = pygame.font.Font(constantes.FUENTE_MENU, 44)

    #Clock
    reloj = pygame.time.Clock()

    #Ejecutando
    ejecutando = True

    #Bandera
    bandera = False

    #Formularios
    formulario_actual = "menu"

    # Bucle del juego
    while ejecutando:

        cola_eventos = pygame.event.get()
        reloj.tick(constantes.FPS)

        if formulario_actual == "menu":
            formulario_actual = menu.mostrar_menu(pantalla, cola_eventos,)
        
        elif formulario_actual == "salir":
            ejecutando = False

        pantalla.blit(fondo_pantalla_principal, (0, 0)) #Actualiza el fondo de la pantalla pricipal

        funciones.mostrar_titulo_y_subtitulo(pantalla, fuente_titulo, fuente_subtitulo, constantes.COLOR_ROJO)

        lista_opciones = ["JUGAR", "OPCIONES", "RANKING", "SALIR"]
        funciones.mostrar_opciones_menu(pantalla, fuente_menu, lista_opciones, constantes.COLOR_NARANJA)

        pygame.display.flip()

        


