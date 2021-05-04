# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

texto_1 = '5'
texto_2 = '7'

# Verifique cual cual de los dos textos es mayor alfabéticamente
# Imprima en pantalla según corresponda
if texto_1 > texto_2:
    print(texto_1,"es mayor a", texto_2)
else:
    print(texto_1,"es menor a", texto_2)
# Transforma esas variables tipo texto y almacénalas
# en nuevas variables númericas (int)
# Repita el proceso, ¿Cuál de las nuevas variables es mayor?
# Imprima en pantalla según corresponda
if int (texto_1) >  int (texto_2):
     print( int (texto_1),"es mayor a", int (texto_2))
else:
    print( int (texto_1),"es menor a", int (texto_2))

# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?
# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)

'''
No puede encontrar la respuesta precisa en internet. 
Sin embargo, me parace que es porque python trata  a los caracteres numericos como los alfanumericos
de la misma forma, como si fueran numeros.En los sistemas informáticos, los datos son guardados como números y caracteres. 
Ocupan un espacio en el alfabeto que tiene guardado en su memoria.
Alt + 64 escribe el @, ocupa el lugar 64 de ese alfabeto, por ejemplo. 

'''