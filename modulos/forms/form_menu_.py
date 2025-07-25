import sys
import modulos.forms.form_base as form_base
import modulos.nivel_cartas as nivel_cartas
import modulos.variables as var
from utn_fra.pygame_widgets import (
    Button, Label,
)


def iniciar_form_menu_principal(dict_form_datos: dict):
    """
    Inicializa el formulario del menú principal con todos sus componentes.
    
    Args:
        dict_form_datos (dict): Diccionario con los datos base del formulario
    
    Returns:
        dict: Diccionario del formulario creado con todos los componentes del menú
    """
    form = form_base.crear_form_base(dict_form_datos)
    
    form['label_titulo'] = Label(
        x=var.DIMENSION_PANTALLA[0]//2, 
        y=100,text=var.TITULO_JUEGO, 
        screen=form.get('pantalla'), 
        font_path=var.RUTA_FUENTE_SAIYAN_SANS, 
        font_size=60
        )
    
    form['label_subtitulo'] = Label(
        x=var.DIMENSION_PANTALLA[0]//2, 
        y=180,text=var.TEXTO_MENU_PRINCIPAL, 
        screen=form.get('pantalla'), 
        font_path=var.RUTA_FUENTE_SAIYAN_SANS, 
        font_size=55
        )
    
    form['boton_jugar'] = Button(
        x=var.DIMENSION_PANTALLA[0]//2, 
        y=370, text=var.BOTON_JUGAR, 
        screen=form.get('pantalla'), 
        font_path=var.RUTA_FUENTE_SAIYAN_SANS,
        color=var.COLOR_NARANJA, 
        font_size=44, 
        on_click=cambiar_formulario_on_click, 
        on_click_param='form_juego'
        )

    form['boton_ranking'] = Button(
        x=var.DIMENSION_PANTALLA[0]//2, 
        y=445, 
        text=var.BOTON_RANKING, 
        screen=form.get('pantalla'), 
        font_path=var.RUTA_FUENTE_SAIYAN_SANS,
        color=var.COLOR_NARANJA, 
        font_size=44, 
        on_click=cambiar_formulario_on_click, 
        on_click_param='form_ranking'
        )

    form['boton_opciones'] = Button(
        x=var.DIMENSION_PANTALLA[0]//2, 
        y=520, 
        text=var.BOTON_OPCIONES, 
        screen=form.get('pantalla'), 
        font_path=var.RUTA_FUENTE_SAIYAN_SANS,
        color=var.COLOR_NARANJA, 
        font_size=44, 
        on_click=cambiar_formulario_on_click, 
        on_click_param='form_opciones'
        )

    form['boton_salir'] = Button(
        x=var.DIMENSION_PANTALLA[0]//2, 
        y=595, 
        text=var.BOTON_SALIR, 
        screen=form.get('pantalla'), 
        font_path=var.RUTA_FUENTE_SAIYAN_SANS,
        color=var.COLOR_NARANJA, 
        font_size=44,
        on_click=click_salir, 
        on_click_param='boton_salir'
        )
    
    
    form['lista_objetos'] = [
        form.get('label_titulo'),
        form.get('label_subtitulo'), 
        form.get('boton_jugar'), 
        form.get('boton_ranking'),
        form.get('boton_opciones'), 
        form.get('boton_salir')
    ]
    
    form_base.forms_dict[dict_form_datos.get('nombre')] = form
    
    return form

def cambiar_formulario_on_click(parametro: str):
    """
    Maneja el cambio de formulario al hacer clic en un botón.
    Si es el formulario de juego, reinicia el nivel antes de activarlo.
    
    Args:
        parametro (str): Nombre del formulario a activar
    """
    form_juego = form_base.forms_dict[parametro]
    if parametro == "form_juego":
        nivel_cartas.reiniciar_nivel(form_juego.get("nivel"))
       
    form_base.activar_form(parametro)

def click_salir(parametro: str):
    """
    Maneja el evento de clic en el botón salir y cierra la aplicación.
    
    Args:
        parametro (str): Parámetro pasado al hacer clic
    """
    print(parametro)
    sys.exit()

def dibujar(dict_form_datos: dict):
    """
    Dibuja el formulario del menú principal.
    
    Args:
        dict_form_datos (dict): Diccionario del formulario con todos los componentes
    """
    form_base.dibujar(dict_form_datos)

def actualizar(dict_form_datos: dict):
    """
    Actualiza el estado del formulario del menú principal.
    
    Args:
        dict_form_datos (dict): Diccionario del formulario a actualizar
    """
    form_base.actualizar(dict_form_datos)

def activar_musica(dict_form_datos: dict, form_manager: dict):
    """
    Activa la música asociada al formulario del menú principal.
    
    Args:
        dict_form_datos (dict): Diccionario del formulario con la ruta de música
        form_manager (dict): Diccionario del gestor de formularios para manejar la música
    """
    form_base.activar_musica(dict_form_datos, form_manager)

