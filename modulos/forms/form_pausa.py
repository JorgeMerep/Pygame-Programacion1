import modulos.forms.form_base as form_base
import modulos.variables as var
from utn_fra.pygame_widgets import (
    Button, Label
)

def iniciar_form_pausa(dict_form_datos: dict):
    """
    Inicializa el formulario de pausa con todos sus componentes.
    
    Args:
        dict_form_datos (dict): Diccionario con los datos base del formulario
    
    Returns:
        dict: Diccionario del formulario creado con todos los componentes de pausa
    """
    form = form_base.crear_form_base(dict_form_datos)
    
    form['titulo'] = Label(
        x=var.DIMENSION_PANTALLA[0] // 2, 
        y=var.DIMENSION_PANTALLA[1] // 2 - 300,
        text=var.TITULO_JUEGO, 
        screen=form.get('pantalla'), 
        font_path=var.RUTA_FUENTE_SAIYAN_SANS, 
        font_size=75, 
        color=var.COLOR_NARANJA
    )
    form['subtitulo'] = Label(
        x=var.DIMENSION_PANTALLA[0] // 2, 
        y=var.DIMENSION_PANTALLA[1] // 2 + 320,
        text='PAUSA', 
        screen=form.get('pantalla'), 
        font_path=var.RUTA_FUENTE_SAIYAN_SANS, 
        font_size=80, 
        color=var.COLOR_NARANJA
    )
    
    form['boton_atras'] = Button(
        x= 180, 
        y=var.DIMENSION_PANTALLA[1] // 2 + 320,
        text= var.BOTON_VOLVER_MENU, 
        screen=form.get('pantalla'), 
        font_path=var.RUTA_FUENTE_SAIYAN_SANS, 
        color=var.COLOR_ROJO,
        font_size= 40,
        on_click=cambiar_form_on_click, 
        on_click_param='form_menu'
    )
    
    form['boton_continuar'] = Button(
        x= 1090, 
        y=var.DIMENSION_PANTALLA[1] // 2 + 320,
        text=var.BOTON_VOLVER_JUEGO, 
        screen=form.get('pantalla'), 
        font_path=var.RUTA_FUENTE_SAIYAN_SANS, 
        color=var.COLOR_ROJO,
        font_size= 40,
        on_click=cambiar_form_on_click, 
        on_click_param='form_juego'
    )
    
    form['lista_objetos'] = [
        form.get('titulo'), 
        form.get('subtitulo'),
        form.get('boton_atras'), 
        form.get('boton_continuar')
    ]
    
    form_base.forms_dict[form.get('nombre')] = form
    
    return form

def cambiar_form_on_click(parametro: str):
    """
    Maneja el evento de clic para cambiar de formulario.
    
    Args:
        parametro (str): Nombre del formulario a activar
    """
    form_base.activar_form(parametro)

def dibujar(dict_form_datos: dict):
    """
    Dibuja el formulario de pausa.
    
    Args:
        dict_form_datos (dict): Diccionario del formulario con todos los componentes
    """
    form_base.dibujar(dict_form_datos)

def actualizar(dict_form_datos: dict):
    """
    Actualiza el estado del formulario de pausa.
    
    Args:
        dict_form_datos (dict): Diccionario del formulario a actualizar
    """
    form_base.actualizar(dict_form_datos)

def activar_musica(dict_form_datos: dict, form_manager: dict):
    """
    Activa la música asociada al formulario de pausa.
    
    Args:
        dict_form_datos (dict): Diccionario del formulario con la ruta de música
        form_manager (dict): Diccionario del gestor de formularios para manejar la música
    """
    form_base.activar_musica(dict_form_datos, form_manager)