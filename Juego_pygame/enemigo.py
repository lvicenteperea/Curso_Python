import pygame
from ventana import Ventana
from config import DIR_IMG, SONIDO_KO_ENEMIGO


class Enemigo:
    def __init__(self, x, y, ancho = 50, alto = 50, velocidad = 3, color = "purple") -> None:
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.velocidad = velocidad
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.imagen = pygame.image.load(f"{DIR_IMG}enemigo.png")
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
        # self.imagen = pygame.transform.rotate(self.imagen, 90)

    def dibujar(self, ventana: Ventana):
        pygame.draw.rect(ventana.marco, self.color, self.rect)
        # self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        
        ventana.dibujar_obj(self)


    def mover(self):
        self.y += self.velocidad

    def muerte(self, enemigos: dict):
        enemigos.remove(self)

        SONIDO_BALA = pygame.mixer.Sound(SONIDO_KO_ENEMIGO)
        SONIDO_BALA.play()