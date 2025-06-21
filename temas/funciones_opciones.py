import pygame
import constantes

def fondo_pantalla_opciones():
    fondo_pantalla = pygame.image.load(constantes.FONDO_PANTALLA_OPCIONES)
    
    return fondo_pantalla

def musica_pantalla_opciones():
    musica_pantalla_opciones = pygame.mixer.music.load(constantes.MUSICA_PANTALLA_OPCIONES)
    pygame.mixer.music.play(-1)
    
    return musica_pantalla_opciones
