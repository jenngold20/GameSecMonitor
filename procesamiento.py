
#Consigna 2 - Módulo procesamiento.py - Métricas globales de operación
#Implementar una función que calcule un panorama estadístico general de todas las sesiones registradas:



def calcular_estadisticas_globales(sesiones: list[dict]) -> dict:
   #Retorna un diccionario con las métricas consolidadas 

   pass
   
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
    pass 
...



def clasificar_incidentes(sesiones: list[dict]) -> tuple[dict, list[dict]]: 
    # Retorna una tupla: 
    # 1. Diccionario resumen de frecuencias: {"Normal": N, "Sospechoso": S, "Crítico": C} 
    # 2. Lista de diccionarios simplificados correspondientes únicamente a los eventos 'Crítico' 
    pass


''' Debe devolver: 
{ 
    "id_sesion": 14, 
    "jugador_id": "User_482", 
    "servidor": "NA-Virginia", 
    "motivo": "Exceso de reportes por trampa (4) e intentos fallidos (5)" 
}
'''