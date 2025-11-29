#=============FORMULARIO================
print ("FORMULARIO DE USUARIOS")
nombre = input("Ingrese su nombre número uno")
nombre2 = input("Ingrese su nombre numero dos")
apellido = input("Ingrese su apellido")
apellido2 = input("Ingrese su apellido dos")
print ("el nombre completo es",nombre + " " + nombre2 + " " + apellido + " " +apellido2)

#===============DATOS NUMERICOS=========
edad =int(input("ingrese su edad"))
print("Edad:", 19)
peso =float(input("Ingresa su peso"))
print("Peso:", 90"kg")
telefono =int(input("ingrese su telefono"))
altura =float(input ("ingrese su altura"))
hijos =int(input("ingrese el numero de hijos"))
año_nacimiento=int(input("ingrese su año de nacimiento"))
mes_nacimiento=int(input("ingrese su mes de nacimiento"))
dia_nacimiento=int(input("ingrese su dia de nacimiento"))
cedula=int(input("ingrese su numero de cedula"))
#==============DATOS TEXTO O STRING=============
correo = input("ingrese su correo")
tipo_sangre=input("ingrese su tipo de sangre")
genero = input("ingrese su genero")
estado = input("ingrese si es casada o soltera")
eps=input("ingrese su eps")
universidad = input("ingrese su universidad")
carrera = input("ingrese su carrera")





#============== MOSTRAR DATOS ==============
print("\n===== DATOS PERSONALES =====")
print("Edad:", edad)
print("Peso:", peso, "kg")
print("Teléfono:", telefono)
print("Altura:", altura, "m")
print("Número de hijos:", hijos)
print("Fecha de nacimiento:", dia_nacimiento, "/", mes_nacimiento, "/", año_nacimiento)
print("Cédula:", cedula)

print("\n===== DATOS ADICIONALES =====")
print("Correo:", correo)
print("Tipo de sangre:", tipo_sangre)
print("Género:", genero)
print("Estado civil:", estado)
print("EPS:", eps)
print("Universidad:", universidad)
print("Carrera:", carrera)