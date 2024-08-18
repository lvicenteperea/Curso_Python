from PyQt5.QtCore import QRect
from PyQt5.QtGui import QColor, QPainter

class Enemigo:
    def __init__(self, x, y, ancho=50, alto=50, velocidad=3, color="purple"):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.velocidad = velocidad
        self.color = QColor(color)
        self.rect = QRect(self.x, self.y, self.ancho, self.alto)

    def dibujar(self, painter: QPainter):
        # Dibujar el enemigo
        painter.setBrush(self.color)
        painter.drawRect(self.rect)
        
        # Actualizar la posición del rectángulo
        self.rect.moveTo(self.x, self.y)

    def mover(self):
        self.y += self.velocidad
        self.rect.moveTo(self.x, self.y)
