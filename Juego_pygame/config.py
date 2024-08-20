import pygame 

ANCHO = 1000
ALTO = 800
LIMITE_SUP = 30
TAM_FUENTE = 20
FONDO_PANTALLA = "black"
SEPARADOR = ";"

VIDAS = 5
DEFENSOR_VELOCIDAD = 5     # cuanto MAYOR sea el número, mas rápido irá EL DEFENSOR!!

ENEMIGOS_FPS = 60           # cuanto MAYOR sea el número, mas rápido irán los bichos!!
TIEMPO_ENTRE_ENEMIGOS = 700 # cuanto MENOR sea el número, mas bichos saldrán!!

TIEMPO_ENTRE_BALAS = 70    # cuanto MENOR sea el número, mas rápido saldrán las balas!!
BALA_ANCHO = 4
BALA_ALTO = 6
BALA_VELOCIDAD = 10         # cuanto MAYOR sea el número, mas rápido irán las balas!!
BALA_COLOR = "white"

DIR_IMG = "./Juego_pygame/imagenes/"
DIR_DAT = "./Juego_pygame/ficheros/"
DIR_SONIDOS = "./Juego_pygame/media/"

SONIDO_LASER = f"{DIR_SONIDOS}disparo_laser.wav"
SONIDO_KO_ENEMIGO = f"{DIR_SONIDOS}muerte_enemigo.wav"
SONIDO_QUITA_VIDA = f"{DIR_SONIDOS}quita_vida.wav"

