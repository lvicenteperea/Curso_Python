#pip install pygame
# https://www.tiktok.com/@luisetindev_/video/7399378711818112288
import pygame 
import random
from config import ANCHO, ALTO, LIMITE_SUP, ENEMIGOS_FPS, TIEMPO_ENTRE_ENEMIGOS
from funciones import gestionar_teclas
from personaje import Cubo
from enemigo import Enemigo
from bala import Balas


def juego(ventana, puntos):
    reloj = pygame.time.Clock()
    tiempo_pasado = 0

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
        defensor.dibujar(ventana)

        # Movimiento de los enemigos
        for enemigo in enemigos:
            enemigo.dibujar(ventana)
            enemigo.mover()

            # miramos si colisiona o sale de pantalla
            if pygame.Rect.colliderect(defensor.rect, enemigo.rect):
                enemigos.remove(enemigo)

                if defensor.quita_vida() == 0:
                  jugando = False
                  break

            if enemigo.y > ALTO:
                enemigos.remove(enemigo)
                defensor.suma_puntos(-1)

            for bala in balas.diccionario:
                if pygame.Rect.colliderect(bala.rect, enemigo.rect):
                    defensor.elimina_enemigo(enemigos, enemigo, balas.diccionario, bala)


        # Movimiento de las balas
        for bala in balas.diccionario:
            bala.dibujar(ventana.marco)
            bala.mover()
            if bala.y < LIMITE_SUP:
                balas.diccionario.remove(bala)
            '''
                Esto estaba desde el principio, pero parece que me sobra....
                if pygame.Rect.colliderect(bala.rect, enemigo.rect):
                    try:
                        enemigos.remove(enemigo)
                    except Exception as e:
                        # Habría que ver porqué pasa esto.... o pasa porque se ha podido elimiarn 14 lineas mas arriba, al eliminar enemigos
                        print(f"Error inexperado ENEMIGO {type(e).__name__}: {e}")

                    print("Seguimos")
                    try:
                        balas.diccionario.remove(bala)
                    except Exception as e:
                        print(f"Error inexperado BALAS {type(e).__name__}: {e}")
            '''

        ventana.muestra_texto(f"Vidas: {str(defensor.vida)}", 40, 16)
        ventana.muestra_texto(f"Puntos: {str(defensor.puntos)}", ANCHO - ((len(str(defensor.puntos))*3)+50), 16)

        pygame.display.update()

    return defensor.puntos
