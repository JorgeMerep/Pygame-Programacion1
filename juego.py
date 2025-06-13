import pygame, sys
import constantes

 # Inicio pygame
pygame.init() 

# Tamaño pantalla
pantalla = pygame.display.set_mode(constantes.TAMAÑO_PANTALLA)

# Definicion de Titulo e icono de pantalla 
pygame.display.set_caption(constantes.TITULO_JUEGO)
icono_pantalla = pygame.image.load(constantes.ICONO_JUEGO)
pygame.display.set_icon(icono_pantalla)

# Fondo Pantalla Principal
fondo_pantalla_principal = pygame.image.load(constantes.FONDO_PANTALLA_PRINCIPAL)

# Bucle principal del juego
while True:
    pantalla.blit(fondo_pantalla_principal, (0, 0))  #Actualiza fondo de pantalla principal
    pygame.display.flip()  # ✅ Actualiza la pantalla

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
