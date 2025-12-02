#Tienes una lista con el orden de canciones de una playlist.
#Escribe un programa que pida al usuario un número n y rote la lista de canciones n posiciones a la derecha

#enumerate() = genera pares (número, elemento)
#for i, s in ... = recorre esos pares
#(f"{i}. {s}") = muestra el número y el nombre bonito

playlist = ["los cuatro A", "ahi ahi B", "perro viejo C", "hecha pa mi D"]
n = int(input("¿Cuántas posiciones rotar a la derecha? ")) % len(playlist)
rotada = playlist[-n:] + playlist[:-n]
print("\n Playlist rotada:")
for i, s in enumerate(rotada, 1): print(f"{i}. {s}")

# Lista de ingredientes originales
ingredientes = ["tomate", "cebolla", "pimiento", "aceite", "ajo", "sal", "pimienta"]

print("Ingredientes originales:")
print(", ".join(ingredientes))

# Pedimos al usuario los ingredientes que no quiere
prohibidos = input("\nEscribe los ingredientes que NO quieres (separados por coma): ")

# Convertimos la entrada en lista y quitamos espacios extra
prohibidos = [x.strip() for x in prohibidos.split(",")]

# Generamos nueva lista eliminando los prohibidos
nueva_lista = [i for i in ingredientes if i not in prohibidos]

print("\n Nueva lista de ingredientes:")
print(", ".join(nueva_lista))





