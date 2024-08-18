from PyQt5.QtCore import QCoreApplication, Qt, QTimer
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QFont, QColor
import random

from config import ANCHO, ALTO, LIMITE_SUP, ENEMIGOS_FPS, TIEMPO_ENTRE_ENEMIGOS, VIDAS, POS_X_DEFENSOR,COLOR_FONDO
from personaje import Cubo
from enemigo import Enemigo
from bala import Balas
from funciones import gestionar_teclas

class JuegoWidget(QWidget):
    def __init__(self, ventana):
        super().__init__(ventana)
        self.initUI()

        self.reloj = QTimer(self)
        self.reloj.timeout.connect(self.actualizar)
        self.reloj.start(ENEMIGOS_FPS)

        self.vida = VIDAS
        self.puntos = 0
        self.tiempo_pasado = 0

        self.defensor = Cubo(ANCHO/2, POS_X_DEFENSOR)
        self.enemigos = []
        self.balas = Balas()

        self.jugando = True
        self.setFocus()

    def initUI(self):
        self.setGeometry(0, 0, ANCHO, ALTO)
        self.setStyleSheet("background-color: black;")
        self.show()

    def actualizar(self):
        if not self.jugando:
            return

        # Actualizar el juego
        self.tiempo_pasado += TIEMPO_ENTRE_ENEMIGOS
        if self.tiempo_pasado > TIEMPO_ENTRE_ENEMIGOS:
            enemigo = Enemigo(random.randint(0, ANCHO - 30), LIMITE_SUP)
            self.enemigos.append(enemigo)
            self.tiempo_pasado = 0

        # Mover los enemigos
        for enemigo in self.enemigos:
            enemigo.mover()

        # Mover las balas
        for bala in self.balas.diccionario:
            bala.mover()
            if bala.y < LIMITE_SUP:
                self.balas.diccionario.remove(bala)

        # Detectar colisiones
        for enemigo in self.enemigos:
            if self.defensor.rect.intersects(enemigo.rect):
                self.vida -= 1
                self.enemigos.remove(enemigo)
                if self.vida == 0:
                    self.jugando = False
                    break

            for bala in self.balas.diccionario:
                if bala.rect.intersects(enemigo.rect):
                    self.puntos += 1
                    self.enemigos.remove(enemigo)
                    self.balas.diccionario.remove(bala)

        # Redibujar todo
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.white)
        painter.setFont(QFont('Arial', 14))
        painter.fillRect(self.rect(), QColor(COLOR_FONDO))

        # Dibujar el defensor
        self.defensor.dibujar(painter)

        # Dibujar los enemigos
        for enemigo in self.enemigos:
            enemigo.dibujar(painter)

        # Dibujar las balas
        for bala in self.balas.diccionario:
            bala.dibujar(painter)

        # Mostrar vidas y puntos
        painter.drawText(40, 16, f"Vidas: {str(self.vida)}")
        painter.drawText(ANCHO - 100, 16, f"Puntos: {str(self.puntos)}")

        painter.end()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.defensor.mover_izquierda()
        elif event.key() == Qt.Key_Right:
            self.defensor.mover_derecha()
        elif event.key() == Qt.Key_Space:
            self.balas.crear_bala(self.defensor, self.balas)

        self.update()


def juego(ventana, puntos):
    juego_widget = JuegoWidget(ventana)
    ventana.setCentralWidget(juego_widget)

    # Esperar hasta que el juego termine
    while juego_widget.jugando:
        QCoreApplication.processEvents()

    return juego_widget.puntos
