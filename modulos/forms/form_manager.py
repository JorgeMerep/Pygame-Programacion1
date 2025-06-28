import pygame as pygame
import modulos.variables as var
import modulos.forms.form_menu_ as form_menu_
import modulos.forms.form_opciones as form_opciones
import modulos.forms.form_ranking as form_ranking


def crear_form_manager(pantalla: pygame.Surface, datos_juego: dict) -> dict:
    form = {}
    form['pantalla_principal'] = pantalla
    form['nivel_actual'] = 1
    form['juego_comenzado'] = False
    form['jugador'] = None
    form['enemigo'] = None
    
    form['jugador'] = datos_juego.get('jugador')
    
    form['lista_forms'] = [
        form_menu_.iniciar_form_menu_principal(
            dict_form_datos={
                "nombre":'form_menu', 
                "pantalla":form.get('pantalla_principal'), 
                "activo":True,
                "coords":(0,0), 
                "numero_nivel":1, 
                "ruta_musica":var.RUTA_MUSICA_MENU,
                "ruta_fondo": var.RUTA_FONDO_MENU,
                "dimension_pantalla": var.DIMENSION_PANTALLA
            }
        ),
        form_opciones.iniciar_form_opciones(
            dict_form_datos={
                "nombre":'form_opciones', 
                "pantalla":form.get('pantalla_principal'), 
                "activo":True,
                "coords":(0,0), 
                "numero_nivel":1, 
                "ruta_musica":var.RUTA_MUSICA_OPCIONES,
                "ruta_fondo": var.RUTA_FONDO_OPCIONES,
                "dimension_pantalla": var.DIMENSION_PANTALLA
            }
        ),
        form_ranking.iniciar_form_ranking(
            dict_form_datos={
                "nombre":'form_ranking', 
                "pantalla":form.get('pantalla_principal'), 
                "activo":True,
                "coords":(0,0), 
                "numero_nivel":1, 
                "ruta_musica":var.RUTA_MUSICA_RANKING,
                "ruta_fondo": var.RUTA_FONDO_RANKING,
                "dimension_pantalla": var.DIMENSION_PANTALLA
            }, jugador=form.get('jugador')
        )
    ]
    
    return form


def actualizar_forms(form_manager: dict, lista_eventos: pygame.event.Event):
    # Preguntar por cada uno de los formularios si esta activo
    # en caso de estarlo, dibujar y actualizar
    
    # FORM MENU
    if form_manager.get('lista_forms')[0].get('activo'):
        form_menu_.actualizar(form_manager.get('lista_forms')[0])
        form_menu_.dibujar(form_manager.get('lista_forms')[0])
    
    # FORM OPCIONES
    elif form_manager.get('lista_forms')[1].get('activo'):
        form_opciones.actualizar(form_manager.get('lista_forms')[1])
        form_opciones.dibujar(form_manager.get('lista_forms')[1])
    
    # FORM RANKING
    elif form_manager.get('lista_forms')[2].get('activo'):
        form_ranking.actualizar(form_manager.get('lista_forms')[2])
        form_ranking.dibujar(form_manager.get('lista_forms')[2])


def actualizar(form_manager: dict, lista_eventos: pygame.event.Event):
    actualizar_forms(form_manager, lista_eventos)
    