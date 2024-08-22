#pip install pygame
# https://www.tiktok.com/@luisetindev_/video/7399378711818112288
import pygame 
import random
from config import ANCHO, ALTO, LIMITE_SUP, ENEMIGOS_FPS, TIEMPO_ENTRE_ENEMIGOS, MINIMO_ENTRE_BALAS
from funciones import gestionar_teclas
from personaje import Cubo
from enemigo import Enemigo
from item import Item
from bala import Balas


def juego(ventana, puntos):
    reloj = pygame.time.Clock()
    tiempo_pasado = 0
    tiempo_pasado_items = 0

    defensor = Cubo(ANCHO/2, ALTO-75)
    enemigos = []
    enemigo = Enemigo(random.randint(0, ANCHO), LIMITE_SUP)
    # enemigos.append(enemigo)
    balas = Balas()
    items = []
    item = Item(random.randint(0, ANCHO), LIMITE_SUP)

    jugando = True
    while jugando:
        tiempo = reloj.tick(ENEMIGOS_FPS)
        tiempo_pasado += tiempo
        tiempo_pasado_items += tiempo

        if tiempo_pasado > TIEMPO_ENTRE_ENEMIGOS:
            enemigo = Enemigo(random.randint(0, ANCHO - enemigo.ancho), LIMITE_SUP)
            enemigos.append(enemigo)
            tiempo_pasado = 0

        if tiempo_pasado_items > (TIEMPO_ENTRE_ENEMIGOS*3) and balas.tiempo_entre_balas > MINIMO_ENTRE_BALAS:
            item = Item(random.randint(0, ANCHO - item.ancho), LIMITE_SUP)
            items.append(item)
            tiempo_pasado_items = 0

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

        for item in items:
            item.dibujar(ventana)
            item.mover()

            # miramos si colisiona o sale de pantalla
            if pygame.Rect.colliderect(defensor.rect, item.rect):
                print(item.tipo)
                if item.tipo == 1:
                    balas.reduce_tiempo_entre_balas()
                else:
                    defensor.aumenta_velocidad()

                items.remove(item)

            if enemigo.y > ALTO:
                items.remove(item)

        ventana.muestra_texto(f"Vidas: {str(defensor.vida)}", 40, 16)
        ventana.muestra_texto(f"Balas/Velocidad: {str(balas.tiempo_entre_balas)}/{str(defensor.velocidad)}", ANCHO // 2, 16)
        ventana.muestra_texto(f"Puntos: {str(defensor.puntos)}", ANCHO - ((len(str(defensor.puntos))*3)+50), 16)



        pygame.display.update()

    return defensor.puntos
