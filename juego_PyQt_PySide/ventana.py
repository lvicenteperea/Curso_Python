from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QLineEdit, QWidget, QApplication
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt
from config import ANCHO, ALTO, TAM_FUENTE

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, ANCHO, ALTO)
        self.setWindowTitle("Primer Juego")
        
        # Configuración de la fuente
        self.fuente = QFont("Comic Sans", TAM_FUENTE)
        self.fuente_tam = QFont("Arial", 16)

        # Configuración del layout principal
        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)
        self.setCentralWidget(self.central_widget)

        self.show()

    def muestra_texto(self, texto, ancho=ANCHO - 50, alto=16, tam_fuente=TAM_FUENTE, fuente="Comic Sans", color=(255, 255, 255)):
        # Configuración de la fuente
        font = QFont(fuente, tam_fuente)
        label = QLabel(texto, self)
        label.setFont(font)
        label.setStyleSheet(f"color: rgb({color[0]}, {color[1]}, {color[2]});")
        label.move(ancho, alto)
        label.adjustSize()  # Ajustar tamaño al contenido
        label.show()

    def pedir_datos(self, prompt, max_caracteres=20):
        # Variables
        dato_pedido = ""
        self.layout.setAlignment(Qt.AlignCenter)

        # Crear y mostrar la etiqueta del prompt
        prompt_label = QLabel(prompt, self)
        prompt_label.setFont(self.fuente)
        prompt_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(prompt_label)

        # Crear y mostrar la entrada de texto
        input_line = QLineEdit(self)
        input_line.setMaxLength(max_caracteres)
        input_line.setFont(QFont("Arial", TAM_FUENTE * 2))
        input_line.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(input_line)

        input_line.returnPressed.connect(lambda: self.captura_entrada(input_line))
        
        self.show()

        # Esperar a que el usuario presione Enter
        self.input_value = ""
        while not self.input_value:
            QApplication.processEvents()

        return self.input_value

    def captura_entrada(self, input_line):
        self.input_value = input_line.text()
        input_line.clear()
