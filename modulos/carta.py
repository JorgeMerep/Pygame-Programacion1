import pygame  
import modulos.auxiliar as aux


def inicializar_carta(carta_dict: dict, coordenadas: tuple[int,int]) -> dict:
    """
    Inicializa una carta con todos sus atributos y propiedades visuales.
    
    Args:
        carta_dict (dict): Diccionario con los datos base de la carta (hp, atk, def, bonus, paths de imágenes)
        coordenadas (tuple[int,int]): Tupla con las coordenadas (x, y) donde posicionar la carta
    
    Returns:
        dict: Diccionario completo de la carta con imágenes cargadas y rectángulos posicionados
    """
    carta_dict_final = {}

    carta_dict_final['hp'] = carta_dict.get('hp')
    carta_dict_final['atk'] = carta_dict.get('atk')
    carta_dict_final['def'] = carta_dict.get('def')
    carta_dict_final['bonus'] = carta_dict.get('bonus')

    carta_dict_final['path_imagen_frente'] = carta_dict.get('path_imagen_frente')
    carta_dict_final['path_imagen_reverso'] = carta_dict.get('path_imagen_reverso')
    
    carta_dict_final['visible'] = False

    carta_dict_final['imagen'] = aux.achicar_imagen_carta(carta_dict_final.get('path_imagen_frente'), 45)
    carta_dict_final['imagen_reverso'] = aux.achicar_imagen_carta(carta_dict_final.get('path_imagen_reverso'), 45)
    
    carta_dict_final['rect'] = carta_dict_final.get('imagen').get_rect()
    carta_dict_final['rect'].x = coordenadas[0]
    carta_dict_final['rect'].y = coordenadas[1]
    
    carta_dict_final['rect_reverso'] = carta_dict_final.get('imagen_reverso').get_rect()
    carta_dict_final['rect_reverso'].x = coordenadas[0]
    carta_dict_final['rect_reverso'].y = coordenadas[1]
    
    return carta_dict_final

def obtener_hp_carta(card_dict: dict):
    """
    Obtiene los puntos de vida de una carta.
    
    Args:
        card_dict (dict): Diccionario de la carta
    
    Returns:
        int: Puntos de vida de la carta
    """
    return card_dict.get('hp')

def obtener_atk_carta(card_dict: dict):
    """
    Obtiene los puntos de ataque de una carta.
    
    Args:
        card_dict (dict): Diccionario de la carta
    
    Returns:
        int: Puntos de ataque de la carta
    """
    return card_dict.get('atk')

def obtener_def_carta(card_dict: dict):
    """
    Obtiene los puntos de defensa de una carta.
    
    Args:
        card_dict (dict): Diccionario de la carta
    
    Returns:
        int: Puntos de defensa de la carta
    """
    return card_dict.get('def')

def obtener_bonus_carta(card_dict: dict):
    """
    Obtiene el porcentaje de bonus de una carta.
    
    Args:
        card_dict (dict): Diccionario de la carta
    
    Returns:
        int: Porcentaje de bonus de la carta
    """
    return card_dict.get('bonus')

def obtener_ataque_mas_bonus(card_dict: dict):
    """
    Calcula el ataque de la carta incluyendo el bonus aplicado.
    
    Args:
        card_dict (dict): Diccionario de la carta
    
    Returns:
        int: Ataque total con bonus aplicado
    """
    ataque_mas_bonus = obtener_atk_carta(card_dict) * (1+(obtener_bonus_carta(card_dict))/100)
    return int(ataque_mas_bonus)

def obtener_hp_mas_bonus(card_dict: dict):
    """
    Calcula los puntos de vida de la carta incluyendo el bonus aplicado.
    
    Args:
        card_dict (dict): Diccionario de la carta
    
    Returns:
        int: HP total con bonus aplicado
    """
    hp_mas_bonus = obtener_hp_carta(card_dict) * (1+(obtener_bonus_carta(card_dict))/100)
    return int(hp_mas_bonus)

def obtener_def_mas_bonus(card_dict: dict):
    """
    Calcula la defensa de la carta incluyendo el bonus aplicado.
    
    Args:
        card_dict (dict): Diccionario de la carta
    
    Returns:
        int: Defensa total con bonus aplicado
    """
    def_mas_bonus = obtener_def_carta(card_dict) * (1+(obtener_bonus_carta(card_dict))/100)
    return int(def_mas_bonus)

def dibujar_carta(datos_carta: dict, pantalla: pygame.Surface):
    """
    Dibuja la carta en la pantalla, mostrando el frente si es visible o el reverso si no lo es.
    
    Args:
        datos_carta (dict): Diccionario de la carta con información visual
        pantalla (pygame.Surface): Superficie donde dibujar la carta
    """
    if datos_carta.get('visible'):
        pantalla.blit(datos_carta.get('imagen'), datos_carta.get('rect'))
    else:
        pantalla.blit(datos_carta.get('imagen_reverso'), datos_carta.get('rect_reverso'))

def asignar_coordenadas_carta(carta_dict: dict, nueva_coordenada: tuple[int,int]):
    """
    Asigna nuevas coordenadas a una carta, actualizando ambos rectángulos (frente y reverso).
    
    Args:
        carta_dict (dict): Diccionario de la carta
        nueva_coordenada (tuple[int,int]): Tupla con las nuevas coordenadas (x, y)
    """
    carta_dict['rect'].topleft = nueva_coordenada
    carta_dict['rect_reverso'].topleft = nueva_coordenada

def cambiar_visibilidad_carta(carta_dict: dict):
    """
    Cambia la visibilidad de una carta a visible (muestra el frente).
    
    Args:
        carta_dict (dict): Diccionario de la carta
    """
    carta_dict['visible'] = True
