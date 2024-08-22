import pygame
from config import ANCHO, DIR_IMG, VIDAS, DEFENSOR_VELOCIDAD, SONIDO_QUITA_VIDA
from ventana import Ventana
from bala import Bala
from enemigo import Enemigo

class Cubo:
    #------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------
    def __init__(self, x, y, ancho = 50, alto = 50, velocidad = DEFENSOR_VELOCIDAD, color = "red") -> None:
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.velocidad = velocidad
        self.color = color
        self.vida = VIDAS
        self.puntos = 0
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.imagen = pygame.image.load(f"{DIR_IMG}defensor2.webp")
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
        # self.imagen = pygame.transform.rotate(self.imagen, 90)

    #------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------
    def dibujar(self, ventana: Ventana):
        if self.x > ANCHO:
            self.x = 0
        elif self.x < 0:
            self.x = ANCHO

        ventana.dibujar_obj(self)

        # self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        # # pygame.draw.rect(ventana.marco, self.color, self.rect)
        # ventana.marco.blit(self.imagen, (self.x, self.y))

    #------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------
    def quita_vida(self, vidas = 1):
        self.vida -= vidas
        
        SONIDO_BALA = pygame.mixer.Sound(SONIDO_QUITA_VIDA)
        SONIDO_BALA.play()
        
        return self.vida


    #------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------
    def suma_puntos(self, puntos) -> int:
        self.puntos += puntos
        return self.puntos

    #------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------
    def elimina_enemigo(self, enemigos: dict, enemigo: Enemigo, balas_diccionario: dict, bala: Bala):
        self.suma_puntos(5)
        # enemigos.remove(enemigo)
        enemigo.muerte(enemigos)
        balas_diccionario.remove(bala)

    def aumenta_velocidad(self, miliseg = 3):
        if self.velocidad < 18:
            self.velocidad += miliseg
