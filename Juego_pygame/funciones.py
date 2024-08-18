import pygame 
from config import VIDAS
from datetime import datetime

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
def grabar_jugada(ventana, prompt, puntos):

    # Formateamos datos y pedimos el nombre del jugador
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    mis_puntos = f"{puntos:>10,}".replace(",", ".")

    # nombre = input ("Introduce tu nombre: " )
    nombre = ventana.pedir_datos(prompt)

    if len(nombre) > 0:
        with open('./Juego_pygame/puntuaciones.txt', 'a') as archivo:
            archivo.write(f"{nombre:<20} - {mis_puntos} - {fecha} - {VIDAS:>5}\n")


# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
'''
def pedir_nombre(ventana, prompt) -> str:
    # Variables
    nombre = ""
    max_caracteres = 20
    input_active = True
    pygame.event.clear()
    pos_ancho = ANCHO//2
    pos_alto  = ALTO//2

    # Bucle principal
    running = True
    while running:
        # Lo borramos todo y volvemos a imprimir para sacar bien el nombre, si no, queda superpuesto
        ventana.marco.fill("black")    
        # Prompt
        ventana.muestra_texto(prompt, pos_ancho, pos_alto, TAM_FUENTE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if input_active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Finaliza la entrada al presionar Enter
                        input_active = False
                        running = False
                    elif event.key == pygame.K_BACKSPACE:  # Borra el último carácter
                        nombre = nombre[:-1]
                    elif len(nombre) < max_caracteres:  # Añade caracteres al nombre si no excede el máximo
                        nombre += event.unicode

        ventana.muestra_texto(nombre, pos_ancho, pos_alto + 60, TAM_FUENTE * 2)

        pygame.display.update()
        # Actualizar la pantalla
        # pygame.display.flip()

    # Imprimir el nombre capturado (solo para ver el resultado fuera de Pygame)
    print(f"Nombre introducido: {nombre}")
    return nombre
'''