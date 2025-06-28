import modulos.variables as var

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

