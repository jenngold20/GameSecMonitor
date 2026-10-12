#Consigna 5: Módulo main.py — Interfaz de Consola y Reporte Final 
#El archivo main.py debe presentar un menú interactivo en consola mediante un bucle while:

'''
========================================= 
      GAMESEC MONITOR - PANEL DE CONTROL 
========================================= 
1. Cargar y validar dataset 
2. Ver estadísticas globales de servidores 
3. Ver rendimiento por región de servidor 
4. Auditar incidentes de seguridad (Críticos y Sospechosos) 
5. Exportar reporte consolidado (reporte_gamesec.txt) 
6. Salir 
========================================= 
Seleccione una opción: 




Asimismo, la opción 5 debe invocar a la función exportar_reporte(sesiones, 
ruta_salida='reporte_gamesec.txt') para escribir un informe estructurado que consolide todos los análisis 
realizados.

'''

def mostrar_menu():
    print()
    print("=========================================")
    print("    GAMESEC MONITOR - PANEL DE CONTROL")
    print("=========================================")
    print("1. Cargar y validar dataset")
    print("2. Ver estadísticas globales de servidores")
    print("3. Ver rendimiento por región de servidor")
    print("4. Auditar incidentes de seguridad (Críticos y Sospechosos)")
    print("5. Exportar reporte consolidado (reporte_gamesec.txt)")
    print("6. Salir")
    print("=========================================")



def main():
    # la lista arranca vacia hasta que se use la opcion 1
    sesiones = []
    opcion = ""

    while opcion != "6":
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
             print("Opción 1")

        elif opcion == "2":
            print("Opción 2")

        elif opcion == "3":
            print("Opción 3")

        elif opcion == "4":
           print("Opción 4")

        elif opcion == "5":
            print("Opción 5")
            
        elif opcion == "6":
            print("Saliendo del programa...")

        else:
            print("Opción inválida, intente de nuevo.")


main()
