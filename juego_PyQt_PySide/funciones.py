from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent
from datetime import datetime
from config import ANCHO, ALTO, TAM_FUENTE, VIDAS

def gestionar_teclas(defensor, balas, event):
    """
    Maneja las teclas presionadas en PyQt y actualiza el estado del defensor y las balas.
    """
    # Manejamos solo los eventos de teclas
    if event.type() == QKeyEvent.KeyPress:
        key = event.key()
        
        if key == Qt.Key_Left or key == Qt.Key_A:
            defensor.mover_izquierda()
        elif key == Qt.Key_Right or key == Qt.Key_D:
            defensor.mover_derecha()
        elif key == Qt.Key_Space:
            balas.crear_bala(defensor, balas)

    # Para PyQt, devolvemos True porque la ventana se sigue ejecutando
    return True

def grabar_jugada(ventana, prompt, puntos):
    """
    Graba la jugada del jugador en un archivo de puntuaciones.
    """

    # Formateamos datos y pedimos el nombre del jugador
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    mis_puntos = f"{puntos:>10,}".replace(",", ".")

    # Pedir el nombre del jugador usando el método de la clase Ventana
    nombre = ventana.pedir_datos(prompt)

    if len(nombre) > 0:
        with open('./Juego_pygame/puntuaciones.txt', 'a') as archivo:
            archivo.write(f"{nombre:<20} - {mis_puntos} - {fecha} - {VIDAS:>5}\n")