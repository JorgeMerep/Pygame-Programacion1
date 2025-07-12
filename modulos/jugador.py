def inicializar_jugador():
    """
    Inicializa un diccionario de jugador con valores predeterminados.
    
    Returns:
        dict: Diccionario del jugador con puntajes inicializados en 0 y nombre por defecto
    """
    jugador_actual = {}
    jugador_actual['puntaje_actual'] = 0
    jugador_actual['puntaje_total'] = 0
    jugador_actual['nombre'] = 'Player'
    
    return jugador_actual

def actualizar_puntaje_total(jugador_actual: dict):
    """
    Actualiza el puntaje total del jugador sumando el puntaje actual.
    
    Args:
        jugador_actual (dict): Diccionario del jugador
    """
    jugador_actual['puntaje_total'] += jugador_actual.get('puntaje_actual')

def obtener_puntaje_total(jugador_actual: dict):
    """
    Obtiene el puntaje total del jugador.
    
    Args:
        jugador_actual (dict): Diccionario del jugador
    
    Returns:
        int: Puntaje total del jugador
    """
    return jugador_actual.get('puntaje_total')

def sumar_puntaje_mano_ganada(jugador_actual: dict, nuevo_puntaje: int):
    """
    Suma puntaje al jugador cuando gana una mano.
    
    Args:
        jugador_actual (dict): Diccionario del jugador
        nuevo_puntaje (int): Puntaje a sumar por la mano ganada
    """
    jugador_actual['puntaje_actual'] += nuevo_puntaje

def colocar_nombre(jugador_actual: dict, nuevo_nombre: str):
    """
    Asigna un nuevo nombre al jugador.
    
    Args:
        jugador_actual (dict): Diccionario del jugador
        nuevo_nombre (str): Nuevo nombre del jugador
    """
    jugador_actual['nombre'] = nuevo_nombre

def obtener_puntaje_actual(jugador_actual: dict):
    """
    Obtiene el puntaje actual del jugador.
    
    Args:
        jugador_actual (dict): Diccionario del jugador
    
    Returns:
        int: Puntaje actual del jugador
    """
    return jugador_actual.get('puntaje_actual')

def obtener_nombre(jugador_actual: dict):
    """
    Obtiene el nombre del jugador.
    
    Args:
        jugador_actual (dict): Diccionario del jugador
    
    Returns:
        str: Nombre del jugador
    """
    return jugador_actual.get('nombre')

def reiniciar_partida(jugador_actual: dict):
    """
    Reinicia el puntaje actual del jugador manteniendo el puntaje total.
    
    Args:
        jugador_actual (dict): Diccionario del jugador
    """
    jugador_actual['puntaje_actual'] = 0