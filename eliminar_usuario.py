import csv

nombre_archivo = 'datos.csv'
numero_de_identificacion = int(input('Digite el numero de identificación: ')) # Índice de la fila a eliminar

# Lee todas las filas en memoria
with open(nombre_archivo, 'r', newline='') as f:
    lector_csv = csv.reader(f)
    encabezados = next(lector_csv) # Lee la primera fila como encabezados
    filas = list(lector_csv)

# Elimina la fila de la lista

for fila in filas:
    if fila[0]==numero_de_identificacion:
        fila_a_eliminar= fila.index(numero_de_identificacion)
        del filas[fila_a_eliminar]
        break


# Escribe las filas restantes de vuelta al archivo
with open(nombre_archivo, 'w', newline='') as f:
    escritor_csv = csv.writer(f)
    escritor_csv.writerows(filas)
    

