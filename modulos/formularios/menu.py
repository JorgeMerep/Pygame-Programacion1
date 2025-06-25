import pygame
import modulos.constantes as constantes


def mostrar_menu(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event]) -> str:
    retorno = "menu"

    pygame.display.set_caption(constantes.TITULO_JUEGO)

    for event in cola_eventos:
        if event.type == pygame.QUIT:
            retorno = "salir"
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if constantes.RECT_JUGAR.collidepoint(x, y):
                pass
                #retorno = "jugar"
            elif constantes.RECT_OPCIONES.collidepoint(x, y):
                retorno = "opciones"
            elif constantes.RECT_RANKING.collidepoint(x, y):
                pass
                #retorno = "ranking"
            elif constantes.RECT_SALIR.collidepoint(x, y):
                retorno = "salir"

    return retorno

                 