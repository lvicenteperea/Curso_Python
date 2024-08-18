#pip install pygame
# https://www.tiktok.com/@luisetindev_/video/7399378711818112288
import pygame 
import random
from config import ANCHO, ALTO, LIMITE_SUP, ENEMIGOS_FPS, TIEMPO_ENTRE_ENEMIGOS, VIDAS
from funciones import gestionar_teclas
from personaje import Cubo
from enemigo import Enemigo
from bala import Balas


def juego(ventana, puntos):
    reloj = pygame.time.Clock()
    tiempo_pasado = 0
    vida = VIDAS
    puntos = 0

    defensor = Cubo(ANCHO/2, ALTO-75)
    enemigos = []
    enemigo = Enemigo(random.randint(0, ANCHO), LIMITE_SUP)
    # enemigos.append(enemigo)
    balas = Balas()

    jugando = True
    while jugando:
        tiempo_pasado += reloj.tick(ENEMIGOS_FPS)
        if tiempo_pasado > TIEMPO_ENTRE_ENEMIGOS:
            enemigo = Enemigo(random.randint(0, ANCHO - enemigo.ancho), LIMITE_SUP)
            enemigos.append(enemigo)
            tiempo_pasado = 0

        if not gestionar_teclas(defensor, balas):
            jugando = False
            break

        ventana.marco.fill("black")    
        
        # Movimiento del defensor que depende de la tecla pulsada
        defensor.dibujar(ventana.marco)

        # Movimiento de los enemigos
        for enemigo in enemigos:
            enemigo.dibujar(ventana.marco)
            enemigo.mover()

            # miramos si colisiona o sale de pantalla
            if pygame.Rect.colliderect(defensor.rect, enemigo.rect):
                vida -= 1
                enemigos.remove(enemigo)
                if vida == 0:
                    jugando = False
                    break

            if enemigo.y > ALTO:
                enemigos.remove(enemigo)

            for bala in balas.diccionario:
                if pygame.Rect.colliderect(bala.rect, enemigo.rect):
                    puntos += 1
                    enemigos.remove(enemigo)
                    balas.diccionario.remove(bala)


        # Movimiento de las balas
        for bala in balas.diccionario:
            bala.dibujar(ventana.marco)
            bala.mover()
            if bala.y < LIMITE_SUP:
                balas.diccionario.remove(bala)

            if pygame.Rect.colliderect(bala.rect, enemigo.rect):
                enemigos.remove(enemigo)
                balas.diccionario.remove(bala)

        ventana.muestra_texto(f"Vidas: {str(vida)}", 40, 16)
        ventana.muestra_texto(f"Puntos: {str(puntos)}", ANCHO - 50, 16)

        pygame.display.update()

    return puntos
