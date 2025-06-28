import pygame as pygame
import modulos.forms.form_base as form_base
import modulos.variables as var
import modulos.auxiliar as aux
from utn_fra.pygame_widgets import (
    Button, Label
)


def iniciar_form_ranking(dict_form_datos: dict, jugador: dict):
    form = form_base.crear_form_base(dict_form_datos)    
    
    form['jugador'] = jugador
    
    form['pantalla_ranking'] = []
    form['lista_ranking'] = []
    
    form['label_titulo'] = Label(x=var.DIMENSION_PANTALLA[0]//2, y=var.DIMENSION_PANTALLA[1]//2 - 250,text=var.TITULO_JUEGO, screen=form.get('pantalla'), font_path=var.RUTA_FUENTE_SAIYAN_SANS, font_size=60)

    form['label_subtitulo'] = Label(x=var.DIMENSION_PANTALLA[0]//2 + 50, y=var.DIMENSION_PANTALLA[1]//2 - 165,text=var.TEXTO_RANKING, screen=form.get('pantalla'), font_path=var.RUTA_FUENTE_SAIYAN_SANS, font_size=55, color=var.COLOR_NARANJA)
    
    form['boton_volver'] = Button(x=var.DIMENSION_PANTALLA[0]//2, y=var.DIMENSION_PANTALLA[1]//2 + 255, text=var.BOTON_VOLVER_MENU, screen=form.get('pantalla'), font_path=var.RUTA_FUENTE_SAIYAN_SANS, color=var.COLOR_NARANJA, font_size=44, on_click=click_volver_menu, on_click_param='form_menu')
    
    form['lista_objetos'] = [
        form.get('label_titulo'), 
        form.get('label_subtitulo'),
        form.get('boton_volver')
    ]
    
    form_base.forms_dict[dict_form_datos.get('nombre')] = form
    
    return form


def click_volver_menu(parametro: str):
    form_base.activar_form(parametro)


def iniciar_ranking(dict_form_datos: dict):
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
    dict_form_datos['lista_ranking'] = aux.cargar_ranking()[:10]
    iniciar_ranking(dict_form_datos)

def dibujar(dict_form_datos: dict):
    form_base.dibujar(dict_form_datos)
    for label in dict_form_datos.get('pantalla_ranking'):
        label.draw()

def actualizar(dict_form_datos: dict):
    
    if dict_form_datos.get('activo'):
        inicializar_ranking(dict_form_datos)
    form_base.actualizar(dict_form_datos)