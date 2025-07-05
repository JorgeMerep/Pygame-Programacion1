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


def generar_bd(root_path_cards: str):
        
    carta_dict = {}

    for root, dir, files in os.walk(root_path_cards, topdown=True):
        reverse_path = ''
        deck_cards = []
        deck_name = root.split('\\')[-1]
        deck_name = deck_name.split('/')[-1]
        
        for file in files:
            path_card = os.path.join(root, file)
            path_card = path_card.replace('\\' , '/')
            
            if 'reverse' in path_card.lower():
                reverse_path = path_card
            else:
                file = file.replace('\\', '/')
                name_without_ext = file.split('/')[-1].split('.png')[0]
                parts = name_without_ext.split('_')

                # Validación estricta: buscamos exactamente este patrón
                if len(parts) == 8 and parts[1] == 'HP' and parts[3] == 'ATK' and parts[5] == 'DEF':
                    vida = int(parts[2])
                    ataque = int(parts[4])
                    defensa = int(parts[6])
                    bonus = int(parts[-1])

                    card = {
                        'hp': vida,
                        'atk': ataque,
                        'def': defensa,
                        'bonus': bonus,
                        'path_imagen_frente': path_card
                    }

                    deck_cards.append(card)  #SOLO si la carta es válida
        
        for index_card in range(len(deck_cards)):
            deck_cards[index_card]['path_imagen_reverso'] = reverse_path
        
        carta_dict[deck_name] = deck_cards

    return carta_dict


def achicar_imagen_carta(path_imagen: str, porcentaje: int):
    imagen_raw = pygame.image.load(path_imagen)
    alto = int(imagen_raw.get_height() * float(f'0.{porcentaje}'))
    ancho = int(imagen_raw.get_width() * float(f'0.{porcentaje}'))
    imagen_final = pygame.transform.scale(imagen_raw, (ancho, alto))
    return imagen_final