#===================================
#OPERADORES EN PYTHON
print("===========OPERADORES ARITMETICOS===========")
a = 10
b = 5
print(f"la suma de a mas b es igual:" ,a + b)
print(f"la resta de a menos b es igual a:", a-b)
print(f"la multiplicación de a por b es igual a:", a*b)
print(f"la divisió de a y b es igual a:", a/b)
print("============OPERADORES RELACIONALES=========")
print(" a == b", a==b) # == es para comparar relaciones identicas
print(" a != b", a!=b) # != significa diferente o relacion de diferencia
print( "a < b" ,a < b) # Relación menor que <
print("a > b", a > b) # Relación mayor que >
print(" a <= b", a <= b) #Relaciones Menores o iguales
print(" a >= b", a >= b) # Relaciones Mayores o iguales 
print(" ============OPERADORES LÓGICOS ========")
x = True
y = False
#AND
print("x AND Y", x and y)
print("x OR Y", x or y)
print("x NOT Y", x is not y)
print("===============OPERADORES UNARIOS========= ")
z = 7
print ("z es positivo",{+z}) # para designar valores positivos
print ("z es negativo", {-z}) # Valores Negativos
print ("not (z > 0)", { not (z > 0)})
print ("not (z > 0)", { not (-z > 0)})
