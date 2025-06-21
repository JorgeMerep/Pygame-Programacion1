import pygame
import temas.constantes as constantes


def mostrar_config(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event]) -> str:
    retorno = "opciones"

    pygame.display.set_caption(constantes.TITULO_OPCIONES)

    pass