import pygame 
from config import VIDAS, DIR_DAT, FONDO_PANTALLA, LIMITE_SUP, TAM_FUENTE, ANCHO 
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
    fichero = f"{DIR_DAT}puntuaciones.txt"

    ventana.marco.fill(FONDO_PANTALLA)  # Llenamos la pantalla de negro solo una vez al principio
    lista_fichero(ventana, fichero, 2, top_n=5)  # primero sacamos los mejores jugadores

    nombre = ventana.pedir_datos(prompt)

    if len(nombre) > 0:
        with open(fichero, 'a') as archivo:
            archivo.write(f"{nombre:<20} - {mis_puntos} - {fecha} - {VIDAS:>5}\n")

    ordenar_fic(fichero, 2, 5)

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
def ordenar_fic(fichero, columna, top_n=5):
    with open(fichero, 'r') as file:
        lines = file.readlines()

    # Separar cabeceras y datos
    cabeceras = lines[:2]
    datos = lines[2:]

    # Función de ordenación por la columna "Puntos"
    def extraer_puntos(linea):
        return int(linea.split('-')[columna-1].strip())

    # Ordenar los datos por la columna "Puntos"
    datos_ordenados = sorted(datos, key=extraer_puntos, reverse=True)

    # Seleccionar las top_n mejores puntuaciones
    mejores_puntuaciones = datos_ordenados[:top_n]

    # Escribir los resultados ordenados en el fichero (puedes cambiar el nombre si quieres un fichero nuevo)
    with open(f"{fichero}_Orden_{columna}_top_{top_n}", 'w') as file:
        file.writelines(cabeceras)
        file.writelines(mejores_puntuaciones)


# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
def lista_fichero(ventana, fichero, columna, top_n=5):
    
    espacio_linea = LIMITE_SUP

    try:
        with open(f"{fichero}_Orden_{columna}_top_{top_n}", 'r') as file:
            for linea in file:
                ventana.muestra_texto(linea.rstrip("\n"), ANCHO // 2, espacio_linea, TAM_FUENTE, "Courier")
                espacio_linea += 30

    except Exception as e:
        print(f"No se ha podido abrir {fichero}_Orden_{columna}_top_{top_n}: {type(e).__name__}: {e}")
