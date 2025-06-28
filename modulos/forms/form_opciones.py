import pygame as pygame
import modulos.forms.form_base as form_base
import modulos.variables as var
from utn_fra.pygame_widgets import (
    Button, Label
)

def iniciar_form_opciones(dict_form_datos: dict):
    form = form_base.crear_form_base(dict_form_datos)
    
    form['label_titulo'] = Label(x=var.DIMENSION_PANTALLA[0]//2, y=100,text=var.TITULO_JUEGO, screen=form.get('pantalla'), font_path=var.RUTA_FUENTE_SAIYAN_SANS, font_size=60)

    form['label_subtitulo'] = Label(x=var.DIMENSION_PANTALLA[0]//2, y=180,text=var.TEXTO_OPCIONES, screen=form.get('pantalla'), font_path=var.RUTA_FUENTE_SAIYAN_SANS, font_size=55)

    form['boton_musica_on'] = Button(x=var.DIMENSION_PANTALLA[0]//2, y=320, text=var.BOTON_MUSICA_ON, screen=form.get('pantalla'), font_path=var.RUTA_FUENTE_SAIYAN_SANS, color=var.COLOR_NARANJA, font_size=44, on_click="", on_click_param='')

    form['boton_musica_off'] = Button(x=var.DIMENSION_PANTALLA[0]//2, y=395, text=var.BOTON_MUSICA_OFF, screen=form.get('pantalla'), font_path=var.RUTA_FUENTE_SAIYAN_SANS, color=var.COLOR_NARANJA, font_size=44, on_click="", on_click_param='')
    
    form['boton_volver'] = Button(x=var.DIMENSION_PANTALLA[0]//2, y=595, text=var.BOTON_VOLVER_MENU, screen=form.get('pantalla'), font_path=var.RUTA_FUENTE_SAIYAN_SANS, color=var.COLOR_NARANJA, font_size=55, on_click=click_volver, on_click_param='form_menu')
    
    
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
    form_base.activar_form(parametro)

def dibujar(dict_form_datos: dict):
    form_base.dibujar(dict_form_datos)

def actualizar(dict_form_datos: dict):
    form_base.actualizar(dict_form_datos)
