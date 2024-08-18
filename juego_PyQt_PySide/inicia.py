from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, QEvent
from funciones import grabar_jugada
from config import ANCHO, ALTO, TAM_FUENTE
from ventana import Ventana
from juego import juego
import sys

def inicia_juego():
    app = QApplication(sys.argv)
    jugar = True

    while jugar:
        ventana = Ventana()
        puntos = juego(ventana, 0)

        # Mostrar mensajes finales
        ventana.muestra_texto('Cierre la ventana para salir y la tecla "j" para Jugar otra vez', ANCHO//2, ALTO//2, TAM_FUENTE)
        ventana.update()
        
        # Grabar la jugada
        grabar_jugada(ventana, f"Has conseguido {str(puntos)} PUNTOS. Introduce tu nombre: ", puntos)

        ventana.muestra_texto('Cierre la ventana para salir y la tecla "j" para Jugar otra vez', ANCHO//2, ALTO//2, TAM_FUENTE)
        ventana.update()

        waiting = True
        while waiting:
            event = app.processEvents()  # Procesar eventos
            for event in app.allWidgets():
                if event.type() == QEvent.Close:
                    waiting = False
                    jugar = False
                    break
                elif event.type() == QKeyEvent.KeyPress and event.key() == Qt.Key_J:
                    waiting = False
                    break

    sys.exit(app.exec_())

if __name__ == '__main__':
    inicia_juego()
