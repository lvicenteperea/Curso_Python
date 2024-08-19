import pygame
from config import ANCHO


class Cubo:
    def __init__(self, x, y, ancho = 35, alto = 35, velocidad = 10, color = "red") -> None:
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.velocidad = velocidad
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.imagen = pygame.image.load("./Juego_pygame/defensor.svg")
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
        self.imagen = pygame.transform.rotate(self.imagen, 90)


    def dibujar(self, ventana):
        if self.x > ANCHO:
            self.x = 0
        elif self.x < 0:
            self.x = ANCHO

        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        pygame.draw.rect(ventana, self.color, self.rect)
        ventana.blit(self.imagen, self.x, self.y)