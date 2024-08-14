import pygame 
#pip install pygame

ANCHO = 1000
ALTO = 800
VENTANA = pygame.display.set_mode([ANCHO,ALTO])

jugando = True
while jugando:
    pygame.display.update()


'''    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

pygame.display.set_caption("Primer Juego")
'''
