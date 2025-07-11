import pygame  
import modulos.variables as var
import modulos.auxiliar as aux
import random
import modulos.carta as carta
import modulos.jugador as jugador_humano
import modulos.enemigo as enemigo_actual

def inicializar_nivel_cartas(jugador: dict, enemigo: dict, pantalla: pygame.Surface, numero_nivel: int):
    
    nivel_data = {}
    nivel_data['numero_nivel'] = numero_nivel
    nivel_data['configs'] = {}

    nivel_data['cartas_mazo_juego'] = [] #Todas las cartas de la base de datos
    nivel_data['cartas_mazo_juego_final_jugador'] = [] #Cartas reverso repartidas al jugador
    nivel_data['cartas_mazo_juego_final_enemigo'] = [] #Cartas reverso repartidas al enemigo
    nivel_data['cartas_mazo_juego_final_vistas_jugador'] = [] #Cartas frente del jugador
    nivel_data['cartas_mazo_juego_final_vistas_enemigo'] = [] #Cartas frente del enemigo
    nivel_data['rutas_mazos'] = ''

    nivel_data["hp_total_inicial_jugador"] = 0

    nivel_data["hp_total_jugador"] = 0
    nivel_data["atk_total_jugador"] = 0
    nivel_data["def_total_jugador"] = 0
    nivel_data["hp_total_enemigo"] = 0
    nivel_data["atk_total_enemigo"] = 0
    nivel_data["def_total_enemigo"] = 0

    nivel_data['buff_shield_activo'] = False
    nivel_data['buff_heal_activo'] = False


    nivel_data['pantalla'] = pantalla

    nivel_data['jugador'] = jugador
    nivel_data['enemigo'] = enemigo
    nivel_data["evaluar_ganador"] = ""

    
    nivel_data['juego_finalizado'] = False
    nivel_data['puntaje_guardado'] = False

    nivel_data['timer_partida'] = var.TIMER
    nivel_data['ganador'] = None
 
    nivel_data['puntaje_nivel'] = 0
    nivel_data['data_cargada'] = False
    
    return nivel_data

def inicializar_data_nivel(nivel_data: dict): 
    cargar_configs_nivel(nivel_data)
    cargar_bd_cartas(nivel_data)
    generar_mazo_jugador(nivel_data)
    generar_mazo_enemigo(nivel_data)

def cargar_configs_nivel(nivel_data: dict):
    if not nivel_data.get('juego_finalizado') and not nivel_data.get('data_cargada'):
        print('=============== CARGANDO CONFIGS INICIALES ===============')
        configs_globales = aux.cargar_configs(var.RUTA_CONFIGS_JSON)
        nivel_data['configs'] = configs_globales.get(f'nivel_{nivel_data.get("numero_nivel")}')
        nivel_data['rutas_mazos'] = nivel_data.get('configs').get('mazos')

def cargar_bd_cartas(nivel_data: dict):
    if not nivel_data.get('juego_finalizado'):
        print('=============== GENERANDO BD CARTAS INICIALES ===============')

        nivel_data['cartas_mazo_juego'] = {}  # Inicializar como diccionario vacío

        for nombre_mazo, ruta in nivel_data.get('rutas_mazos').items():
            cartas_del_mazo = aux.generar_bd(ruta)

            # Buscar el mazo por nombre y agregarlo al dict general
            if nombre_mazo in cartas_del_mazo:
                nivel_data['cartas_mazo_juego'][nombre_mazo] = cartas_del_mazo[nombre_mazo]
            else:
                print(f"No se encontró el mazo '{nombre_mazo}' en la ruta {ruta}")

        print(nivel_data.get("cartas_mazo_juego"))
        print("BASE DE DATOS DE CARTAS CARGA COMPLETA")


def generar_mazo_jugador(nivel_data: dict):
    print('=============== GENERANDO MAZO FINAL JUGADOR ===============')

    bd_cartas = nivel_data.get('cartas_mazo_juego')  # Dict con mazos y sus cartas
    cantidades = nivel_data.get('configs').get('cantidades')  # Dict con cantidades por mazo

    nivel_data['cartas_mazo_juego_final_jugador'] = []

    coordenada_inicial = nivel_data.get('configs').get('coordenadas').get('mazo_1_jugador')
    
    for mazo, cantidad in cantidades.items():
        mazo_elegido = random.sample(bd_cartas.get(mazo), cantidad)
        
        for cartas in (mazo_elegido):
            carta_final = carta.inicializar_carta(cartas, coordenada_inicial)
            nivel_data['cartas_mazo_juego_final_jugador'].append(carta_final)

    random.shuffle(nivel_data['cartas_mazo_juego_final_jugador'])  # Mezclar el mazo final

    # Inicializar los totales en 0
    nivel_data["hp_total_jugador"] = 0
    nivel_data["hp_total_inicial_jugador"] = 0 
    nivel_data["atk_total_jugador"] = 0
    nivel_data["def_total_jugador"] = 0
    nivel_data["hp_total_enemigo"] = 0
    nivel_data["atk_total_enemigo"] = 0
    nivel_data["def_total_enemigo"] = 0

    # Sumar los stats del mazo del jugador
    for carta_final in nivel_data["cartas_mazo_juego_final_jugador"]:
        nivel_data["hp_total_jugador"] += carta_final.get("hp", 0)
        nivel_data["hp_total_inicial_jugador"] += carta_final.get("hp", 0)
        nivel_data["atk_total_jugador"] += carta_final.get("atk", 0)
        nivel_data["def_total_jugador"] += carta_final.get("def", 0)
    


def generar_mazo_enemigo(nivel_data: dict):
    print('=============== GENERANDO MAZO FINAL ENEMIGO===============')

    bd_cartas = nivel_data.get('cartas_mazo_juego')  # Dict con mazos y sus cartas
    cantidades = nivel_data.get('configs').get('cantidades')  # Dict con cantidades por mazo

    nivel_data['cartas_mazo_juego_final_enemigo'] = []

    coordenada_inicial = nivel_data.get('configs').get('coordenadas').get('mazo_1_enemigo')
    
    for mazo, cantidad in cantidades.items():
        mazo_elegido = random.sample(bd_cartas.get(mazo), cantidad)
        
        for cartas in (mazo_elegido):
            carta_final = carta.inicializar_carta(cartas, coordenada_inicial)
            nivel_data['cartas_mazo_juego_final_enemigo'].append(carta_final)

    random.shuffle(nivel_data['cartas_mazo_juego_final_enemigo'])  # Mezclar el mazo final

    # Sumar los stats del mazo del enemigo
    for carta_final in nivel_data["cartas_mazo_juego_final_enemigo"]:
        nivel_data["hp_total_enemigo"] += carta_final.get("hp", 0)
        nivel_data["atk_total_enemigo"] += carta_final.get("atk", 0)
        nivel_data["def_total_enemigo"] += carta_final.get("def", 0)


def jugar_partida(nivel_data: dict):
    
    # JUGADOR: Verificar cartas del mazo. Visibilidad. Dar vuelta carta
    if nivel_data.get('cartas_mazo_juego_final_jugador') and\
        not nivel_data.get('cartas_mazo_juego_final_jugador')[-1].get('visible'):
        carta.asignar_coordenadas_carta(nivel_data.get('cartas_mazo_juego_final_jugador')[-1], nivel_data.get('configs').get('coordenadas').get('mazo_2_jugador'))

        carta.cambiar_visibilidad_carta(nivel_data.get('cartas_mazo_juego_final_jugador')[-1])
        
        carta_vista_jugador = nivel_data.get('cartas_mazo_juego_final_jugador').pop()
        nivel_data.get('cartas_mazo_juego_final_vistas_jugador').append(carta_vista_jugador)

    # ENEMIGO: Verificar cartas del mazo. Visibilidad. Dar vuelta carta
    if nivel_data.get('cartas_mazo_juego_final_enemigo') and\
        not nivel_data.get('cartas_mazo_juego_final_enemigo')[-1].get('visible'):
        carta.asignar_coordenadas_carta(nivel_data.get('cartas_mazo_juego_final_enemigo')[-1], nivel_data.get('configs').get('coordenadas').get('mazo_2_enemigo'))

        carta.cambiar_visibilidad_carta(nivel_data.get('cartas_mazo_juego_final_enemigo')[-1])
        
        carta_vista_enemigo = nivel_data.get('cartas_mazo_juego_final_enemigo').pop()
        nivel_data.get('cartas_mazo_juego_final_vistas_enemigo').append(carta_vista_enemigo)

    # Chequear carta jugador y enemigo para evaluar la carta ganadora. Evalua buffs
    evaluar_stats_carta_vista(carta_vista_jugador, carta_vista_enemigo, nivel_data)

def evaluar_stats_carta_vista(carta_vista_jugador: dict, carta_vista_enemigo: dict, nivel_data: dict):
    ataque_mas_bonus_jugador = carta.obtener_ataque_mas_bonus(carta_vista_jugador)
    ataque_mas_bonus_enemigo = carta.obtener_ataque_mas_bonus(carta_vista_enemigo) 

    if ataque_mas_bonus_jugador > ataque_mas_bonus_enemigo:
        defensa_perdida = carta.obtener_def_mas_bonus(carta_vista_enemigo)
        hp_perdida = carta.obtener_hp_mas_bonus(carta_vista_enemigo)
        nivel_data["def_total_enemigo"] = max(0, nivel_data["def_total_enemigo"] - defensa_perdida)
        nivel_data["hp_total_enemigo"] = max(0, nivel_data["hp_total_enemigo"] - hp_perdida)
        nivel_data["atk_total_enemigo"] = max(0, nivel_data["atk_total_enemigo"] - ataque_mas_bonus_enemigo)

    else:
        if nivel_data.get("buff_shield_activo", False):
            # SHIELD ACTIVO: daño rebota al enemigo
            defensa_perdida = carta.obtener_def_mas_bonus(carta_vista_enemigo)
            hp_perdida = carta.obtener_hp_mas_bonus(carta_vista_enemigo)
            nivel_data["def_total_enemigo"] = max(0, nivel_data["def_total_enemigo"] - defensa_perdida)
            nivel_data["hp_total_enemigo"] = max(0, nivel_data["hp_total_enemigo"] - hp_perdida)
            nivel_data["atk_total_enemigo"] = max(0, nivel_data["atk_total_enemigo"] - ataque_mas_bonus_enemigo)

        else:
            # Sin shield: jugador recibe daño normal
            defensa_perdida = carta.obtener_def_mas_bonus(carta_vista_jugador)
            hp_perdida = carta.obtener_hp_mas_bonus(carta_vista_jugador)
            nivel_data["def_total_jugador"] = max(0, nivel_data["def_total_jugador"] - defensa_perdida)
            nivel_data["hp_total_jugador"] = max(0, nivel_data["hp_total_jugador"] - hp_perdida)
            nivel_data["atk_total_jugador"] = max(0, nivel_data["atk_total_jugador"] - ataque_mas_bonus_jugador)

    
    evaluar_ganador_mano(ataque_mas_bonus_jugador, ataque_mas_bonus_enemigo, nivel_data)

    # Los buff solo se usan una vez
    nivel_data['buff_shield_activo'] = False
    nivel_data["buff_heal_activo"] = False


def evaluar_ganador_mano(ataque_mas_bonus_jugador: int, ataque_mas_bonus_enemigo: int, nivel_data: dict):
    if nivel_data["buff_shield_activo"] == True:
        jugador_humano.sumar_puntaje_mano_ganada(nivel_data.get("jugador"), 1)   
    else:
        if ataque_mas_bonus_jugador > ataque_mas_bonus_enemigo:
            jugador_humano.sumar_puntaje_mano_ganada(nivel_data.get("jugador"), 1)
        else:
            enemigo_actual.sumar_puntaje_mano_ganada(nivel_data.get("enemigo"), 1)

def evaluar_hp_jugadores(nivel_data: dict):
    if nivel_data.get("hp_total_jugador") == 0 or nivel_data.get("hp_total_enemigo") == 0:
       return True
    
def activar_buff_shield(nivel_data: dict):
    nivel_data['buff_shield_activo'] = True

def activar_buff_heal(nivel_data: dict):
    nivel_data["hp_total_jugador"] = nivel_data.get("hp_total_inicial_jugador") 

def tiempo_esta_terminado(nivel_data: dict):
    return nivel_data.get('timer_partida') <= 0

def mazo_esta_vacio(nivel_data: dict):
    return len(nivel_data.get('cartas_mazo_juego_final_jugador')) == 0 and len(nivel_data.get("cartas_mazo_juego_final_enemigo")) == 0

def juego_terminado(nivel_data: dict):
    return nivel_data.get('juego_finalizado')

def check_juego_terminado(nivel_data: dict):
    if mazo_esta_vacio(nivel_data) or\
        tiempo_esta_terminado(nivel_data) or\
            evaluar_hp_jugadores(nivel_data):
                nivel_data['juego_finalizado'] = True


def reiniciar_nivel(nivel_data: dict):
    print('=============== REINICIANDO NIVEL ===============')
    nivel_data['buff_shield_activo'] = False
    nivel_data['buff_heal_activo'] = False
    nivel_data['juego_finalizado'] = False
    nivel_data['puntaje_guardado'] = False
    nivel_data['data_cargada'] = False
    nivel_data['puntaje_nivel'] = 0
    nivel_data['timer_partida'] = var.TIMER
    nivel_data.get("jugador")["puntaje_actual"] = 0
    nivel_data.get("jugador")["puntaje_total"] = 0
    nivel_data.get("enemigo")["puntaje_actual"] = 0
    nivel_data.get("enemigo")["puntaje_total"] = 0

    inicializar_data_nivel(nivel_data)

    return 

def dibujar_cartas(nivel_data: dict):
    if nivel_data.get('cartas_mazo_juego_final_jugador'):
        carta.dibujar_carta(nivel_data.get('cartas_mazo_juego_final_jugador')[-1], nivel_data.get('pantalla'))
        
    if nivel_data.get('cartas_mazo_juego_final_vistas_jugador'):
        carta.dibujar_carta(nivel_data.get('cartas_mazo_juego_final_vistas_jugador')[-1], nivel_data.get('pantalla'))
    
    if nivel_data.get('cartas_mazo_juego_final_enemigo'):
        carta.dibujar_carta(nivel_data.get('cartas_mazo_juego_final_enemigo')[-1], nivel_data.get('pantalla'))
        
    if nivel_data.get('cartas_mazo_juego_final_vistas_enemigo'):
        carta.dibujar_carta(nivel_data.get('cartas_mazo_juego_final_vistas_enemigo')[-1], nivel_data.get('pantalla'))

def actualizar_cartas(nivel_data: dict):
    check_juego_terminado(nivel_data)
    if juego_terminado(nivel_data) and not nivel_data.get('puntaje_guardado'):
        jugador_humano.actualizar_puntaje_total(nivel_data.get("jugador"))
        nivel_data['puntaje_guardado'] = True
        print(f'Puntaje acumulado: {jugador_humano.get_puntaje_total(nivel_data.get("jugador"))}')

        
        