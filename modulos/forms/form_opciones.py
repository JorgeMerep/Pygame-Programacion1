import modulos.forms.form_base as form_base
import modulos.variables as var
import pygame
from utn_fra.pygame_widgets import (
    Button, Label
)

def iniciar_form_opciones(dict_form_datos: dict):
    """
    Inicializa el formulario de opciones con todos sus componentes.
    
    Args:
        dict_form_datos (dict): Diccionario con los datos base del formulario
    
    Returns:
        dict: Diccionario del formulario creado con todos los componentes de opciones
    """
    form = form_base.crear_form_base(dict_form_datos)
    
    form['label_titulo'] = Label(
        x=var.DIMENSION_PANTALLA[0]//2, 
        y=100,
        text=var.TITULO_JUEGO, 
        screen=form.get('pantalla'), 
        font_path=var.RUTA_FUENTE_SAIYAN_SANS,
        font_size=60
        )

    form['label_subtitulo'] = Label(
        x=var.DIMENSION_PANTALLA[0]//2, 
        y=180,
        text=var.TEXTO_OPCIONES, 
        screen=form.get('pantalla'), 
        font_path=var.RUTA_FUENTE_SAIYAN_SANS, 
        font_size=55
        )

    form['boton_musica_on'] = Button(
        x=var.DIMENSION_PANTALLA[0]//2, 
        y=320, 
        text=var.BOTON_MUSICA_ON, 
        screen=form.get('pantalla'), 
        font_path=var.RUTA_FUENTE_SAIYAN_SANS, 
        color=var.COLOR_NARANJA, 
        font_size=44, 
        on_click=click_music_on, 
        on_click_param=''
        )

    form['boton_musica_off'] = Button(
        x=var.DIMENSION_PANTALLA[0]//2, 
        y=395, 
        text=var.BOTON_MUSICA_OFF, 
        screen=form.get('pantalla'), 
        font_path=var.RUTA_FUENTE_SAIYAN_SANS, 
        color=var.COLOR_NARANJA, 
        font_size=44, 
        on_click=click_music_off, 
        on_click_param=''
        )
    
    form['boton_volver'] = Button(
        x=var.DIMENSION_PANTALLA[0]//2, 
        y=595, 
        text=var.BOTON_VOLVER_MENU, 
        screen=form.get('pantalla'), 
        font_path=var.RUTA_FUENTE_SAIYAN_SANS, 
        color=var.COLOR_NARANJA, 
        font_size=55, 
        on_click=click_volver,
        on_click_param='form_menu'
        )
    
    
    form['lista_objetos'] = [
        form.get('label_titulo'), 
        form.get('label_subtitulo'), 
        form.get('boton_musica_on'),
        form.get('boton_musica_off'),
        form.get('boton_volver')
    ]
    
    form_base.forms_dict[dict_form_datos.get('nombre')] = form
    
    return form

def click_volver(parametro: str):
    """
    Maneja el evento de clic en el botón volver y activa el formulario especificado.
    
    Args:
        parametro (str): Nombre del formulario a activar
    """
    form_base.activar_form(parametro)

def click_music_on(parametro: str):
    """
    Maneja el evento de clic en el botón de música encendida.
    Habilita la música en el gestor de formularios y la reproduce.
    
    Args:
        parametro (str): Parámetro pasado al hacer clic (no utilizado)
    """
    form = form_base.forms_dict.get("form_opciones")
    if form:
        form_manager_ref = form.get("form_manager_ref")
        if form_manager_ref:
            form_manager_ref["musica_habilitada"] = True
            ruta = form.get("ruta_musica")
            if ruta:
                form_base.reproducir_musica(ruta, form_manager_ref, forzar=True)

def click_music_off(parametro: str):
    """
    Maneja el evento de clic en el botón de música apagada.
    Deshabilita la música en el gestor de formularios y la detiene.
    
    Args:
        parametro (str): Parámetro pasado al hacer clic (no utilizado)
    """
    form = form_base.forms_dict.get("form_opciones")
    if form:
        form_manager_ref = form.get("form_manager_ref")
        if form_manager_ref:
            form_manager_ref["musica_habilitada"] = False
            pygame.mixer.music.stop()

def dibujar(dict_form_datos: dict):
    """
    Dibuja el formulario de opciones.
    
    Args:
        dict_form_datos (dict): Diccionario del formulario con todos los componentes
    """
    form_base.dibujar(dict_form_datos)

def actualizar(dict_form_datos: dict):
    """
    Actualiza el estado del formulario de opciones.
    
    Args:
        dict_form_datos (dict): Diccionario del formulario a actualizar
    """
    form_base.actualizar(dict_form_datos)

def activar_musica(dict_form_datos: dict, form_manager: dict):
    """
    Activa la música asociada al formulario de opciones.
    
    Args:
        dict_form_datos (dict): Diccionario del formulario con la ruta de música
        form_manager (dict): Diccionario del gestor de formularios para manejar la música
    """
    form_base.activar_musica(dict_form_datos, form_manager)

