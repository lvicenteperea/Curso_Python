import pygame
from config import TIEMPO_ENTRE_BALAS, BALA_ANCHO, BALA_ALTO, BALA_VELOCIDAD, BALA_COLOR


class Bala:
    def __init__(self, x, y, ancho = BALA_ANCHO, alto = BALA_ALTO, velocidad = BALA_VELOCIDAD, color = BALA_COLOR) -> None:
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.velocidad = velocidad
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.color, self.rect )
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def mover(self):
        self.y -= self.velocidad

class Balas:
    def __init__(self, tiempo_entre_balas = TIEMPO_ENTRE_BALAS) -> None:
        self.diccionario = []
        self.ultima_bala = 0
        self.tiempo_entre_balas = tiempo_entre_balas


    def crear_bala(self, defensor, balas):
        if pygame.time.get_ticks() - balas.ultima_bala > TIEMPO_ENTRE_BALAS:
            balas.diccionario.append(Bala(defensor.rect.centerx, defensor.rect.centery))
            balas.ultima_bala = pygame.time.get_ticks()