'''
https://www.freecodecamp.org/espanol/news/11-proyectos-de-python-que-los-desarrolladores-junior-pueden-crear-para-practicar/
##########################################################
# CONTADOR  de palabras y letras
##########################################################
' ''

word = str(input("Por favor, introduce un texto: "))
word_list = []
contador = 1

for i in range(len(word)):
    word_list.insert(i,word[i:contador])
    contador += 1

print(f"Son {str(len(word) - word_list.count(' '))} Caracteres")
print(f"y {word_list.count(' ')+1} palabas")
'''



'''
##########################################################
ACRÓNIMOS!!!
##########################################################
    Entrada -> As Soon As Possible. Salida -> ASAP.
    Entrada -> World Health Organization. Salida -> WHO.
    Entrada -> Absent Without Leave. Salida -> AWOL.
' ''

frase = str(input("Introduce el nombre de tu empresa: "))
acronimo = frase[0]

blanco = 0
for i in frase:
    if i == ' ':
        blanco = 1
    elif blanco == 1:
        blanco = 0
        acronimo += i

print(f"[{acronimo}]")
'''

'''
##########################################################
Piedra Papel o Tijera
##########################################################
    piedra (puño cerrado)
    papel (mano plana)
    tijeras (un puño con el dedo índice y el dedo medio extendidos, formando una V)
' ''

from random import randint
 
choice = ["rock","paper","scissors"]
print("Welcome to the Rock, Paper, Scissors Game\n")

def main():
    computer = choice[randint(0,2)]
 
    player = input("Your Choice: ").lower()
    print("Computer Chose: " + computer)
 
    if player == computer:
        print("Draw")
    if player == computer:
        print("Draw")
    elif player == "rock" and computer == "paper":
        print("Computer Wins")
    elif player == "rock" and computer == "scissors":
        print("Player Wins")
    elif player == "paper" and computer == "rock":
        print("Player Wins")
    elif player == "paper" and computer == "scissors":
        print("Computer Wins")
    elif player == "scissors" and computer  == "rock":
        print("Computer Wins")
    elif player == "scissors" and computer == "paper":
        print("Player Wins")
    elif player == "end":
        print("Adios")
        return
 
    main()
 
main()
'''

'''
##########################################################
Adivina el número oculto
##########################################################
    Debemos de preguntar al usuario un número entre 1 y 50.
    Si añaden un número fuera de ese rango, vamos a indicar con un error que anime a elegir un número dentro del rango adecuado..
    Si no acertamos el número oculto, preguntaremos al usuario si queremos seguir jugando, introduciendo un nuevo número o queremos dejar de jugar.
    Finalmente, cuando el usuario acierta correctamente el número oculto, mostramos un mensaje de enhorabuena y mostramos el número de intentos que hemos utilizado para llegar a esta situación.
' ''

import random

continuar = 'S'
intentos = 0

while continuar == 'S':
    num_oculto = random.randint(1, 50)
    valor = int(input (f"Dame un número entre 1 y 50 ({num_oculto}): ") )
    intentos += 1

    if valor < 1 or valor > 50:
            print(f"El número {valor} no está dentro del rango entre 1 y 50, por favor Elige otro.")
    elif valor == num_oculto:
            print(f"Enhorabuena!!! El número {valor} es el número oculto!!")
            continuar = "N"
    elif valor != num_oculto:
            print(f"El número {valor} NO es el número oculto!!.")
            respuesta = str(input("¿Quieres continuar? ")).upper()
            if respuesta == "N":
                   continuar = "N"


print(f"Muchas gracias por participar con tus {intentos}")
'''

'''
##########################################################
Es palíndromo
##########################################################
    Animamos a los usuarios a introducir cinco palabras. Después comprobamos cuáles son palabras palíndromas o no.
    ¿Qué es un palíndromo? Es una palabra que podemos leer de la misma manera desde la izquierda a la derecha y viceversa.
' ''

palabras = []
num_palabras = 3
for x in range(num_palabras):
    palabra = str(input("Introduce la palabra Palindromo: ")).lower()
    palabras.append(palabra)

print(palabras)
print("")

for x in palabras:
    palindromo = x[::-1]
    if x == palindromo:
        print(f"{x} es un palindromo!!")
    else:
        print(f"{x} NO es un palindromo!! sería {palindromo}")
'''

'''
##########################################################
Calculador de propinas
##########################################################
    En este caso, nuestro objetivo es averiguar exactamente 
    la cantidad de propina que hay que proporcionar después 
    de un servicio. En este caso, hay que solicitar la 
    factura total. 
    Con esto, aplicaremos la propina para el 18%, 20% y 25%
' ''
propina = 0
tipo_propina = {"normal":   1.18,
                "buena":    1.20,
                "generosa": 1.25}
factura_total = float(input("Dime cual es la factura total: "))
mi_propina = ""

while mi_propina not in tipo_propina.keys():
    mi_propina = str(input(f"Que tipo de propina quieres dejar {list(tipo_propina.keys())}: ")).lower()

propina = factura_total * tipo_propina.get(mi_propina)

print(f"La factura total es de {factura_total}, la propina de {propina:,.2f}, por lo que en total hay que pagar {factura_total + propina:,.2f}")
'''

'''
##########################################################
Extractor de información del correo electrónico
##########################################################
    Recopile una dirección de correo electrónico del usuario y luego averigüe si el
    usuario tiene un nombre de dominio personalizado o un nombre de dominio popular.
' ''
dominios_genericos = ["gmail", "hotmail", "yahoo"]
continuar = True
nombre = "Luis"
dominio = "gmaile"

while continuar:
    mi_correo = str(input("Me pudes decir tu correo?: " )).lower()
    parte_anterior, _, parte_posterior = mi_correo.partition('@')
    print(parte_anterior, parte_posterior)
    if parte_anterior == "" or parte_posterior == "":
        print("Error en el correo")
    else:
        nombre, _, _ = parte_anterior.partition('.') # si no tiene "." coge todo.
        dominio, _, nodo = parte_posterior.partition('.')
        if nodo == "":
            print("Error en el correo2")
        else:
            continuar = False



print(f"Hola {nombre.capitalize()}, estoy viendo que tu email está registrado con {dominio.upper()}, ", "con un dominio genérico" if dominio in dominios_genericos else "que es un dominio privado")
'''


'''
##########################################################
Generador de letras
##########################################################
    Pedimos a un usuario que elija una canción de una lista de 10 canciones. 
    Cuando el usuario lo hace, imprime la letra de la canción que seleccionó.
'''
artistas =  {1: "Pink Floyd",
             2: "Beatles",
             3: "Queen"}
'''
letras = [[["Wish your are here", "Letra de: Wish your are here"], ["The Wall", "Letra de: The Wall"]], 
          [["Let it be", "Letra de: Let it be"]], 
          [["Heart attack", "Letra de: heart attack"]]
         ]
'''
letras = [[[1, {"Wish your are here": "Letra de: Wish your are here"}], [1, {"The Wall": "Letra de: The Wall"}]], 
          [[2, {"Let it be": "Letra de: Let it be"}],], 
          [[3, {"Heart attack": "Letra de: heart attack"}]]
         ]

artista = int(input(f"Elige un artista {artistas}: "))-1
cancion = 0
if len(letras[artista]) > 1:
    continuar = True
    while continuar:
        x = 1
        for cancion_letra in letras[artista]:
            print(f"{x} - {list(cancion_letra[1].keys())}")
            x += 1

        cancion = int(input(f"Elige una Canción {letras[artista]}: "))-1
        print("")
        if cancion >= 0 and cancion < len(letras[artista]):
            continuar = False
        else:
            print("No es una canción válida")

print(f"La letra de la canción elegida es: {list(letras[artista][cancion][1].values())}")
print("")
print("")
print("")