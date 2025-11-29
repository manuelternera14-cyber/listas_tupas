import csv

with open('datos.csv', mode='r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    encabezados = next(lector_csv) # Lee la primera fila como encabezados
    for fila in lector_csv:
        print(fila) # cada fila es una lista