  #Suma de dos números: Pide dos números y muestra su suma.
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
print("La suma es:", a + b)
   
   
#Área del triángulo: Calcula el área de un triángulo con base y altura ingresado por el usuario
base = float(input("Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))
area = (base * altura) / 2
print("El área del triángulo es:", area)

#5. Potencia: Calcula xyx^yxy usando el operador **.
x = float(input("Ingresa el número base: "))
y = float(input("Ingresa el exponente: "))
print("El resultado de x^y es:", x ** y)

7. #Verificar edad: Pide la edad y muestra si la persona es mayor de
edad (18).
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")


8. #Comparar cadenas: Pide dos cadenas y verifica si son iguales.
texto1 = input("Ingresa la primera cadena: ")
texto2 = input("Ingresa la segunda cadena: ")

if texto1 == texto2:
    print("Las cadenas son iguales.")
else:
    print("Las cadenas son diferentes.")

#11. Acceso permitido: Solicita usuario y contraseña y valida si ambos

#son correctos usando and
usuario = input("Usuario: ")
contraseña = input("Contraseña: ")

if usuario == "admin" and contraseña == "1234":
    print("Acceso permitido.")
else:
    print("Acceso denegado.")

 
 #13. Verificación múltiple: Pide tres valores booleanos e imprime si al

#menos uno es True (usa or).
a = bool(int(input("Valor 1 (1=True, 0=False): ")))
b = bool(int(input("Valor 2 (1=True, 0=False): ")))
c = bool(int(input("Valor 3 (1=True, 0=False): ")))

if a or b or c:
    print("Al menos uno es True.")
else:
    print("Todos son False.")

#15. Combinación: Determina si un número está entre 10 y 50 y es par al mismo tiempo
num = int(input("Ingresa un número: "))
if 10 <= num <= 50 and num % 2 == 0:
    print("El número está entre 10 y 50 y es par.")
else:
    print("No cumple las condiciones.")

