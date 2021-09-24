# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

texto_1 = '5'
texto_2 = '7'

# 1-Verifique cual de los dos textos es mayor alfabéticamente
# La comparación alfabética es aquella que se logra cuando
# se utiliza el operador mayor o menor con Strings (textos)
# Imprima en pantalla según corresponda

if texto_1 > texto_2:
    print("texto 1 es > texto 2")
elif texto_2 > texto_1:
    print("texto_2 es mayor a texto_1")
else:
    print("los 2 textos son iguales")

# 2-Transforma esas variables tipo texto en variables numéricas con (int)
# y almacénalas en nuevas variables.
# Compare las nuevas variables para ver cual es mayor o menor
# utilizando los operadores correspondientes
# ¿Cuál de las nuevas variables es mayor?
# Imprima en pantalla según corresponda
numero_1 = int(texto_1)
numero_2 = int(texto_2)

if numero_1 > numero_2:
    print("numero 1 es > numero 2")
elif numero_2 > numero_1:
    print("numero 2 es mayor a numero 1")
else:
    print("Los 2 numeros son iguales")

# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?
# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)
print (f"El numero de ordinal que esta asociado a texto_1 es = {ord(texto_1)}")
print (f"El numero de ordinal que esta asociado a texto_2 es = {ord(texto_2)}")