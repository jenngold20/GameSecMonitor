#Consigna 5: Módulo main.py — Interfaz de Consola y Reporte Final 
#El archivo main.py debe presentar un menú interactivo en consola mediante un bucle while:

import carga
import procesamiento

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


def mostrar_estadisticas(sesiones: list[dict]):
    estadisticas = procesamiento.calcular_estadisticas_globales(sesiones)
    print()
    print("--- ESTADÍSTICAS GLOBALES ---")
    print("Total de sesiones:", estadisticas["total_sesiones"])
    print("Ping promedio:", estadisticas["ping_promedio"], "ms")
    print("Duración promedio:", estadisticas["duracion_promedio"], "min")
    print("Porcentaje competitivas/torneo:", estadisticas["porcentaje_competitivas"], "%")


def mostrar_por_servidor(sesiones: list[dict]):
    servidores = procesamiento.analizar_por_servidor(sesiones)
    print()
    print("--- RENDIMIENTO POR SERVIDOR ---")
    for servidor in servidores:
        datos = servidores[servidor]
        print(servidor, "->", datos["cantidad"], "sesiones | ping:", datos["ping_promedio"],
              "ms | fps:", datos["fps_promedio"])


def mostrar_incidentes(sesiones: list[dict]):
    resumen, criticos = procesamiento.clasificar_incidentes(sesiones)
    sospechosos = procesamiento.obtener_sospechosos(sesiones)

    print()
    print("--- AUDITORÍA DE SEGURIDAD ---")
    print("Normales:", resumen["Normal"])
    print("Sospechosos:", resumen["Sospechoso"])
    print("Críticos:", resumen["Crítico"])

    print()
    print("Sesiones críticas:")
    for evento in criticos:
        print("  [!] Sesión #" + str(evento["id_sesion"]), "|", evento["jugador_id"], "|", evento["servidor"])
        print("      Motivo:", evento["motivo"])

    print()
    print("Sesiones sospechosas:")
    for sesion in sospechosos:
        print("  [?] Sesión #" + str(sesion["id_sesion"]), "|", sesion["jugador_id"], "|", sesion["servidor"],
              "| ping:", sesion["ping_promedio"], "| intentos:", sesion["intentos_fallidos"],
              "| reportes:", sesion["reportes_trampa"])


def exportar_reporte(sesiones: list[dict], ruta_salida: str = "reporte_gamesec.txt", fecha: str = "") -> str:
    estadisticas = procesamiento.calcular_estadisticas_globales(sesiones)
    servidores = procesamiento.analizar_por_servidor(sesiones)
    resumen, criticos = procesamiento.clasificar_incidentes(sesiones)
    total = estadisticas["total_sesiones"]

    linea_doble = "=" * 70
    linea_simple = "-" * 70

    # voy guardando cada renglon del reporte en una lista y despues lo escribo todo junto
    lineas = []
    lineas.append(linea_doble)
    lineas.append("              REPORTE DE AUDITORÍA Y TELEMETRÍA — GAMESEC")
    lineas.append(linea_doble)
    lineas.append("Fecha de generación: " + fecha)
    lineas.append("")

    lineas.append("[1] RESUMEN GLOBAL OPERATIVO")
    lineas.append(linea_simple)
    lineas.append("Total de sesiones procesadas: " + str(total))
    lineas.append(f"Ping promedio global: {estadisticas['ping_promedio']:.2f} ms")
    lineas.append(f"Duración media de partida: {estadisticas['duracion_promedio']:.2f} min")
    lineas.append(f"Partidas de alta competencia (Ranked/Torneo): {estadisticas['porcentaje_competitivas']:.2f}%")
    lineas.append("")

    lineas.append("[2] RENDIMIENTO REGIONAL POR SERVIDOR")
    lineas.append(linea_simple)
    lineas.append("Servidor           | Sesiones | Ping Promedio | FPS Promedio")
    lineas.append(linea_simple)
    for servidor in servidores:
        datos = servidores[servidor]
        ping = f"{datos['ping_promedio']:.2f} ms"
        fps = f"{datos['fps_promedio']:.2f} fps"
        lineas.append(f"{servidor:<18} | {datos['cantidad']:<8} | {ping:<13} | {fps}")
    lineas.append("")

    lineas.append("[3] AUDITORÍA DE SEGURIDAD E INCIDENTES")
    lineas.append(linea_simple)
    lineas.append("Distribución de estados de seguridad:")
    lineas.append(f"  • Normales:    {resumen['Normal']:>3} sesiones ({resumen['Normal'] * 100 / total:5.2f}%)")
    lineas.append(f"  • Sospechosos: {resumen['Sospechoso']:>3} sesiones ({resumen['Sospechoso'] * 100 / total:5.2f}%)")
    lineas.append(f"  • Críticos:    {resumen['Crítico']:>3} sesiones ({resumen['Crítico'] * 100 / total:5.2f}%)")
    lineas.append("")
    lineas.append("Detalle de Sesiones Críticas Detectadas:")
    for evento in criticos:
        id_texto = "#" + str(evento["id_sesion"])
        lineas.append(f"  [!] Sesión {id_texto:<4} | Jugador: {evento['jugador_id']} | Servidor: {evento['servidor']}")
        lineas.append("      Motivo: " + evento["motivo"])
    lineas.append("")

    lineas.append("[4] CONCLUSIONES TÉCNICAS DEL EQUIPO")
    lineas.append(linea_simple)
    lineas.append("1. Los servidores de Sudamérica (SA-SaoPaulo y SA-BuenosAires) tienen el menor ping")
    lineas.append("   promedio (menos de 80 ms), mientras que NA-Virginia supera los 220 ms y EU-Frankfurt")
    lineas.append("   ronda los 200 ms. La experiencia de juego es mucho mejor en las regiones más cercanas.")
    lineas.append("2. Todas las sesiones críticas cumplen las dos condiciones a la vez (muchos reportes y")
    lineas.append("   muchos intentos fallidos), y 7 de las 10 ocurrieron en partidas Competitivas, donde")
    lineas.append("   hay más incentivo para hacer trampa.")
    lineas.append("3. NA-Virginia concentra la mitad de las sesiones sospechosas (11 de 22), en gran parte")
    lineas.append("   por combinar ping alto con intentos fallidos, lo que podría indicar lag switching.")
    lineas.append("   Conviene revisar ese servidor con más detalle.")
    lineas.append(linea_doble)
    lineas.append("                       FIN DEL REPORTE GAMESEC")
    lineas.append(linea_doble)

    with open(ruta_salida, "w", encoding="utf-8") as archivo:
        for linea in lineas:
            archivo.write(linea + "\n")

    return ruta_salida





def main():
    # la lista arranca vacia hasta que se use la opcion 1
    sesiones = []
    opcion = ""
    
    while opcion != "6":
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            try:
                sesiones = carga.cargar_telemetria("gamesec_logs.csv")
                print("Dataset cargado correctamente:", len(sesiones), "registros.")
            except ValueError as error:
                print("Error:", error)

        elif opcion in ["2", "3", "4", "5"] and len(sesiones) == 0:
            print("Primero tiene que cargar el dataset (opción 1).")

        elif opcion == "2":
            mostrar_estadisticas(sesiones)

        elif opcion == "3":
            mostrar_por_servidor(sesiones)

        elif opcion == "4":
            mostrar_incidentes(sesiones)

        elif opcion == "5":
            fecha = input("Ingrese la fecha de hoy (dd/mm/aaaa): ").strip()
            ruta = exportar_reporte(sesiones, "reporte_gamesec.txt", fecha)
            print("Reporte generado en", ruta)

        elif opcion == "6":
            print("Saliendo del programa...")

        else:
            print("Opción inválida, intente de nuevo.")



main()
