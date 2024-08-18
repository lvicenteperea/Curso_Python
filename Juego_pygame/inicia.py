#pip install pygame
# https://www.tiktok.com/@luisetindev_/video/7399378711818112288
import pygame
from funciones import grabar_jugada
from config import ANCHO, ALTO,TAM_FUENTE
from ventana import Ventana
from juego import juego

jugar = True

while jugar:

    ventana = Ventana()
    puntos = juego(ventana, 0)

    ventana.marco.fill("black")    
    # ventana.muestra_texto('Cierre la ventana para salir y la tecla "j" para Jugar otra vez', ANCHO//2, ALTO//2 - 60, TAM_FUENTE)
    # ventana.muestra_texto(f"Puntos: {str(puntos)}", ANCHO//2, ALTO//2, 70)

    # pedir_nombre(ventana, "Introduce tu nombre: ")
    grabar_jugada(ventana, f"Has conseguido {str(puntos)} PUNTOS. Introduce tu nombre: ", puntos)

    ventana.marco.fill("black")    
    ventana.muestra_texto('Cierre la ventana para salir y la tecla "j" para Jugar otra vez', ANCHO//2, ALTO//2, TAM_FUENTE)
    pygame.display.update()
    pygame.time.delay(200)
    pygame.event.clear()

    waiting = True
    while waiting:
        teclas = pygame.event.get()

        for event in teclas:
            try:
                var1 =  event
                if event.type == pygame.QUIT:
                    waiting = False
                    jugar = False
                elif event.key == pygame.K_j:
                    waiting = False
                break
            except: # no se porqué, en el for, puede ir mucho contenido y si tocas raton o teclas especiales, var1.key no existe y casca
                pass
                
# salimos de la ventana
pygame.quit()

# grabar_jugada(puntos)

quit()
