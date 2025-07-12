def inicializar_enemigo():
    """
    Inicializa un diccionario de enemigo con valores predeterminados.
    
    Returns:
        dict: Diccionario del enemigo con puntajes inicializados en 0 y nombre por defecto
    """
    enemigo = {}
    enemigo['puntaje_actual'] = 0
    enemigo['puntaje_total'] = 0
    enemigo['nombre'] = 'Enemigo'
    
    return enemigo

def sumar_puntaje_mano_ganada(enemigo: dict, nuevo_puntaje: int):
    """
    Suma puntaje al enemigo cuando gana una mano.
    
    Args:
        enemigo (dict): Diccionario del enemigo
        nuevo_puntaje (int): Puntaje a sumar por la mano ganada
    """
    enemigo['puntaje_actual'] += nuevo_puntaje

def obtener_puntaje_actual(enemigo: dict):
    """
    Obtiene el puntaje actual del enemigo.
    
    Args:
        enemigo (dict): Diccionario del enemigo
    
    Returns:
        int: Puntaje actual del enemigo
    """
    return enemigo.get('puntaje_actual')

def obtener_puntaje_total(enemigo: dict):
    """
    Obtiene el puntaje total del enemigo.
    
    Args:
        enemigo (dict): Diccionario del enemigo
    
    Returns:
        int: Puntaje total del enemigo
    """
    return enemigo.get('puntaje_total')

def obtener_nombre(enemigo: dict):
    """
    Obtiene el nombre del enemigo.
    
    Args:
        enemigo (dict): Diccionario del enemigo
    
    Returns:
        str: Nombre del enemigo
    """
    return enemigo.get('nombre')

def reiniciar_partida(enemigo: dict):
    """
    Reinicia el puntaje actual del enemigo manteniendo el puntaje total.
    
    Args:
        enemigo (dict): Diccionario del enemigo
    """
    enemigo['puntaje_actual'] = 0



