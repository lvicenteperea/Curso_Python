import pygame


class Enemigo:
    def __init__(self, x, y, ancho = 50, alto = 50, velocidad = 3, color = "purple") -> None:
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.velocidad = velocidad
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.color, self.rect)
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def mover(self):
        self.y += self.velocidad