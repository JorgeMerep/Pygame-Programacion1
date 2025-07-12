import pygame 
import modulos.variables as var

forms_dict = {}

def crear_form_base(dict_form_datos: dict) -> dict:
    """
    Crea un formulario base con todos los componentes necesarios.
    
    Args:
        dict_form_datos (dict): Diccionario con los datos del formulario que debe contener:
            - form_manager_ref: Referencia al gestor de formularios
            - nombre: Nombre del formulario
            - pantalla: Superficie de la pantalla
            - activo: Estado activo del formulario
            - coords: Tupla con coordenadas (x, y)
            - numero_nivel: Número del nivel
            - ruta_musica: Ruta del archivo de música
            - ruta_fondo: Ruta de la imagen de fondo
            - dimension_pantalla: Dimensiones de la pantalla
    
    Returns:
        dict: Diccionario con el formulario creado conteniendo superficie, rectángulo y propiedades
    """
    form = {}
    form['form_manager_ref'] = dict_form_datos.get('form_manager_ref')
    form['nombre'] = dict_form_datos.get('nombre')
    form['pantalla'] = dict_form_datos.get('pantalla')
    form['activo'] = dict_form_datos.get('activo')
    form['x_coord'] = dict_form_datos.get('coords')[0]
    form['y_coord'] = dict_form_datos.get('coords')[1]
    form['numero_nivel'] = dict_form_datos.get('numero_nivel')
    form['ruta_musica'] = dict_form_datos.get('ruta_musica')
    form['superficie'] = pygame.image.load(dict_form_datos.get('ruta_fondo')).convert_alpha()
    form['superficie'] = pygame.transform.scale(form.get('superficie'), dict_form_datos.get('dimension_pantalla'))
    
    form['rectangulo'] = form.get('superficie').get_rect()
    form['rectangulo'].x = dict_form_datos.get('coords')[0]
    form['rectangulo'].y = dict_form_datos.get('coords')[1]

    return form

def activar_form(nombre: str):
    """
    Activa un formulario específico y desactiva todos los demás.
    
    Args:
        nombre (str): Nombre del formulario a activar
    """
    for form in forms_dict.values():
        form['activo'] = False
    forms_dict[nombre]['activo'] = True

def actualizar_objetos(dict_form_datos: dict):
    """
    Actualiza todos los objetos contenidos en el formulario.
    
    Args:
        dict_form_datos (dict): Diccionario del formulario que debe contener 'lista_objetos'
    """
    for objeto in dict_form_datos.get('lista_objetos'):
        objeto.update()

def dibujar_objetos(dict_form_datos: dict):
    """
    Dibuja todos los objetos contenidos en el formulario.
    
    Args:
        dict_form_datos (dict): Diccionario del formulario que debe contener 'lista_objetos'
    """
    for objeto in dict_form_datos.get('lista_objetos'):
        objeto.draw()

def dibujar(dict_form_datos: dict):
    """
    Dibuja el formulario completo en la pantalla incluyendo su superficie y objetos.
    
    Args:
        dict_form_datos (dict): Diccionario del formulario con pantalla, superficie y rectángulo
    """
    dict_form_datos['pantalla'].blit(dict_form_datos.get('superficie'), dict_form_datos.get('rectangulo'))
    dibujar_objetos(dict_form_datos)

def actualizar(dict_form_datos: dict):
    """
    Actualiza el estado del formulario, principalmente sus objetos.
    
    Args:
        dict_form_datos (dict): Diccionario del formulario a actualizar
    """
    actualizar_objetos(dict_form_datos)

def reproducir_musica(ruta: str, form_manager: dict, forzar: bool = False):
    """
    Reproduce música de fondo si está habilitada y si ya no se está reproduciendo.
    
    Args:
        ruta (str): Ruta del archivo de música a reproducir
        form_manager (dict): Diccionario del gestor de formularios con configuración de música
        forzar (bool, optional): Si True, fuerza la reproducción aunque ya se esté reproduciendo. Por defecto False.
    """
    if not form_manager.get('musica_habilitada'):
        return  # No reproducir música si está deshabilitada por mas que cambies de formulario
    
    musica_actual = form_manager.get('musica_actual')
    if musica_actual != ruta or forzar:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(ruta)
        pygame.mixer.music.set_volume(var.VOL_MUSICA_MINIMO)
        pygame.mixer.music.play(-1)
        form_manager['musica_actual'] = ruta

def activar_musica(dict_form_datos: dict, form_manager: dict):
    """
    Activa la música asociada al formulario si tiene una ruta de música definida.
    
    Args:
        dict_form_datos (dict): Diccionario del formulario que debe contener 'ruta_musica'
        form_manager (dict): Diccionario del gestor de formularios para manejar la música
    """
    ruta_musica = dict_form_datos.get('ruta_musica')
    if ruta_musica:
        reproducir_musica(ruta_musica, form_manager)






