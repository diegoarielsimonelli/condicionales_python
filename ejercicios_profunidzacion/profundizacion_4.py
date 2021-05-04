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
2 - Ordenar por cantidad de letras (longitud de la palabra)

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio

print("Ingrese una palabra")
palabra_1 = str(input())
print("Ingrese una segunda palabra")
palabra_2 = str(input())
print("Ingrese una tercer palabra")
palabra_3 = str(input())

print("Una vez ingresadas las 3 palabras: ¿Cómo quieres ordenarlas?\n Ingresa la opción 1 ó la opción 2: \n 1 - Ordenar por orden alfabético \n 2 - Ordenar por cantidad de letras")
opción= int(input())
palabras = [palabra_1, palabra_2, palabra_3]
palabras_alfabeto= sorted(palabras)
palabras_letras=sorted(palabras, key=len, reverse=True)
if opción == 1:
    print(palabras_alfabeto)
else:
 print(palabras_letras)