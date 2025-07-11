
def inicializar_jugador():
    jugador_actual = {}
    jugador_actual['puntaje_actual'] = 0
    jugador_actual['puntaje_total'] = 0
    jugador_actual['nombre'] = 'Player'
    
    return jugador_actual

def actualizar_puntaje_total(jugador_actual: dict):
    jugador_actual['puntaje_total'] += jugador_actual.get('puntaje_actual')

def obtener_puntaje_total(jugador_actual: dict):
    return jugador_actual.get('puntaje_total')

def sumar_puntaje_mano_ganada(jugador_actual: dict, nuevo_puntaje: int):
    jugador_actual['puntaje_actual'] += nuevo_puntaje

def colocar_nombre(jugador_actual: dict, nuevo_puntaje: int):
    jugador_actual['nombre'] = nuevo_puntaje