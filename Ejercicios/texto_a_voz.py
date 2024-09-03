import pyttsx3

def texto_a_voz(texto):
    engine = pyttsx3.init()

    # Configurar las propiedades de la voz si es necesario
    engine.setProperty('rate', 150)  # Velocidad de la voz (palabras por minuto)
    engine.setProperty('volume', 1.0)  # Volumen (0.0 a 1.0)

    # Obtener las voces disponibles
    voces = engine.getProperty('voices')

    for voz in voces:
        print(f"ID: {voz.id}")
        print(f"Nombre: {voz.name}")
        print(f"Género: {voz.gender}")
        print(f"Idioma: {voz.languages}\n")


    engine.say(texto)
    engine.runAndWait()


texto = input("Texto: ")

texto_a_voz(texto)