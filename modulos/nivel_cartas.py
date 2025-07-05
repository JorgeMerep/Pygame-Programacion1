import pygame  
import modulos.variables as var
import modulos.auxiliar as aux
import random
import modulos.carta as carta
import modulos.jugador as jugador_humano

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

    nivel_data['pantalla'] = pantalla

    nivel_data['jugador'] = jugador
    nivel_data['enemigo'] = enemigo

    
    nivel_data['juego_finalizado'] = False
    nivel_data['puntaje_guardado'] = False
    nivel_data['timer_partida'] = var.TIMER
    nivel_data['ganador'] = None
 
    nivel_data['puntaje_nivel'] = 0
    nivel_data['data_cargada'] = False
    
    return nivel_data

def inicializar_data_nivel(nivel_data: dict):
    print('ESTOY GASTANDO RECURSOS Y CARGANDO TODA LA DATA DEL LEVEL')
    cargar_configs_nivel(nivel_data)
    cargar_bd_cartas(nivel_data)
    generar_mazo_jugador(nivel_data)
    generar_mazo_enemigo(nivel_data)

def cargar_configs_nivel(nivel_data: dict):
    if not nivel_data.get('juego_finalizado') and not nivel_data.get('data_cargada'):
        print('=============== CARGANDO CONFIGS INICIALES ===============')
        configs_globales = aux.cargar_configs(var.RUTA_CONFIGS_JSON)
        print(f'PRIMER PRINT {configs_globales}')
        nivel_data['configs'] = configs_globales.get(f'nivel_{nivel_data.get("numero_nivel")}')
        print(f'SEGUNDO PRINT {nivel_data.get("configs")}')
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
                print(f"⚠️ Atención: No se encontró el mazo '{nombre_mazo}' en la ruta {ruta}")

        print(nivel_data.get("cartas_mazo_juego"))
        print("BASE DE DATOS DE CARTAS CARGA COMPLETA")


def generar_mazo_jugador(nivel_data: dict):
    print('=============== GENERANDO MAZO FINAL ===============')

    bd_cartas = nivel_data.get('cartas_mazo_juego')  # Dict con mazos y sus cartas
    cantidades = nivel_data.get('configs').get('cantidades')  # Dict con cantidades por mazo

    nivel_data['cartas_mazo_juego_final_jugador'] = []

    coordenada_inicial = nivel_data.get('configs').get('coordenadas').get('mazo_1_jugador')
    
    for mazo, cantidad in cantidades.items():
        for indice_cartas in range (cantidad):
            carta_base = bd_cartas.get(mazo).pop() #Levantamos la carta base de la DB y usamos la ultima y la quitamos de la DB
            carta_final = carta.inicializar_carta(carta_base, coordenada_inicial)
            nivel_data['cartas_mazo_juego_final_jugador'].append(carta_final)
            print(carta_final)

    random.shuffle(nivel_data['cartas_mazo_juego_final_jugador'])  # Mezclar el mazo final

def generar_mazo_enemigo(nivel_data: dict):
    print('=============== GENERANDO MAZO FINAL ===============')

    bd_cartas = nivel_data.get('cartas_mazo_juego')  # Dict con mazos y sus cartas
    cantidades = nivel_data.get('configs').get('cantidades')  # Dict con cantidades por mazo

    nivel_data['cartas_mazo_juego_final_enemigo'] = []

    coordenada_inicial = nivel_data.get('configs').get('coordenadas').get('mazo_1_enemigo')
    
    for mazo, cantidad in cantidades.items():
        for indice_cartas in range (cantidad):
            carta_base = bd_cartas.get(mazo).pop() #Levantamos la carta base de la DB y usamos la ultima y la quitamos de la DB
            carta_final = carta.inicializar_carta(carta_base, coordenada_inicial)
            nivel_data['cartas_mazo_juego_final_enemigo'].append(carta_final)
            print(carta_final)

    random.shuffle(nivel_data['cartas_mazo_juego_final_enemigo'])  # Mezclar el mazo final

def eventos(nivel_data: dict, cola_eventos: list[pygame.event.Event]):
    
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(f'Coordenada: {evento.pos}')
            # verificar la colision con el boton del jugador
            if nivel_data.get('cartas_mazo_juego_final_jugador') and\
               nivel_data.get('cartas_mazo_juego_final_jugador')[-1].get('rect').collidepoint(evento.pos) and\
               not nivel_data.get('cartas_mazo_juego_final_jugador')[-1].get('visible'):
                carta.asignar_coordenadas_carta(nivel_data.get('cartas_mazo_juego_final_jugador')[-1], nivel_data.get('configs').get('coordenadas').get('mazo_2_jugador'))

                carta.cambiar_visibilidad_carta(nivel_data.get('cartas_mazo_juego_final_jugador')[-1])
                
                carta_vista = nivel_data.get('cartas_mazo_juego_final_jugador').pop()
                nivel_data.get('cartas_mazo_juego_final_vistas_jugador').append(carta_vista)

            # verificar la colision con el boton del jugador
            if nivel_data.get('cartas_mazo_juego_final_enemigo') and\
               nivel_data.get('cartas_mazo_juego_final_enemigo')[-1].get('rect').collidepoint(evento.pos) and\
               not nivel_data.get('cartas_mazo_juego_final_enemigo')[-1].get('visible'):
                carta.asignar_coordenadas_carta(nivel_data.get('cartas_mazo_juego_final_enemigo')[-1], nivel_data.get('configs').get('coordenadas').get('mazo_2_enemigo'))

                carta.cambiar_visibilidad_carta(nivel_data.get('cartas_mazo_juego_final_enemigo')[-1])
                
                carta_vista = nivel_data.get('cartas_mazo_juego_final_enemigo').pop()
                nivel_data.get('cartas_mazo_juego_final_vistas_enemigo').append(carta_vista)
                                         

def tiempo_esta_terminado(nivel_data: dict):
    return nivel_data.get('timer_partida') <= 0

def mazo_esta_vacio(nivel_data: dict):
    return len(nivel_data.get('cartas_mazo_juego_final_jugador')) == 0

def check_juego_terminado(nivel_data: dict):
    if mazo_esta_vacio(nivel_data) or\
        tiempo_esta_terminado(nivel_data):
            nivel_data['juego_finalizado'] = True

def juego_terminado(nivel_data: dict):
    return nivel_data.get('juego_finalizado')

def reiniciar_nivel(nivel_cartas: dict, jugador: dict, pantalla: pygame.Surface, nro_nivel: int):
    print('=============== REINICIANDO NIVEL ===============')
    jugador_humano.set_puntaje_actual(jugador, 0)
    nivel_cartas = inicializar_nivel_cartas(jugador, pantalla, nro_nivel)
    return nivel_cartas

def dibujar_cartas(nivel_data: dict):
    if nivel_data.get('cartas_mazo_juego_final_jugador'):
        carta.dibujar_carta(nivel_data.get('cartas_mazo_juego_final_jugador')[-1], nivel_data.get('pantalla'))
        
    if nivel_data.get('cartas_mazo_juego_final_vistas_jugador'):
        carta.dibujar_carta(nivel_data.get('cartas_mazo_juego_final_vistas_jugador')[-1], nivel_data.get('pantalla'))
    
    if nivel_data.get('cartas_mazo_juego_final_enemigo'):
        carta.dibujar_carta(nivel_data.get('cartas_mazo_juego_final_enemigo')[-1], nivel_data.get('pantalla'))
        
    if nivel_data.get('cartas_mazo_juego_final_vistas_enemigo'):
        carta.dibujar_carta(nivel_data.get('cartas_mazo_juego_final_vistas_enemigo')[-1], nivel_data.get('pantalla'))

def actualizar_cartas(nivel_data: dict, cola_eventos: list[pygame.event.Event]):
    eventos(nivel_data, cola_eventos)
    check_juego_terminado(nivel_data)
    if juego_terminado(nivel_data) and not nivel_data.get('puntaje_guardado'):
        jugador_humano.actualizar_puntaje_total(nivel_data.get("jugador"))
        # nombre_elegido = rd.choice(var.nombres)
        # jugador_humano.set_nombre(nivel_data.get("jugador"), nombre_elegido)
        # aux.guardar_ranking(nivel_data.get('jugador'))
        nivel_data['puntaje_guardado'] = True
        print(f'Puntaje acumulado: {jugador_humano.get_puntaje_total(nivel_data.get("jugador"))}')