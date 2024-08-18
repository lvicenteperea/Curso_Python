from PyQt5.QtCore import QRect
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtCore import QTime
from config import TIEMPO_ENTRE_BALAS, BALA_ANCHO, BALA_ALTO, BALA_VELOCIDAD, BALA_COLOR

class Bala:
    def __init__(self, x, y, ancho=BALA_ANCHO, alto=BALA_ALTO, velocidad=BALA_VELOCIDAD, color=BALA_COLOR):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.velocidad = velocidad
        self.color = QColor(color)
        self.rect = QRect(self.x, self.y, self.ancho, self.alto)

    def dibujar(self, painter: QPainter):
        # Dibujar la bala
        painter.setBrush(self.color)
        painter.drawRect(self.rect)
        
        # Actualizar la posición del rectángulo
        self.rect.moveTo(self.x, self.y)

    def mover(self):
        self.y -= self.velocidad
        self.rect.moveTo(self.x, self.y)

class Balas:
    def __init__(self, tiempo_entre_balas=TIEMPO_ENTRE_BALAS):
        self.diccionario = []
        self.ultima_bala = 0
        self.tiempo_entre_balas = tiempo_entre_balas

    def crear_bala(self, defensor, balas):
        tiempo_actual = QTime.currentTime().msecsSinceStartOfDay()
        if tiempo_actual - balas.ultima_bala > self.tiempo_entre_balas:
            balas.diccionario.append(Bala(defensor.rect.center().x(), defensor.rect.center().y()))
            balas.ultima_bala = tiempo_actual
