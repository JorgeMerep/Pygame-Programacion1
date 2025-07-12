import pygame 
import sys
import modulos.variables as var
import modulos.forms.form_manager as form_manager
import modulos.jugador as jugador_humano
import modulos.enemigo as enemigo_actual

def jugar_dragon_ball():
    """
    Función principal del juego Dragon Ball que inicializa pygame, crea la ventana,
    configura el juego y ejecuta el bucle principal.
    
    Inicializa:
    - Pygame y el mixer de audio
    - La ventana del juego con título e icono
    - Los datos del juego (puntaje, vidas, jugador, enemigo)
    - El gestor de formularios
    
    Ejecuta el bucle principal que:
    - Maneja los eventos de pygame
    - Actualiza los formularios
    - Refresca la pantalla
    - Controla los FPS
    
    Termina limpiamente cuando se cierra la ventana.
    """
    pygame.init()
    pygame.mixer.init()
    
    pygame.display.set_caption(var.TITULO_JUEGO)
    pantalla = pygame.display.set_mode(var.DIMENSION_PANTALLA)
    pygame.display.set_icon(pygame.image.load(var.RUTA_ICONO))
    corriendo =True
    reloj = pygame.time.Clock()
    datos_juego = {
        "puntaje": 0,
        "cantidad_vidas": var.CANTIDAD_VIDAS,
        "jugador": jugador_humano.inicializar_jugador(),
        "enemigo": enemigo_actual.inicializar_enemigo(),
    }
        
    f_manager = form_manager.crear_form_manager(pantalla, datos_juego)
        
    while corriendo:
        
        lista_eventos = pygame.event.get()
        reloj.tick(var.FPS)
        
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                corriendo = False
                
        form_manager.actualizar(f_manager, lista_eventos)
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()
