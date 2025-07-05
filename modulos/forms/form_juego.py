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

    
    
    
    form['reloj'] = pygame.time.Clock()
    form['first_last_timer'] = pygame.time.get_ticks()
    form['bonus_1_used'] = False
    form['bonus_2_used'] = False
    
   
    
    
    form['lista_objetos'] = [
        
    ]
    
    form_base.forms_dict[dict_form_datos.get('nombre')] = form
    
    return form

def dibujar(dict_form_datos: dict):
    form_base.dibujar(dict_form_datos)
    nivel_cartas.dibujar_cartas(nivel_data=dict_form_datos.get("nivel"))

def actualizar(dict_form_datos: dict, lista_eventos: list[pygame.event.Event]):
    form_base.actualizar(dict_form_datos)
    nivel_cartas.actualizar_cartas(nivel_data=dict_form_datos.get("nivel"), cola_eventos=lista_eventos)

def activar_musica(dict_form_datos: dict, form_manager: dict):
    form_base.activar_musica(dict_form_datos, form_manager)