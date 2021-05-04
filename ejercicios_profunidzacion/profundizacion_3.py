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
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

print("Ingrese el primer valor de temperatura")
temperatura_1 = float(input())
print("Ingrese el segundo valor de temperatura")
temperatura_2 = float(input())
print("Ingrese el tercer valor de temperatura")
temperatura_3 = float(input())

promedio= (temperatura_1 + temperatura_2 + temperatura_3)/3

if temperatura_1 > temperatura_2 and temperatura_1 > temperatura_3:
    print("la temperatura mayor es", temperatura_1)
elif  temperatura_2 > temperatura_1 and temperatura_2 > temperatura_3:
    print("la temperatura mayor es", temperatura_2)
elif  temperatura_3 > temperatura_1 and temperatura_3 > temperatura_2:
    print("la temperatura mayor es", temperatura_3)

if temperatura_1 < temperatura_2 and temperatura_1 < temperatura_3:
    print ("la menor temperatura es", temperatura_1)
elif temperatura_2 < temperatura_1 and temperatura_2 < temperatura_3:
    print ("la menor temperatura es", temperatura_2)
elif temperatura_3 < temperatura_1 and temperatura_3 < temperatura_2:
    print ("la menor temperatura es", temperatura_3)

print("el promedio es", promedio)