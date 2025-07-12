import modulos.variables as var
import pygame
import json
import os

def parsear_entero(valor: str):
    """
    Convierte una cadena a entero si es un dígito, de lo contrario devuelve el valor original.
    
    Args:
        valor (str): Cadena a convertir
    
    Returns:
        int | str: El valor convertido a entero si es posible, de lo contrario la cadena original
    """
    if valor.isdigit():
        return int(valor)
    return valor

def mapear_valores(matriz: list[list], indice_a_aplicar: int, callback_parseo_entero):
    """
    Aplica una función callback a todos los valores de una columna específica en una matriz.
    
    Args:
        matriz (list[list]): Matriz de datos donde aplicar la función
        indice_a_aplicar (int): Índice de la columna a procesar
        callback_parseo_entero: Función callback a aplicar a cada valor
    """
    for indice_fila in range(len(matriz)):
        valor = matriz[indice_fila][indice_a_aplicar]
        matriz[indice_fila][indice_a_aplicar] = callback_parseo_entero(valor)

def cargar_ranking():
    """
    Carga el ranking desde un archivo CSV, parsea los puntajes y ordena por puntaje descendente.
    
    Returns:
        list: Lista de listas con [nombre, puntaje] ordenada por puntaje descendente
    """
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
    """
    Carga configuraciones desde un archivo JSON.
    
    Args:
        path (str): Ruta del archivo JSON con las configuraciones
    
    Returns:
        dict: Diccionario con las configuraciones cargadas
    """
    configuraciones = {}
    with open(path, 'r', encoding='utf-8') as file:
        configuraciones = json.load(file)

    return configuraciones

def generar_bd(root_path_cards: str):
    """
    Genera una base de datos de cartas recorriendo directorios y procesando archivos de imagen.
    Extrae información de las cartas desde los nombres de archivo con formato específico.
    
    Args:
        root_path_cards (str): Ruta raíz donde se encuentran los directorios con cartas
    
    Returns:
        dict: Diccionario con mazos de cartas organizados por nombre de directorio
    """
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

                # Validación estricta: solo exactamente este patrón
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
    """
    Reduce el tamaño de una imagen de carta según un porcentaje especificado.
    
    Args:
        path_imagen (str): Ruta de la imagen a redimensionar
        porcentaje (int): Porcentaje de reducción (ej: 50 para reducir al 50%)
    
    Returns:
        pygame.Surface: Imagen redimensionada
    """
    imagen_raw = pygame.image.load(path_imagen)
    alto = int(imagen_raw.get_height() * float(f'0.{porcentaje}'))
    ancho = int(imagen_raw.get_width() * float(f'0.{porcentaje}'))
    imagen_final = pygame.transform.scale(imagen_raw, (ancho, alto))
    return imagen_final

def guardar_ranking(jugador_dict: dict):
    """
    Guarda los datos del jugador en el archivo de ranking CSV.
    
    Args:
        jugador_dict (dict): Diccionario del jugador que debe contener 'nombre' y 'puntaje_actual'
    """
    with open(var.RUTA_RANKING_CSV, 'a', encoding='utf-8') as file:
        data = f'{jugador_dict.get("nombre")},{jugador_dict.get("puntaje_actual")}\n'
        file.write(data)
