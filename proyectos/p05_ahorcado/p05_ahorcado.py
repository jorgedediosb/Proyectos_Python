# Proyecto "Juego del ahorcado"
'''
El juego elige una palabra al azar de una lista.
El jugador debe adivinarla en 6 intentos.
'''

from random import choice
import os

palabras = ['panadero', 'dinosaurio', 'helipuerto', 'tiburon']
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False

# Limpiar consola cada vez que se escribe una nueva letra
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))

    return palabra_elegida, letras_unicas

def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input("Elige una letra: ")
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("No has elegido una letra correcta")

    return letra_elegida

def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []

    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')

    print(' '.join(lista_oculta))

def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):

    fin = False

    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        # añadiendo 'not in' se evita bug al elegir siempre la misma letra y finalice el juego
        letras_correctas.append(letra_elegida)
        coincidencias += 1

    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print(input("Ya has encontrado esa letra.\nPrueba con otra (pulsa ENTER)"))
    elif letra_elegida not in palabra_oculta:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1
    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)

    return vidas, fin, coincidencias

def perder():
    print("Te has quedado sin vidas")
    print(input("La palabra oculta era: " + palabra))

    return True

def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print(input("Felicitaciones, has encontrado la palabra!!!"))

    return True

palabra, letras_unicas = elegir_palabra(palabras)

while not juego_terminado:
    print('\n' + '*' * 40)
    print("¡Bienvenido al juego del ahorcado!")
    print('*' * 40 + '\n' + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print('Letras incorrectas: ' + '-'.join(letras_incorrectas))
    print(f'Vidas: {intentos}')
    print('\n' + '*' * 40 + '\n')
    letra = pedir_letra()
    
    intentos, terminado, aciertos = chequear_letra(letra,palabra,intentos,aciertos)
    juego_terminado = terminado
    limpiar_consola()

    #Preguntar al usuario si quiere volver a jugar
    if juego_terminado:
        respuesta = input("Deseas volver a jugar? (s/n): ")
        if respuesta.lower() == 's':
            #reiniciar juego
            palabra, letras_unicas = elegir_palabra(palabras)
            letras_correctas = []
            letras_incorrectas = []
            intentos = 6
            acierto = 0
            juego_terminado = False
        else:
            break
'''
Base de datos con todas las palabras:
1º Crear base de datos en archivo de texto con las palabras (cada una en una línea).
2º Lee el archivo de texto y almacena todas las palabras en una lista.
3º Utilizar la función  random.choice()  para seleccionar una palabra aleatoria de la lista.
Ejemplo:

import random
 def obtener_palabra_aleatoria():
    with open("base_de_datos.txt", "r") as archivo:
        palabras = archivo.readlines()
     palabra_secreta = random.choice(palabras).strip()
    return palabra_secreta
 palabra_secreta = obtener_palabra_aleatoria()
jugar(palabra_secreta)
'''