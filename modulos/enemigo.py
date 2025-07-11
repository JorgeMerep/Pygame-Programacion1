
def inicializar_enemigo():
    enemigo = {}
    enemigo['puntaje_actual'] = 0
    enemigo['puntaje_total'] = 0
    enemigo['nombre'] = 'Enemigo'
    
    return enemigo

def sumar_puntaje_mano_ganada(enemigo: dict, nuevo_puntaje: int):
    enemigo['puntaje_actual'] += nuevo_puntaje



