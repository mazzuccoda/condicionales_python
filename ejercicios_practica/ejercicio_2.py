# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda
if texto_1 > texto_2:
    print(f"{texto_1} es mayor a {texto_2}")
elif texto_2 > texto_1:
    print(f"{texto_2} es mayor a {texto_1}")
else:
    print("Los 2 textos ingresados son iguales")
# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda
if len(texto_1) > len(texto_2):
    print(f"{texto_1} tiene mas cantidad de letras que {texto_2}")
elif len(texto_2) > len(texto_1):
    print(f"{texto_2} tiene mas cantidad de letras que {texto_1}")
else:
    print("Los 2 textos tienen la mis")
# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

if texto_1[0] > texto_2[0]:
    print(f"La primera palabra de {texto_1} es mayor que la primera palabra de {texto_2}")
else:
    print(f"La primera palabra de {texto_1} no es mayor que la primera palabra de {texto_2}")

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda
if texto_1 == copia_texto_1:
    print("La condición que copia_texto_1 es igual que texto_1 es verdadera")
else:
    print("La condición que copia_texto_1 es igual que texto_1 es falsa")
# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda
if texto_2 == copia_texto_1:
    print("La condición que copia_texto_1 es igual que texto_1 es verdadera")
else:
    print("a condición que copia_texto_1 es igual que texto_1 es falsa")