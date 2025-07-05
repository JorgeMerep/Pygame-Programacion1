import pygame
import modulos.forms.form_base as form_base
import modulos.variables as var
import modulos.nivel_cartas as nivel_cartas
from utn_fra.pygame_widgets import (
Label,Button
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
    font_path=var.RUTA_FUENTE_SAIYAN_SANS,
    font_size=30,
    )

    form["label_atk_jugador"] = Label(
        x=140,
        y=540,
        text=f"ATK: {form['nivel'].get('atk_total_jugador', 0)}",
        screen=form.get('pantalla'),
        font_path=var.RUTA_FUENTE_SAIYAN_SANS,
        font_size=20,
    )

    form["label_def_jugador"] = Label(
    x=140,
    y=560,
    text=f"DEF: {form['nivel'].get('def_total_jugador', 0)}",
    screen=form.get('pantalla'),
    font_path=var.RUTA_FUENTE_SAIYAN_SANS,
    font_size=20,
    )

    form["label_hp_enemigo"] = Label(
        x=140, 
        y=190,
        text=f"HP: {form['nivel'].get('hp_total_enemigo', 0)}",
        screen=form.get('pantalla'), 
        font_path=var.RUTA_FUENTE_SAIYAN_SANS, 
        font_size=30)
    
    form["label_atk_enemigo"] = Label(
        x=140, 
        y=210,
        text=f"ATK: {form['nivel'].get('atk_total_enemigo', 0)}",
        screen=form.get('pantalla'), 
        font_path=var.RUTA_FUENTE_SAIYAN_SANS, 
        font_size=20)
    
    form["label_def_enemigo"] = Label(
        x=140, 
        y=230,
        text=f"DEF: {form['nivel'].get('def_total_enemigo', 0)}",
        screen=form.get('pantalla'), 
        font_path=var.RUTA_FUENTE_SAIYAN_SANS, 
        font_size=20)

   
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
        form.get("label_def_enemigo")     
    ]
    
    form_base.forms_dict[dict_form_datos.get('nombre')] = form
    
    return form

def dibujar(dict_form_datos: dict):
    form_base.dibujar(dict_form_datos)

    print(dict_form_datos.get('lista_objetos'))

    nivel_cartas.dibujar_cartas(nivel_data=dict_form_datos.get("nivel"))

def actualizar(dict_form_datos: dict, lista_eventos: list[pygame.event.Event]):
    form_base.actualizar(dict_form_datos)

    dict_form_datos['label_hp_jugador'].update_text(
    f'HP: {dict_form_datos.get("nivel").get("hp_total_jugador")}', 
    (255, 0, 0)
)

    nivel_cartas.actualizar_cartas(nivel_data=dict_form_datos.get("nivel"), cola_eventos=lista_eventos)

def activar_musica(dict_form_datos: dict, form_manager: dict):
    form_base.activar_musica(dict_form_datos, form_manager)
