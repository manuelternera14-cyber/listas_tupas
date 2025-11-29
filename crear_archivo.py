import csv # importar el formato csv valores separados por comas

with open ("datos.csv", "w", newline ="",  encoding='utf-8') as archivo:
    escritor = csv.writer(archivo) #crear un escritor
    escritor.writerow(['id', 'nombre_usuario','correo_de_usuario', 'contraseña'])

