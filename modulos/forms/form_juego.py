import pygame
import modulos.forms.form_base as form_base
import modulos.variables as var
import modulos.nivel_cartas as nivel_cartas
from utn_fra.pygame_widgets import (
Label,ButtonImageSound
)

def iniciar_form_juego(dict_form_datos: dict, jugador: dict, enemigo: dict):
    form = form_base.crear_form_base(dict_form_datos)
    
    form['jugador'] = jugador
    form['enemigo'] = enemigo

    form["nivel"] = nivel_cartas.inicializar_nivel_cartas(form.get("jugador"), form.get("enemigo"), form.get("pantalla"),form.get("numero_nivel"))

    nivel_cartas.inicializar_data_nivel(form["nivel"]) #Carga la data del nivel y genera los mazos

    form["label_hp_jugador"] = Label(
    x=140,
    y=520,
    text=f"HP: {form['nivel'].get('hp_total_jugador', 0)}",
    screen=form.get('pantalla'),
    font_path=var.RUTA_FUENTE_ALAGARD,
    font_size=30,
    )

    form["label_atk_jugador"] = Label(
        x=140,
        y=540,
        text=f"ATK: {form['nivel'].get('atk_total_jugador', 0)}",
        screen=form.get('pantalla'),
        font_path=var.RUTA_FUENTE_ALAGARD,
        font_size=20,
    )

    form["label_def_jugador"] = Label(
    x=140,
    y=560,
    text=f"DEF: {form['nivel'].get('def_total_jugador', 0)}",
    screen=form.get('pantalla'),
    font_path=var.RUTA_FUENTE_ALAGARD,
    font_size=20,
    )

    form["label_hp_enemigo"] = Label(
        x=140, 
        y=190,
        text=f"HP: {form['nivel'].get('hp_total_enemigo', 0)}",
        screen=form.get('pantalla'), 
        font_path=var.RUTA_FUENTE_ALAGARD, 
        font_size=30)
    
    form["label_atk_enemigo"] = Label(
        x=140, 
        y=210,
        text=f"ATK: {form['nivel'].get('atk_total_enemigo', 0)}",
        screen=form.get('pantalla'), 
        font_path=var.RUTA_FUENTE_ALAGARD, 
        font_size=20)
    
    form["label_def_enemigo"] = Label(
        x=140, 
        y=230,
        text=f"DEF: {form['nivel'].get('def_total_enemigo', 0)}",
        screen=form.get('pantalla'), 
        font_path=var.RUTA_FUENTE_ALAGARD, 
        font_size=20)
    
    form["label_puntaje_partida"] = Label(
    x=150,
    y=50,
    text=f"PUNTAJE: {form['jugador'].get('puntaje_actual', 0)} - {form['enemigo'].get('puntaje_actual', 0)}",
    screen=form.get('pantalla'),
    font_path=var.RUTA_FUENTE_ALAGARD,
    font_size=40,
    )

    form["label_timer"] = Label(
    x=1150,
    y=50,
    text=f"TIMER: {form['nivel'].get('timer_partida', 0)}",
    screen=form.get('pantalla'),
    font_path=var.RUTA_FUENTE_ALAGARD,
    font_size=40,
    )
    
    form["boton_jugar"] = ButtonImageSound(
        x=1200, 
        y=385,
        width= 130,
        height= 50, 
        text= "", 
        screen=form.get('pantalla'),
        image_path= var.RUTA_IMAGEBUTTON_JUGAR,
        sound_path= var.SONIDO_JUGAR,
        font_size= "", 
        on_click= click_jugar_partida, 
        on_click_param= form.get("nivel"))
    
    form["boton_heal"] = ButtonImageSound(
        x=1200, 
        y=570,
        width= 130,
        height= 45, 
        text= "", 
        screen=form.get('pantalla'),
        image_path= var.RUTA_IMAGEBUTTON_HEAL,
        sound_path= var.SONIDO_HEAL,
        font_size= "", 
        on_click= click_activar_buff_heal, 
        on_click_param= form.get("nivel"))
    
    form["boton_shield"] = ButtonImageSound(
        x=1200, 
        y=620,
        width= 130,
        height= 45, 
        text= "", 
        screen=form.get('pantalla'),
        image_path= var.RUTA_IMAGEBUTTON_SHIELD,
        sound_path= var.SONIDO_SHIELD,
        font_size= "", 
        on_click= click_activar_buff_shield, 
        on_click_param= form.get("nivel"))
    
    

   
    form['reloj'] = pygame.time.Clock()
    form['first_last_timer'] = pygame.time.get_ticks()
    form['bonus_1_used'] = False
    form['bonus_2_used'] = False
    
   
    
    
    form['lista_objetos'] = [
        form.get("label_hp_jugador"),
        form.get("label_atk_jugador"),
        form.get("label_def_jugador"),
        form.get("label_hp_enemigo"),
        form.get("label_atk_enemigo"),
        form.get("label_def_enemigo"),
        form.get("label_puntaje_partida"),
        form.get("label_timer"),
        form.get("boton_jugar"),
        form.get("boton_heal"),
        form.get("boton_shield"),   
    ]
    
    form_base.forms_dict[dict_form_datos.get('nombre')] = form
    
    return form

def dibujar(dict_form_datos: dict):
    form_base.dibujar(dict_form_datos)

    nivel_cartas.dibujar_cartas(nivel_data=dict_form_datos.get("nivel"))

def click_jugar_partida(parametro: dict):
    if not nivel_cartas.juego_terminado(parametro):
        nivel_cartas.jugar_partida(parametro)

       
def actualizar(dict_form_datos: dict):
    form_base.actualizar(dict_form_datos)

    nivel_cartas.actualizar_cartas(nivel_data=dict_form_datos.get("nivel"))

    actualizar_timer(dict_form_datos)

    dict_form_datos['label_hp_jugador'].update_text(f'HP: {dict_form_datos.get("nivel").get("hp_total_jugador")}',
    (255, 0, 0))

    dict_form_datos['label_def_jugador'].update_text(f'DEF: {dict_form_datos.get("nivel").get("def_total_jugador")}', (255, 0, 0))
    
    dict_form_datos['label_atk_jugador'].update_text(f'ATK: {dict_form_datos.get("nivel").get("atk_total_jugador")}', (255, 0, 0))

    dict_form_datos['label_hp_enemigo'].update_text(f'HP: {dict_form_datos.get("nivel").get("hp_total_enemigo")}', 
    (255, 0, 0))
    
    dict_form_datos['label_def_enemigo'].update_text(f'DEF: {dict_form_datos.get("nivel").get("def_total_enemigo")}', (255, 0, 0)) 
    
    dict_form_datos['label_atk_enemigo'].update_text(f'ATK: {dict_form_datos.get("nivel").get("atk_total_enemigo")}', (255, 0, 0))

    dict_form_datos['label_puntaje_partida'].update_text(f'PUNTAJE: {dict_form_datos.get('jugador').get('puntaje_actual', 0)} - {dict_form_datos.get('enemigo').get('puntaje_actual', 0)}', (255, 0, 0))

    dict_form_datos['label_timer'].update_text(f'TIMER: {dict_form_datos.get("nivel").get("timer_partida")}', 
    (255, 0, 0))

def actualizar_timer(dict_form_data: dict):
    if dict_form_data.get('nivel').get('timer_partida') > 0:
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - dict_form_data.get('first_last_timer') > 1000:
            dict_form_data.get('nivel')['timer_partida'] -= 1
            dict_form_data['first_last_timer'] = tiempo_actual

def activar_musica(dict_form_datos: dict, form_manager: dict):
    form_base.activar_musica(dict_form_datos, form_manager)

def click_activar_buff_heal(nivel_data: dict):
    nivel_cartas.activar_buff_heal(nivel_data)

def click_activar_buff_shield(nivel_data: dict):
    nivel_cartas.activar_buff_shield(nivel_data)

