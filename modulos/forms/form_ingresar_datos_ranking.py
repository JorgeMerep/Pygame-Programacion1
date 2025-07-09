import modulos.forms.form_base as form_base
import modulos.jugador as jugador_mod
import modulos.variables as var
import modulos.auxiliar as aux
from utn_fra.pygame_widgets import (
    Button, Label, TextBox
)

def iniciar_form_ingresar_datos_ranking(dict_form_datos: dict, jugador: dict):
    form = form_base.crear_form_base(dict_form_datos)
    form['jugador'] = jugador
    form['puntaje'] = jugador_mod.get_puntaje_total(form.get('jugador'))
    form['confirmar_nombre'] = False
    
    form['titulo'] = Label(
        x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 - 200,
        text=var.TITULO_JUEGO, screen=form.get('pantalla'), font_path=var.RUTA_FUENTE_ALAGARD, font_size=75
    )
    form['titulo_2'] = Label(
        x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 - 150,
        text='Ganaste!', screen=form.get('pantalla'), font_path=var.RUTA_FUENTE_ALAGARD, font_size=50, color=var.COLOR_NARANJA
    )
    form['subtitulo'] = Label(
        x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 - 90,
        text='ESCRIBE TU NOMBRE', screen=form.get('pantalla'), font_path=var.RUTA_FUENTE_ALAGARD, font_size=50, color=var.COLOR_ROJO
    )
    form['subtitulo_puntaje'] = Label(
        x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 - 20,
        text=f'Score: {form.get("puntaje")}', screen=form.get('pantalla'), font_path=var.RUTA_FUENTE_ALAGARD, font_size=30, color=var.COLOR_NARANJA
    )
    
    form['text_box'] = TextBox(
        x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 + 40,
        text='____' ,screen=form.get('pantalla'), font_path=var.RUTA_FUENTE_ALAGARD,
        font_size=25, color=var.COLOR_NARANJA
    )
    
    form['boton_confirmar_nombre'] = Button(
        x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 + 100,
        text="CONFIRMAR NOMBRE", screen=form.get('pantalla'), 
        font_path=var.RUTA_FUENTE_ALAGARD, 
        on_click=click_confirmar_nombre, on_click_param=form
    )
    
    form['lista_objetos'] = [
        form.get('titulo'),form.get('titulo_2'),form.get('subtitulo'),form.get('subtitulo_puntaje'),
        form.get('boton_confirmar_nombre')
    ]
    
    form_base.forms_dict[dict_form_datos.get('nombre')] = form
    return form

def click_confirmar_nombre(dict_form_datos: dict):
    dict_form_datos['confirmar_nombre'] = True
    jugador_mod.set_nombre(
        dict_form_datos.get('jugador'), 
        dict_form_datos.get('writing_text').text
    )

    aux.guardar_ranking(dict_form_datos.get('jugador'))
    form_base.activar_form('form_ranking')

def dibujar(dict_form_datos: dict):
    form_base.dibujar(dict_form_datos)
    
    dict_form_datos.get('text_box').draw()
    
    dict_form_datos['writing_text'] = Label(
        x=var.DIMENSION_PANTALLA[0] // 2, 
        y=var.DIMENSION_PANTALLA[1] // 2 + 30,
        text=f'{dict_form_datos.get("text_box").writing.upper()}',
        screen=dict_form_datos.get('pantalla'), 
        font_path=var.RUTA_FUENTE_ALAGARD,
        font_size=30, 
        color=var.COLOR_NARANJA
    )
    
    dict_form_datos.get('writing_text').draw()

def actualizar(dict_form_datos: dict, lista_eventos: list):
    dict_form_datos['puntaje'] = jugador_mod.get_puntaje_total(dict_form_datos.get('jugador'))
    dict_form_datos.get('lista_objetos')[3].update_text(f'PUNTAJE: {dict_form_datos.get("puntaje")}', var.COLOR_NARANJA)
    dict_form_datos.get('text_box').update(lista_eventos)
    form_base.actualizar(dict_form_datos)

def activar_musica(dict_form_datos: dict, form_manager: dict):
    form_base.activar_musica(dict_form_datos, form_manager)