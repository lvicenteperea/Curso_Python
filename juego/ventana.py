
import pygame
from config import ANCHO, ALTO, TAM_FUENTE
#from typing import Any


class Ventana:

    def __init__(self) -> None:
        pygame.init()

        self.marco = pygame.display.set_mode([ANCHO,ALTO])
        # Crear una fuente y definir el tamaño
        self.fuente = pygame.font.SysFont("Comic Sans", TAM_FUENTE)  # None usa la fuente predeterminada del sistema, 74 es el tamaño
        self.fuente_tam = pygame.font.Font(None, 16)  # None usa la fuente predeterminada del sistema, 74 es el tamaño

        pygame.display.set_caption("Primer Juego")



    def muestra_texto(self, texto, ancho = ANCHO - 50, alto = 16, tam_fuente = TAM_FUENTE, fuente = "Comic Sans", color = (255, 255, 255)):
        # Si nos envían una fuente diferente, la cambiamos, porque ya está inicializada a TAM_FUENTE
        if tam_fuente != TAM_FUENTE:
            # self.fuente_tam = pygame.font.Font(None, tam_fuente)  # None usa la fuente predeterminada del sistema, 74 es el tamaño
            self.fuente = pygame.font.SysFont(fuente, tam_fuente)

        # Renderizar el texto en una superficie
        text = self.fuente.render(texto, True, color)

        # Obtener el rectángulo del texto para poder posicionarlo
        text_rect = text.get_rect(center=(ancho, alto))

        self.marco.blit(text, text_rect)

