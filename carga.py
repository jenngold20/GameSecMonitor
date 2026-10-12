#Consigna 1: Módulo carga.py - Carga y Validación de datos

import csv
import os



#Función encargada de leer el dataset
def cargar_telemetria(ruta_archivo: str) -> list[dict]:
    #Lee el archivo CSV con csv.DictReader 
    #Convierte tipos: int(id, ping, fps, intentos, reportes), float (duración), str(resto)
    #retorna una lista de diccionarios
    pass


#Qué debe hacer esta función? 
''' 
Debe abrir el archivo usando with open(...) con codificación utf-8,
Utilizar csv.DictReader para mapear automáticamente los nombres de columnas
Realizar el casteo explícito de los tipos de datos numéricos (no pueden quedar como strings)
Validar que el archivo exista y contenga al menos un registro (lanzar ValueError o mensaje amigable si está vacío.)

'''