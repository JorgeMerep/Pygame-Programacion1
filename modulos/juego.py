import pygame 
import sys
import modulos.variables as var
import modulos.forms.form_manager as form_manager
import modulos.jugador as jugador_humano
import modulos.enemigo as enemigo_actual

def jugar_dragon_ball():

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
    