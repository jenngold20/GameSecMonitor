#Consigna 1: Módulo carga.py - Carga y Validación de datos

import csv #para leer el archivo
import os #para fijarme si el archivo existe


#Función encargada de leer el dataset
def cargar_telemetria(ruta_archivo: str) -> list[dict]:   #ruta_archivo:str es porque recibe el nombre del archivo como texto, va a devolver una lista de dicc.
    #Lee el archivo CSV con csv.DictReader 
    #Convierte tipos: int(id, ping, fps, intentos, reportes), float (duración), str(resto)
    #retorna una lista de diccionarios
    #pass
    if not os.path.exists(ruta_archivo):        #esto devuelve True o False, si el archivo no existe entra en el ValueError
        raise ValueError("el archivo " + ruta_archivo + " no existe")

    sesiones = []

    with open(ruta_archivo, "r", encoding="utf-8") as archivo:   #"r" para modo lectura, con with open abro el archivo y lo bueno es que cierra el archivo solo al terminar.
        lector = csv.DictReader(archivo)   #y lo leo  con DictReader. usa la primera lína del CSV como claves. 

        for fila in lector:   #cada fila es un diccionario. Todos los valores vienen como texto, incluso los números.
            # paso cada columna al tipo que corresponde
            sesion = {} #armo un diccionario nuevo pasando cada valor al tipo que corresponde.

            sesion["id_sesion"] = int(fila["id_sesion"])   #si no los casteo, no voy a poder sumar ni comparar.
            sesion["servidor"] = fila["servidor"]
            sesion["jugador_id"] = fila["jugador_id"]
            sesion["tipo_partida"] = fila["tipo_partida"]
            sesion["ping_promedio"] = int(fila["ping_promedio"])
            sesion["fps_promedio"] = int(fila["fps_promedio"])
            sesion["duracion_minutos"] = float(fila["duracion_minutos"])
            sesion["intentos_fallidos"] = int(fila["intentos_fallidos"])
            sesion["reportes_trampa"] = int(fila["reportes_trampa"])

            sesiones.append(sesion)  #agregamos cada sesión ya convertida a la lista. 

    # si no se cargo ninguna fila el archivo esta vacio, si el csv solo tenia encabezados, la lista queda vacia y se lanza otro ValueError
    if len(sesiones) == 0:      
        raise ValueError("el archivo esta vacio, no tiene registros")   #el archivo si no existe, o no tiene registros, tira el ValueError. 

    return sesiones  #devuelve la lista con las sesiones para poder ser usada luego en procesamiento.py


#Qué debe hacer esta función? 
''' 
Debe abrir el archivo usando with open(...) con codificación utf-8,
Utilizar csv.DictReader para mapear automáticamente los nombres de columnas
Realizar el casteo explícito de los tipos de datos numéricos (no pueden quedar como strings)
Validar que el archivo exista y contenga al menos un registro (lanzar ValueError o mensaje amigable si está vacío.)

'''

#print(cargar_telemetria("gamesec_logs.csv")[0])
'''
Devuelve: {'id_sesion': 1, 'servidor': 'SA-BuenosAires', 'jugador_id': 'User_125', 'tipo_partida': 'Competitiva', 'ping_promedio': 49, 'fps_promedio': 75, 'duracion_minutos': 12.0, 'intentos_fallidos': 0, 'reportes_trampa': 1}
'''

