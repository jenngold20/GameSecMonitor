# TP Integrador - GameSec Monitor

Taller de Programación I - UNAHUR - 2026

## Integrantes

Tecnicatura Universitaria en Inteligencia Artificial.

- Belio Gastón
- Goldfeld Jennifer
- Heemskerk Lucas
- Tedesco Milene

## Como se usa

Hay que abrir una consola en la carpeta del tp y poner:

```
python main.py
```

Primero hay que elegir la opcion 1 para cargar el csv, si no el programa no deja usar las otras opciones.
Con la opcion 5 se genera el archivo reporte_gamesec.txt en la misma carpeta (pide que escribas la fecha).

## Que hay en cada archivo

- carga.py: lee el gamesec_logs.csv, pasa los datos a int y float y se fija que el archivo exista y no este vacio.
- procesamiento.py: calcula las estadisticas generales, agrupa los datos por servidor y clasifica las sesiones en normal, sospechoso o critico.
- main.py: tiene el menu y la funcion que arma el reporte.
- gamesec_logs.csv: dataset brindado por la cátedra.

No usamos pandas ni numpy, solo csv y os que vienen con python.
