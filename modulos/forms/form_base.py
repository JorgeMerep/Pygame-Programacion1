import pygame 

forms_dict = {}

def crear_form_base(dict_form_datos: dict) -> dict:
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
    for form in forms_dict.values():
        form['activo'] = False
    forms_dict[nombre]['activo'] = True

def actualizar_objetos(dict_form_datos: dict):
    for objeto in dict_form_datos.get('lista_objetos'):
        objeto.update()

def dibujar_objetos(dict_form_datos: dict):
    for objeto in dict_form_datos.get('lista_objetos'):
        objeto.draw()

def dibujar(dict_form_datos: dict):
    dict_form_datos['pantalla'].blit(dict_form_datos.get('superficie'), dict_form_datos.get('rectangulo'))
    dibujar_objetos(dict_form_datos)

def actualizar(dict_form_datos: dict):
    actualizar_objetos(dict_form_datos)

def reproducir_musica(ruta: str, form_manager: dict, forzar: bool = False):
    if not form_manager.get('musica_habilitada'):
        return  # No reproducir música si está deshabilitada por mas que cambies de formulario
    
    musica_actual = form_manager.get('musica_actual')
    if musica_actual != ruta or forzar:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(ruta)
        pygame.mixer.music.play(-1)
        form_manager['musica_actual'] = ruta

def activar_musica(dict_form_datos: dict, form_manager: dict):
    ruta_musica = dict_form_datos.get('ruta_musica')
    if ruta_musica:
        reproducir_musica(ruta_musica, form_manager)




    
    
