import modulos.forms.form_base as form_base
import modulos.variables as var
import modulos.auxiliar as aux
from utn_fra.pygame_widgets import (
    Button, Label
)


def iniciar_form_ranking(dict_form_datos: dict, jugador: dict):
    """
    Inicializa el formulario de ranking con todos sus componentes.
    
    Args:
        dict_form_datos (dict): Diccionario con los datos base del formulario
        jugador (dict): Diccionario con los datos del jugador
    
    Returns:
        dict: Diccionario del formulario creado con todos los componentes de ranking
    """
    form = form_base.crear_form_base(dict_form_datos)    
    
    form['jugador'] = jugador
    
    form['pantalla_ranking'] = []
    form['lista_ranking'] = []
    
    form['label_titulo'] = Label(
        x=var.DIMENSION_PANTALLA[0]//2, 
        y=var.DIMENSION_PANTALLA[1]//2 - 250,
        text=var.TITULO_JUEGO, 
        screen=form.get('pantalla'), 
        font_path=var.RUTA_FUENTE_SAIYAN_SANS, 
        font_size=60)

    form['label_subtitulo'] = Label(
        x=var.DIMENSION_PANTALLA[0]//2 + 50, 
        y=var.DIMENSION_PANTALLA[1]//2 - 165,
        text=var.TEXTO_RANKING, 
        screen=form.get('pantalla'), 
        font_path=var.RUTA_FUENTE_SAIYAN_SANS, 
        font_size=55, 
        color=var.COLOR_NARANJA)
    
    form['boton_volver'] = Button(
        x=var.DIMENSION_PANTALLA[0]//2, 
        y=var.DIMENSION_PANTALLA[1]//2 + 255, 
        text=var.BOTON_VOLVER_MENU, 
        screen=form.get('pantalla'), 
        font_path=var.RUTA_FUENTE_SAIYAN_SANS, 
        color=var.COLOR_NARANJA, 
        font_size=44, 
        on_click=click_volver_menu, 
        on_click_param='form_menu')
    
    form['lista_objetos'] = [
        form.get('label_titulo'), 
        form.get('label_subtitulo'),
        form.get('boton_volver')
    ]
    
    form_base.forms_dict[dict_form_datos.get('nombre')] = form
    
    return form


def click_volver_menu(parametro: str):
    """
    Maneja el evento de clic en el botón volver al menú.
    
    Args:
        parametro (str): Nombre del formulario a activar
    """
    form_base.activar_form(parametro)


def iniciar_ranking(dict_form_datos: dict):
    """
    Inicializa la visualización del ranking creando labels para cada entrada.
    Muestra el número de posición, nombre y puntaje de cada jugador.
    
    Args:
        dict_form_datos (dict): Diccionario del formulario con la lista de ranking
    """
    dict_form_datos['pantalla_ranking'] = []
    matriz = dict_form_datos.get('lista_ranking')
    for indice_fila in range(len(matriz)):
        
        fila = matriz[indice_fila]
        
        """
        1                   fulano              20
        2                   mengano             15
        """
        
        # numero
        dict_form_datos['pantalla_ranking'].append(
            Label(x=var.DIMENSION_PANTALLA[0]//2 - 220, y=var.DIMENSION_PANTALLA[1]//2.9+indice_fila*31,text=f'{indice_fila + 1}', screen=dict_form_datos.get('pantalla'), font_path=var.RUTA_FUENTE_ALAGARD, color=var.COLOR_NARANJA, font_size=40)
        )
        
        # nombre
        dict_form_datos['pantalla_ranking'].append(
            Label(x=var.DIMENSION_PANTALLA[0]//2, y=var.DIMENSION_PANTALLA[1]//2.9+indice_fila*31,text=f'{fila[0]}', screen=dict_form_datos.get('pantalla'), font_path=var.RUTA_FUENTE_ALAGARD, color=var.COLOR_NARANJA, font_size=40)
        )
        
        # puntaje
        dict_form_datos['pantalla_ranking'].append(
            Label(x=var.DIMENSION_PANTALLA[0]//2 + 220, y=var.DIMENSION_PANTALLA[1]//2.9+indice_fila*31,text=f'{fila[1]}', screen=dict_form_datos.get('pantalla'), font_path=var.RUTA_FUENTE_ALAGARD, color=var.COLOR_NARANJA, font_size=40)
        )
    
    
def inicializar_ranking(dict_form_datos: dict):
    """
    Inicializa el ranking cargando los datos desde el archivo y limitando a 10 entradas.
    
    Args:
        dict_form_datos (dict): Diccionario del formulario donde se almacenará el ranking
    """
    dict_form_datos['lista_ranking'] = aux.cargar_ranking()[:10]
    iniciar_ranking(dict_form_datos)

def dibujar(dict_form_datos: dict):
    """
    Dibuja el formulario de ranking incluyendo todos los labels del ranking.
    
    Args:
        dict_form_datos (dict): Diccionario del formulario con todos los componentes
    """
    form_base.dibujar(dict_form_datos)
    for label in dict_form_datos.get('pantalla_ranking'):
        label.draw()

def actualizar(dict_form_datos: dict):
    """
    Actualiza el formulario de ranking. Si está activo, reinicializa el ranking.
    
    Args:
        dict_form_datos (dict): Diccionario del formulario a actualizar
    """
    if dict_form_datos.get('activo'):
        inicializar_ranking(dict_form_datos)
    form_base.actualizar(dict_form_datos)

def activar_musica(dict_form_datos: dict, form_manager: dict):
    """
    Activa la música asociada al formulario de ranking.
    
    Args:
        dict_form_datos (dict): Diccionario del formulario con la ruta de música
        form_manager (dict): Diccionario del gestor de formularios para manejar la música
    """
    form_base.activar_musica(dict_form_datos, form_manager)
