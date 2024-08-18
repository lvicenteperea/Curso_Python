
import pygame
from config import ANCHO, ALTO, TAM_FUENTE
#from typing import Any


class Ventana:

    # ---------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------
    def __init__(self) -> None:
        pygame.init()

        self.marco = pygame.display.set_mode([ANCHO,ALTO])
        # Crear una fuente y definir el tamaño
        self.fuente = pygame.font.SysFont("Comic Sans", TAM_FUENTE)  # None usa la fuente predeterminada del sistema, 74 es el tamaño
        self.fuente_tam = pygame.font.Font(None, 16)  # None usa la fuente predeterminada del sistema, 74 es el tamaño

        pygame.display.set_caption("Primer Juego")



    # ---------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------
    def muestra_texto(self, texto, ancho = ANCHO - 50, alto = 16, tam_fuente = TAM_FUENTE, fuente = "Comic Sans", color = (255, 255, 255)):
        # Si nos envían una fuente diferente, la cambiamos, porque ya está inicializada a TAM_FUENTE
        # if tam_fuente != TAM_FUENTE:
        # self.fuente_tam = pygame.font.Font(None, tam_fuente)  # None usa la fuente predeterminada del sistema, 74 es el tamaño
        self.fuente = pygame.font.SysFont(fuente, tam_fuente)

        # Renderizar el texto en una superficie
        text = self.fuente.render(texto, True, color)

        # Obtener el rectángulo del texto para poder posicionarlo
        text_rect = text.get_rect(center=(ancho, alto))

        self.marco.blit(text, text_rect)

    # ---------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------
    def pedir_datos(self, prompt, max_caracteres = 20) -> str:
        # Variables
        dato_pedido = ""
        pygame.event.clear()
        pos_ancho = ANCHO//2
        pos_alto  = ALTO//2

        # Bucle principal
        running = True
        while running:
            # Lo borramos todo y volvemos a imprimir para sacar bien el dato_pedido, si no, queda superpuesto
            self.marco.fill("black")    
            # Prompt
            self.muestra_texto(prompt, pos_ancho, pos_alto, TAM_FUENTE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    dato_pedido = ""
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Finaliza la entrada al presionar Enter
                        running = False
                    elif event.key == pygame.K_BACKSPACE:  # Borra el último carácter
                        dato_pedido = dato_pedido[:-1]
                    elif len(dato_pedido) < max_caracteres:  # Añade caracteres al dato_pedido si no excede el máximo
                        dato_pedido += event.unicode

            self.muestra_texto(dato_pedido, pos_ancho, pos_alto + 60, TAM_FUENTE * 2)

            # Actualizar la pantalla
            pygame.display.update()
            # pygame.display.flip()

        return dato_pedido