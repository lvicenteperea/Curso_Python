from PyQt5.QtCore import QRect
from PyQt5.QtGui import QColor, QPainter
from config import ANCHO

class Cubo:
    def __init__(self, x, y, ancho=35, alto=35, velocidad=10, color="red"):
        self.x = int(x)
        self.y = int(y)
        self.ancho = int(ancho)
        self.alto = int(alto)
        self.velocidad = int(velocidad)
        self.color = QColor(color)
        self.rect = QRect(self.x, self.y, self.ancho, self.alto)

    def dibujar(self, painter: QPainter):
        # Dibujar el cubo
        painter.setBrush(self.color)
        painter.drawRect(self.rect)
        
        # Reposicionar si se sale de los bordes
        if self.x > ANCHO:
            self.x = 0
        elif self.x < 0:
            self.x = ANCHO
        self.rect.moveTo(self.x, self.y)

    def mover_izquierda(self):
        self.x -= self.velocidad
        self.rect.moveTo(self.x, self.y)

    def mover_derecha(self):
        self.x += self.velocidad
        self.rect.moveTo(self.x, self.y)
