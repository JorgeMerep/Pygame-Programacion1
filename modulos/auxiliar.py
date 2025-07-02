import modulos.variables as var
import pygame
import json
import os

def parsear_entero(valor: str):
    if valor.isdigit():
        return int(valor)
    return valor

def mapear_valores(matriz: list[list], indice_a_aplicar: int, callback_parseo_entero):
    
    for indice_fila in range(len(matriz)):
        valor = matriz[indice_fila][indice_a_aplicar]
        matriz[indice_fila][indice_a_aplicar] = callback_parseo_entero(valor)

def cargar_ranking():
    ranking = []
    with open(var.RUTA_RANKING_CSV, 'r', encoding='utf-8') as file:
        lineas = file.read()
        for linea in lineas.split('\n'):
            if linea:
                ranking.append(linea.split(','))
    mapear_valores(ranking, 1, parsear_entero)
    ranking.sort(key=lambda fila: fila[1], reverse=True)
    
    return ranking

def cargar_configs(path: str) -> dict:
    configuraciones = {}
    with open(path, 'r', encoding='utf-8') as file:
        configuraciones = json.load(file)

    return configuraciones


def listar_cartas_y_reverso(root: str, files: list) -> tuple[list[dict], str]:

    """
    Recibe la ruta y lista de archivos de un mazo y crea la lista de cartas con sus paths de imagen frontal.
    Detecta y retorna el path del reverso del mazo.
    Hace un split del len del nombre del archivo para obtener los datos de HP, ATK, DEF

    Args:
    root: str
    files: list

    Return:
    tuple que contiene una list(dict-de cartas-) y str(el path de la imagen del reverse del mazo de cartas)

    """
    deck_cards: list[dict] = []
    reverse_path: str = ''
    deck_name: str = os.path.basename(root)

    for file in files:
        path_card = os.path.join(root, file)

        if 'reverse' in path_card.lower():
            reverse_path = path_card
            continue

        file = file.replace('\\', '/')
        filename = os.path.basename(file)
        name_without_ext = filename.split('.')[0]

        parts = name_without_ext.split('_')

        # Validación estricta: buscamos exactamente este patrón
        if len(parts) == 8 and parts[1] == 'HP' and parts[3] == 'ATK' and parts[5] == 'DEF':
            vida = int(parts[2])
            ataque = int(parts[4])
            defensa = int(parts[6])

            card = {
                'id': f'{deck_name}-{name_without_ext}',
                'hp': vida,
                'atk': ataque,
                'def': defensa,
                'path_imagen_frente': path_card
            }

            deck_cards.append(card)
        else:
            print(f"Formato inválido en archivo: {filename}")

    return deck_cards, reverse_path

def asignar_reverso_a_cartas(cartas: list, reverso_path: str):

    """
    Añade la imagen de reverso a todas las cartas del mazo.

    """
    for carta in cartas:
        carta['path_imagen_reverso'] = reverso_path

def generar_bd(root_path_cards: str):

    """
    Recorre toda la ruta de carpetas, genera cada mazo con sus cartas y arma el diccionario final de cartas.
    
    """
    carta_dict = {"cartas": {}}

    for root, files in os.walk(root_path_cards, topdown=True):
        deck_name = root.split('\\')[-1]
        cartas, reverso = listar_cartas_y_reverso(root, files)
        asignar_reverso_a_cartas(cartas, reverso)
        carta_dict['cartas'][deck_name] = cartas

    return carta_dict

def achicar_imagen_card(path_imagen: str, porcentaje: int):
    imagen_raw = pygame.image.load(path_imagen)
    alto = int(imagen_raw.get_height() * float(f'0.{porcentaje}'))
    ancho = int(imagen_raw.get_width() * float(f'0.{porcentaje}'))
    imagen_final = pygame.transform.scale(imagen_raw, (ancho, alto))
    return imagen_final