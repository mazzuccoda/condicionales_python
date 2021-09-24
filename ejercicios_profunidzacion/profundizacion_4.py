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

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio
palabra_1 = str(input("Ingrese la primera palabra\n"))
palabra_2 = str(input("Ingreso la segunda palabra\n"))
palabra_3 = str(input("Ingreso la tercer palabra\n"))

print("Ingrese como desea ordenar estas palabra")
print("si se ingresa 1 se ordenaran las 3 palabras por orden alfabético")
print("Si se ingresa 2 se ordenaran las 3 palabras por cantidad de letras")
orden = int(input("Ingreso la tercer palabra\n"))

alf_1 = ""
alf_2 = ""
alf_3 = "" 
cant_1 = ""
cant_2 = ""
cant_3 = ""

#selecciono la primera en orden alfabetico
if palabra_1[0] >= palabra_2[0] and palabra_1[0] >= palabra_3[0]:
    alf_3 = palabra_1
elif palabra_2[0] >= palabra_1 and palabra_2[0] >= palabra_3[0]:
    alf_3 = palabra_2
elif palabra_3[0] >= palabra_1[0] and palabra_3[0] >= palabra_2[0]:
    alf_3 = palabra_3


#selecciono la segunda en orden alfabetico
if palabra_1[0] >= palabra_2[0] and palabra_1[0] <= palabra_3[0]:
    alf_2 = palabra_1
elif palabra_2[0] >= palabra_1 and palabra_2[0] <= palabra_3[0]:
    alf_2 = palabra_2
elif palabra_3[0] >= palabra_1[0] and palabra_3[0] <= palabra_2[0]:
    alf_2 = palabra_3


#selecciono la tercera en orden alfabetico
if palabra_1[0] <= palabra_2[0] and palabra_1[0] <= palabra_3[0]:
    alf_1 = palabra_1
elif palabra_2[0] <= palabra_1 and palabra_2[0] <= palabra_3[0]:
    alf_1 = palabra_2
elif palabra_3[0] <= palabra_1[0] and palabra_3[0] <= palabra_2[0]:
    alf_1 = palabra_3

#selecciono la primera por cantidad de letras
if len(palabra_1) >= len(palabra_2) and len(palabra_1)>= len(palabra_3):
    cant_1 = palabra_1
elif len(palabra_2) >= len(palabra_1) and len(palabra_2) >= len(palabra_3):
    cant_1= palabra_2
elif len(palabra_3) >= len(palabra_1) and len(palabra_3) >= len(palabra_2):
    cant_1 = palabra_3


#selecciono la segunda por cantidad de letras
if len(palabra_1) >= len(palabra_2) and len(palabra_1) <= len(palabra_3):
    cant_2 = palabra_1
elif len(palabra_2) >= len(palabra_1) and len(palabra_2[0]) <= len(palabra_3):
    cant_2= palabra_2
elif len(palabra_3) >= len(palabra_1) and len(palabra_3) <= len(palabra_2):
    cant_2 = palabra_3

#selecciono la tercera por cantidad de letras
if len(palabra_1) <= len(palabra_2) and len(palabra_1) <= len(palabra_3):
    cant_3 = palabra_1
elif len(palabra_2) <= len(palabra_1) and len(palabra_2) <= len(palabra_3):
    cant_3 = palabra_2
elif len(palabra_3) <= len(palabra_1) and len(palabra_3) <= len(palabra_2):
    cant_3 = palabra_3

if orden == 1:
    print(alf_1)
    print(alf_2)
    print(alf_3)
else:
    print(cant_1)
    print(cant_2)
    print(cant_3)