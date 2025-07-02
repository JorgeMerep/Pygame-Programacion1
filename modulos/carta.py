import pygame  
import modulos.auxiliar as aux


def inicializar_carta(carta_dict: dict, coordenadas: tuple[int,int]) -> dict:

    carta_dict_final = {}

    carta_dict_final['id'] = carta_dict.get('id')
    carta_dict_final['hp'] = carta_dict.get('hp')
    carta_dict_final['atk'] = carta_dict.get('atk')
    carta_dict_final['def'] = carta_dict.get('def')


    carta_dict_final['path_imagen_frente'] = carta_dict.get('path_imagen_frente')
    carta_dict_final['path_imagen_reverso'] = carta_dict.get('path_imagen_reverso')
    
    carta_dict_final['visible'] = False

    carta_dict_final['imagen'] = aux.achicar_imagen_card(carta_dict_final.get('path_imagen_frente'), 40)
    carta_dict_final['imagen_reverso'] = aux.achicar_imagen_card(carta_dict_final.get('path_imagen_reverso'), 40)
    
    carta_dict_final['rect'] = carta_dict_final.get('imagen').get_rect()
    carta_dict_final['rect'].x = coordenadas[0]
    carta_dict_final['rect'].y = coordenadas[1]
    
    carta_dict_final['rect_reverso'] = carta_dict_final.get('imagen_reverso').get_rect()
    carta_dict_final['rect_reverso'].x = coordenadas[0]
    carta_dict_final['rect_reverso'].y = coordenadas[1]
    
    return carta_dict_final

def get_hp_carta(card_dict: dict):
    return card_dict.get('hp')

def get_atk_carta(card_dict: dict):
    return card_dict.get('atk')

def get_def_carta(card_dict: dict):
    return card_dict.get('def')

def draw_carta(datos_carta: dict, pantalla: pygame.Surface):
    
    if datos_carta.get('visible'):
        pantalla.blit(datos_carta.get('imagen'), datos_carta.get('rect'))
    else:
        pantalla.blit(datos_carta.get('imagen_reverso'), datos_carta.get('rect_reverso'))

def asignar_coordenadas_carta(carta_dict: dict, nueva_coordenada: tuple[int,int]):
    carta_dict['rect'].topleft = nueva_coordenada
    carta_dict['rect_reverso'].topleft = nueva_coordenada

def cambiar_visibilidad_carta(carta_dict: dict):
    carta_dict['visible'] = True
    