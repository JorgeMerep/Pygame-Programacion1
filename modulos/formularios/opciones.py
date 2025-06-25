import pygame
import modulos.constantes as constantes


def mostrar_config(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event]) -> str:
    retorno = "opciones"

    pygame.display.set_caption(constantes.TITULO_OPCIONES)

    for event in cola_eventos:
        if event.type == pygame.QUIT:
            retorno = "salir"
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if constantes.RECT_MUSICA_ON.collidepoint(x, y):
                pass
                #retorno = "musica_on"
            elif constantes.RECT_MUSICA_OFF.collidepoint(x, y):
                pass
                retorno = "musica_off"
            elif constantes.RECT_VOLVER_ATRAS.collidepoint(x, y):
                pass
                #retorno = "volver_atras"
            
        

    return retorno

    