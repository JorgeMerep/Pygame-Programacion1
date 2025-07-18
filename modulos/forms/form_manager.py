import pygame
import modulos.variables as var
import modulos.forms.form_menu_ as form_menu_
import modulos.forms.form_opciones as form_opciones
import modulos.forms.form_ranking as form_ranking
import modulos.forms.form_juego as form_juego
import modulos.forms.form_ingresar_datos_ranking as form_ingresar_datos
import modulos.forms.form_pausa as form_pausa


def crear_form_manager(pantalla: pygame.Surface, datos_juego: dict) -> dict:
    """
    Crea y configura el gestor de formularios con todos los formularios del juego.
    
    Args:
        pantalla (pygame.Surface): Superficie principal de la pantalla
        datos_juego (dict): Diccionario con los datos del juego que debe contener:
            - jugador: Datos del jugador
            - enemigo: Datos del enemigo
    
    Returns:
        dict: Diccionario del gestor de formularios con todos los formularios inicializados
    """
    form = {}
    form['pantalla_principal'] = pantalla
    form['nivel_actual'] = 1
    form['juego_comenzado'] = False
    form['musica_actual'] = None
    form['musica_habilitada'] = True 
    form['jugador'] = datos_juego.get('jugador')
    form['enemigo'] = datos_juego.get('enemigo')

        
    form['lista_forms'] = [
        form_menu_.iniciar_form_menu_principal(
            dict_form_datos={
                "form_manager_ref" : form,
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
                "form_manager_ref" : form,
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
                "form_manager_ref" : form,
                "nombre":'form_ranking', 
                "pantalla":form.get('pantalla_principal'), 
                "activo":True,
                "coords":(0,0), 
                "numero_nivel":1, 
                "ruta_musica":var.RUTA_MUSICA_RANKING,
                "ruta_fondo": var.RUTA_FONDO_RANKING,
                "dimension_pantalla": var.DIMENSION_PANTALLA
            }, jugador=form.get('jugador')
        ),
        form_juego.iniciar_form_juego(
            dict_form_datos={
                "form_manager_ref" : form,
                "nombre":'form_juego', 
                "pantalla":form.get('pantalla_principal'), 
                "activo":True,
                "coords":(0,0), 
                "numero_nivel":1, 
                "ruta_musica":var.RUTA_MUSICA_JUEGO,
                "ruta_fondo": var.RUTA_FONDO_JUEGO,
                "dimension_pantalla": var.DIMENSION_PANTALLA
            }, jugador=form.get('jugador'), enemigo=form.get('enemigo')
        ),
        form_ingresar_datos.iniciar_form_ingresar_datos_ranking(
            dict_form_datos={
                "form_manager_ref" : form,
                "nombre":'form_ingresar_datos_ranking', 
                "pantalla":form.get('pantalla_principal'), 
                "activo":True,
                "coords":(0,0), 
                "numero_nivel":1, 
                "ruta_musica":var.RUTA_MUSICA_INGRESAR_DATOS,
                "ruta_fondo": var.RUTA_FONDO_INGRESAR_DATOS_RANKING,
                "dimension_pantalla": var.DIMENSION_PANTALLA
            },jugador=form.get('jugador')
        ),
          form_pausa.iniciar_form_pausa(
            dict_form_datos={
                "form_manager_ref" : form,
                "nombre":'form_pausa', 
                "pantalla":form.get('pantalla_principal'), 
                "activo":True,
                "coords":(0,0), 
                "numero_nivel":1, 
                "ruta_musica":var.RUTA_MUSICA_PAUSA,
                "ruta_fondo": var.RUTA_FONDO_PAUSA,
                "dimension_pantalla": var.DIMENSION_PANTALLA
            }
        ),
    ]
    
    return form


def actualizar_forms(form_manager: dict, lista_eventos: pygame.event.Event):
    """
    Actualiza el formulario activo según el estado del gestor de formularios.
    Verifica cuál formulario está activo y ejecuta sus funciones correspondientes.
    
    Args:
        form_manager (dict): Diccionario del gestor de formularios
        lista_eventos (pygame.event.Event): Lista de eventos de pygame
    """
 
    # FORM MENU
    if form_manager.get('lista_forms')[0].get('activo'):
        form_menu_.actualizar(form_manager.get('lista_forms')[0])
        form_menu_.dibujar(form_manager.get('lista_forms')[0])
        form_menu_.activar_musica(form_manager.get('lista_forms')[0], form_manager)

    # FORM OPCIONES
    elif form_manager.get('lista_forms')[1].get('activo'):
        form_opciones.actualizar(form_manager.get('lista_forms')[1])
        form_opciones.dibujar(form_manager.get('lista_forms')[1])
        form_opciones.activar_musica(form_manager.get('lista_forms')[1], form_manager)
    
    # FORM RANKING
    elif form_manager.get('lista_forms')[2].get('activo'):
        form_ranking.actualizar(form_manager.get('lista_forms')[2])
        form_ranking.dibujar(form_manager.get('lista_forms')[2])
        form_ranking.activar_musica(form_manager.get('lista_forms')[2], form_manager)

    # FORM JUEGO
    elif form_manager.get('lista_forms')[3].get('activo'):
        form_juego.actualizar(form_manager.get('lista_forms')[3], lista_eventos)
        form_juego.dibujar(form_manager.get('lista_forms')[3])
        form_juego.activar_musica(form_manager.get('lista_forms')[3], form_manager)

    # FORM INGRESAR DATOS RANKIING
    elif form_manager.get('lista_forms')[4].get('activo'):
        form_ingresar_datos.actualizar(form_manager.get('lista_forms')[4], lista_eventos)
        form_ingresar_datos.dibujar(form_manager.get('lista_forms')[4])
        form_ingresar_datos.activar_musica(form_manager.get('lista_forms')[4], form_manager)
        
     # FORM PAUSA
    elif form_manager.get('lista_forms')[5].get('activo'):
        form_pausa.actualizar(form_manager.get('lista_forms')[5])
        form_pausa.dibujar(form_manager.get('lista_forms')[5])
        form_pausa.activar_musica(form_manager.get('lista_forms')[5], form_manager)


def actualizar(form_manager: dict, lista_eventos: pygame.event.Event):
    """
    Función principal de actualización que delega la actualización de formularios.
    
    Args:
        form_manager (dict): Diccionario del gestor de formularios
        lista_eventos (pygame.event.Event): Lista de eventos de pygame
    """
    actualizar_forms(form_manager, lista_eventos)
