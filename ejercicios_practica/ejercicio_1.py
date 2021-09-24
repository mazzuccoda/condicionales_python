# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos

numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda
print("#################################################################")
print("Que numero es mayor??")

if numero_1 > numero_2:
    print("{} es Mayor que {}".format(numero_1,numero_2))
elif numero_1 < numero_2:
    print("{} es Mayor que {}".format(numero_2,numero_1))
else: 
    print("Los dos numeros son iguales")
# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso
print("#################################################################")
print("El primer numero ingresado, es positivo, negativo o 0??")


if numero_1 > 0:
    print("{} es positivo".format(numero_1))
elif numero_1 < 0:
    print("{} es Negativo".format(numero_1))
else:
    print("El numero ingresado es 0")
# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición

print("#################################################################")
print("El primer numero ingresado, es mayor a 0 y menor a 100??")


if numero_1 > 0 and numero_1 < 100:
    print(f"La condicion es verdadera, ya que {numero_1} es mayor que 0 y menor que 100")
else:
    print(f"{numero_1} no cumple la condicion de ser mayor que 0 y menor que 100")
# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
print("#################################################################")
print(f"A continuación se va a verificar si {numero_1} < 10 ó que {numero_2} sea > -2")

if  numero_1 < 10 or numero_2 > -2:
    if numero_1 < 10 and numero_2 >-2:
        print("Cumple la condición ya que se cumplen las 2 condiciones")
    elif numero_1 < 10:
        print(f"Cumple la condición ya que {numero_1} < 10")
    else:
        print(f"Cumple la condición ya que {numero_2} es > a -2") 
else:
    print(f"{numero_1} y {numero_2} no cumple ninguna condicion")




