#Pilas / stacks 

print("----------  Pila LIFO  -----------")
stack = []
stack.append(1) #push
stack.append(2) #push
stack.append(3) #push
print(stack)

# pop
stack_item = stack[len(stack) - 1]
del stack[len(stack) - 1]

print(stack_item)
print(stack)

#pero python ya tiene el pop
stack.pop()
print(stack)

#Cola / Queue 
print("----------  Cola FIFO  -----------")
queue = []
queue.append(1) #push
queue.append(2) #push
queue.append(3) #push

print(queue)

queue.pop(0)
print(queue)
print("")
print("")

print("----------  Navegador Web -----------")

stack_web = []

def navegador_web():
  stack = []
  
  while True:
    action = input("Añade una url o interactua con las palabras: Atrás/Salir: ")
    if action.capitalize() == "Atrás":
      if len(stack) > 0:
        stack.pop()
    elif action.capitalize() == "Salir":
      print("Saliendo del navegadr")
      return stack
    else:
      stack.append(action)
    
    if len(stack) == 0:
      print("Estas en la página de inicio")
    else:
      print(f"Has navegado a la web: {stack[len(stack)-1]}")

  return stack


stack_web = navegador_web()
print("--------- Webs Visitadas ---------")
print(stack_web)
print("")
print("")

print("----------  Impresora compartida -----------")

def impresora_compartida() -> list:
  queue = []

  while True:  
    action = input("Añade un documento o selecciona: Imprimir/Salir: ")

    if action.capitalize() == "Imprimir":
      if len(queue) == 0:
        print("No hay documentos para imprimir")
      else:
        print(f"Imprimiendo documento: {queue.pop(0)}")
        
    elif action.capitalize() == "Salir":
      print("Saliendo del programa")
      return queue
      
    else:
      queue.append(action)
      
  return queue

impresora = impresora_compartida()
print("--------- Impresora compartida ---------")
print(impresora)
print("")
print("")