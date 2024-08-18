import pygame 
from config import ANCHO, ALTO, TAM_FUENTE, TIEMPO_ENTRE_BALAS
from bala import Bala


# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
'''
def crear_bala(defensor, balas):
    if pygame.time.get_ticks() - balas.ultima_bala > TIEMPO_ENTRE_BALAS:
        balas.diccionario.append(Bala(defensor.rect.centerx, defensor.rect.centery))
        balas.ultima_bala = pygame.time.get_ticks()
'''
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
def gestionar_teclas(defensor, balas):

    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            return False

    teclas = pygame.key.get_pressed() # lista con las teclas pulsadas

    # if teclas[pygame.K_w]:
    #     defensor.y -= defensor.velocidad
    # if teclas[pygame.K_s]:
    #     defensor.y += defensor.velocidad
    if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
        defensor.x -= defensor.velocidad
    if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
        defensor.x += defensor.velocidad
    if teclas[pygame.K_SPACE]:
        balas.crear_bala(defensor, balas)

    return True



# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------