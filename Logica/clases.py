'''
# Ejercicio 1
class Programador:

    apellido: str = None
  
    def __init__(self, nombre: str, edad: int, lenguajes: list):
        self.nombre = nombre
        self.edad = edad
        self.lenguajes = lenguajes

    def print_info(self):
      print(f"Nombre:\t\t{self.nombre}\nEdad:\t\t{self.edad}\nApellidos:\t{self.apellido}")
      print(f"lenguajes:\t{self.lenguajes}")


mi_programador = Programador("Juan", 25, ["Python", "Java", "C++"])
mi_programador.print_info()

mi_programador.apellido = "Vicente"
mi_programador.print_info()
'''

# Ejercicio 2 Pila (LIFO)
class Stack:
  
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def count(self):
        return len(self.stack)
      
    def print_stack(self):
        print("Pila actual:")
        for elemento in reversed(self.stack):
            print(f"\tElemento: {elemento}")  
        print("--------------------")

        
      
print("-------- STACK (LIFO) --------------")
mi_stack = Stack()
mi_stack.push(1)
mi_stack.push(2)
mi_stack.push(3)
mi_stack.push(4)
mi_stack.print_stack()

mi_stack.pop()
mi_stack.print_stack()


print(mi_stack.pop())
print(mi_stack.pop())
print(mi_stack.pop())
print(mi_stack.pop())
print(mi_stack.pop())
print(mi_stack.pop())
print(mi_stack.pop())
mi_stack.print_stack()


#Cola (FIFO)

class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def count(self):
        return len(self.queue)

    def print_queue(self):
        print("Cola actual:")
        for elemento in self.queue:
            print(f"\tElemento: {elemento}")
        print("--------------------")


print("-------- QUEUE (FIFO) --------------")
mi_cola = Queue()
mi_cola.enqueue(1)
mi_cola.enqueue(2)
mi_cola.enqueue(3)
mi_cola.print_queue()

mi_cola.dequeue()
mi_cola.print_queue()

print(mi_cola.dequeue())
print(mi_cola.dequeue())
print(mi_cola.dequeue())
print(mi_cola.dequeue())
mi_cola.print_queue()



