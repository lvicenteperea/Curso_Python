from transformers import pipeline

chatbot = pipeline('conversational', model='microsoft/DialoGPT-medium')

def chatbot_conversacion():
    print("¡Hola! Soy un chatbot. ¿En qué puedo ayudarte hoy?")
    while True:
        entrada = input("Tú: ")
        if entrada.lower() in ['salir', 'adiós']:
            print("Chatbot: ¡Hasta luego!")
            break
        
        respuesta = chatbot(entrada)
        print("Chatbot:", respuesta[0]['generated_text'])

chatbot_conversacion()
