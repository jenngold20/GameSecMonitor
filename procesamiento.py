
#Consigna 2 - Módulo procesamiento.py - Métricas globales de operación
#Implementar una función que calcule un panorama estadístico general de todas las sesiones registradas:



def calcular_estadisticas_globales(sesiones: list[dict]) -> dict:  #->dict devuelve un diccionario con las 4 métricas solciitadas. 
   #Retorna un diccionario con las métricas consolidadas 
#Recibe la lista de diccionario que devuelve cargar_telemetria(). La recibe como parámetro, sin usar variables globales.
   

   #Preparamos las variables: 
    total = len(sesiones) #cuenta cuantos elementos tiene la lista, serian 150.

    #acumuladores, arrancan en 0 y en cada vuelta del foro se les suma un valor, al final tienen la suma total, que se divide por la cantidad para sacar el promedio.
    suma_ping = 0 
    suma_duracion = 0

    #es un contador, también arranca en 0 pero suma 1 solo cuando se cumple una condición. 
    cant_competitivas = 0  

    #todas arrancan en 0 porque si no existieran antes del for, en python daria error la primera vez que se intenta sumarles algo. 

    for sesion in sesiones:    #en cada vuelta, sesion es un diccionario de la lista, 
        suma_ping = suma_ping + sesion["ping_promedio"] #saca el valor de esa clave del diccionario. Se le suma a lo que ya habia gracias al casteo en carga.py.
        suma_duracion = suma_duracion + sesion["duracion_minutos"]
        # contamos competitivas y torneos juntos. La consigna pide el procentaje de partidas "Competititva" o "Torneo" por eso usamos el OR. 
        #Si es "Casual" no suma nada,-
        if sesion["tipo_partida"] == "Competitiva" or sesion["tipo_partida"] == "Torneo": #Se pone sesion["tipo_partida"] == dos veces porque sino python lo toma como True siempre porque "Torneo" solo ya cuenta como verdadero.
            cant_competitivas = cant_competitivas + 1

    #armamos el resultado según la consigna,  el promedio, porcentaje, round(valor, 2) redondea a 2 decimales.
    #va fuera del for, se calcula una sola vez cuando ya se sumaron todas las sesiones.
    estadisticas = {
        "total_sesiones": total, #la lista no deberia estar vacía porque total seria 0, y no podemos dividir por 0. Igualmente no puede pasar porque cargar_telemetria() lanza un error si el archivo está vacío. 
        "ping_promedio": round(suma_ping / total, 2), 
        "duracion_promedio": round(suma_duracion / total, 2),
        "porcentaje_competitivas": round(cant_competitivas * 100 / total, 2),  
    }
    return estadisticas
#la función no imprime nada, sino que devuelve un diccionario. vamos a usarlo en el main.py para mostarlo por pantalla y para el reporte.

#TESTEO:
#import carga
#print(calcular_estadisticas_globales(carga.cargar_telemetria("gamesec_logs.csv")))
#Devuelve: {'total_sesiones': 150, 'ping_promedio': 148.44, 'duracion_promedio': 29.39, 'porcentaje_competitivas': 53.33}


   
"""
   El diccionario retornado debe contener las siguientes claves:
    'total_sesiones': Cantidad total de registros analizados (int). 
    'ping_promedio': Latencia media global redondeada a 2 decimales (float). 
    'duracion_promedio': Duración media de partidas en minutos redondeada a 2 decimales (float). 
    'porcentaje_competitivas': Porcentaje de sesiones correspondientes a 'Competitiva' o 'Torneo' sobre el total (float).

"""

def analizar_por_servidor(sesiones: list[dict]) -> dict: 
# Retorna un diccionario con el formato: 
# { 
#     "SA-BuenosAires": {"cantidad": 42, "ping_promedio": 45.2, "fps_promedio": 115.4},"
#     
# } 
    acumulador = {}

    for sesion in sesiones:
        servidor = sesion["servidor"]
        if servidor not in acumulador:
            acumulador[servidor] = {"cantidad": 0, "suma_ping": 0, "suma_fps": 0}

        acumulador[servidor]["cantidad"] = acumulador[servidor]["cantidad"] + 1
        acumulador[servidor]["suma_ping"] = acumulador[servidor]["suma_ping"] + sesion["ping_promedio"]
        acumulador[servidor]["suma_fps"] = acumulador[servidor]["suma_fps"] + sesion["fps_promedio"]

    # con las sumas armo el resultado final con los promedios
    resultado = {}
    for servidor in acumulador:
        cantidad = acumulador[servidor]["cantidad"]
        resultado[servidor] = {
            "cantidad": cantidad,
            "ping_promedio": round(acumulador[servidor]["suma_ping"] / cantidad, 2),
            "fps_promedio": round(acumulador[servidor]["suma_fps"] / cantidad, 2),
        }
    return resultado


def clasificar_sesion(sesion: dict) -> str:
    # devuelve el estado de una sola sesion segun las reglas del tp
    ping = sesion["ping_promedio"]
    intentos = sesion["intentos_fallidos"]
    reportes = sesion["reportes_trampa"]

    if reportes >= 3 or intentos >= 4:
        return "Crítico"
    elif (ping > 200 and intentos >= 2) or reportes == 2:
        return "Sospechoso"
    else:
        return "Normal"


def obtener_motivo(sesion: dict) -> str:
    # arma el texto que explica por que la sesion es critica
    intentos = sesion["intentos_fallidos"]
    reportes = sesion["reportes_trampa"]

    if reportes >= 3 and intentos >= 4:
        return "Exceso de reportes por trampa (" + str(reportes) + ") e intentos fallidos (" + str(intentos) + ")"
    elif reportes >= 3:
        return "Exceso de reportes por trampa (" + str(reportes) + " reportes)"
    else:
        return "Ataque de fuerza bruta en login (" + str(intentos) + " intentos fallidos)"


def clasificar_incidentes(sesiones: list[dict]) -> tuple[dict, list[dict]]: 
    # Retorna una tupla: 
    # 1. Diccionario resumen de frecuencias: {"Normal": N, "Sospechoso": S, "Crítico": C} 
    # 2. Lista de diccionarios simplificados correspondientes únicamente a los eventos 'Crítico' 
   # devuelve el estado de una sola sesion segun las reglas del tp
    resumen = {"Normal": 0, "Sospechoso": 0, "Crítico": 0}
    criticos = []

    for sesion in sesiones:
        estado = clasificar_sesion(sesion)
        resumen[estado] = resumen[estado] + 1

        # solo guardo en la lista los criticos, con los datos resumidos
        if estado == "Crítico":
            evento = {
                "id_sesion": sesion["id_sesion"],
                "jugador_id": sesion["jugador_id"],
                "servidor": sesion["servidor"],
                "motivo": obtener_motivo(sesion),
            }
            criticos.append(evento)

    return resumen, criticos

''' Debe devolver: 
{ 
    "id_sesion": 14, 
    "jugador_id": "User_482", 
    "servidor": "NA-Virginia", 
    "motivo": "Exceso de reportes por trampa (4) e intentos fallidos (5)" 
}
'''

def obtener_sospechosos(sesiones: list[dict]) -> list[dict]:
    # devuelve las sesiones que quedaron como sospechosas (para la opcion 4 del menu)
    sospechosos = []
    for sesion in sesiones:
        if clasificar_sesion(sesion) == "Sospechoso":
            sospechosos.append(sesion)
    return sospechosos