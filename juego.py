import pygame, sys
import constantes
import funciones

# Inicio pygame
pygame.init()
pygame.mixer.init()

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

# Rectángulos
rect_titulo = pygame.Rect(constantes.COORDENADA_RECTANGULO_TITULO)
rect_menu = pygame.Rect(constantes.COORDENADA_RECTANGULO_MENU)

# Bucle del juego
while True:
    pantalla.blit(fondo_pantalla_principal, (0, 0)) #Actualiza el fondo de la pantalla pricipal

    # Textos del rectángulo de título
    funciones.render_texto("DRAGON BALL Z", fuente_titulo, constantes.COLOR_ROJO, pantalla, rect_titulo.center)
    funciones.render_texto("MAIN MENU", fuente_subtitulo, constantes.COLOR_ROJO, pantalla, (rect_titulo.centerx, rect_titulo.centery + 60))

    # Textos del rectángulo de menú
    lista_opciones = ["JUGAR", "OPCIONES", "RANKING", "SALIR"]
    espacio_entre_opciones = 55  # Espacio entre cada opción
    eje_x = rect_menu.x + 160  # margen izquierdo 
    eje_y = rect_menu.y + 15  # primer texto un poco más abajo del borde superior del rectángulo

    for indice in range(len(lista_opciones)):
        texto = fuente_menu.render(lista_opciones[indice], True, constantes.COLOR_NARANJA)#Render del texto de las opciones
        pantalla.blit(texto, (eje_x, eje_y + indice * espacio_entre_opciones))#Actualizamos pantalla

    pygame.display.flip()

    for event in pygame.event.get():#Bucle para empezar a manejar los eventos
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
