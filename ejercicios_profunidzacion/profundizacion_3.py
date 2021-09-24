# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
numero_1 = float(input("Ingrese el primer registro de temperatura\n"))
numero_2 = float(input("Ingreso el segundo registro de temperatura\n"))
numero_3 = float(input("Ingreso el tercer registro de temperatura\n"))

maximo = 0 
minimo = 0
promedio = 0
if numero_1 > numero_2 and numero_1 > numero_3:
    maximo = numero_1
elif numero_2 > numero_1 and numero_2 > numero_3:
    maximo = numero_2
elif numero_3 > numero_1 and numero_3 > numero_2:
    maximo = numero_3
else:
    print("Todos los numeros ingresados son iguales") 


if numero_1 < numero_2 and numero_1 < numero_3:
    minimo = numero_1
elif numero_2 < numero_1 and numero_2 < numero_3:
    minimo = numero_2
elif numero_3 < numero_1 and numero_3 < numero_2:
    minimo = numero_3
else:
    print("Todos los numeros ingresados son iguales")

promedio = (numero_1+numero_2+numero_3)/3
print("La maxima temperatura registrada es", maximo)
print("La minima temperatura registrada es", minimo)
print("El promedio de temperatura registrada es", round(promedio,2))