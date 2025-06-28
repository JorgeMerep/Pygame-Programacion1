from modulos.auxiliar import cargar_ranking


ranking = cargar_ranking()

for linea in ranking:
    print(linea)