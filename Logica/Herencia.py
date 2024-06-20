'''
#superclase
class Animal:
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species

    def make_sound(self):
      print("No sabemos que hace")

#subclases
class Perro(Animal):

  def make_sound(self):
        print("Guau")
      

class Gato(Animal):
      
    def make_sound(self):
        print("Miau")


def print_sound(animal: Animal):
    animal.make_sound()


  
#instanciar
mi_animal = Animal("animalito", "Indefinido")
mi_animal.make_sound()

mi_perro = Perro( "Max", "Perro")
mi_perro.make_sound()

mi_gato = Gato( "Michi", "Gato")
mi_gato.make_sound()


#polimorfismo
print_sound(mi_animal)
print_sound(mi_perro)
print_sound(mi_gato)


print("")
print("")
print("------------------------------------------------------")
'''

#Superclase
class Empleado:
    def __init__(self, id: int, nombre: str):
        self.nombre = nombre
        self.id = id
        self.lista_empleados = []
        self.tipo = "Empleado"

    def add(self, empleado):
        self.lista_empleados.append(empleado)


    def print_empleados(self):
        print(f"--- Empleados del {self.tipo} {self.nombre} ---")
        for empleado in self.lista_empleados:
            print(f"Nombre: {empleado.nombre} - ID: {empleado.id}")
        print("------------------------")

#Clases que heredan de Empleado
class Manager(Empleado):
    def __init__(self, id: int, nombre: str, project: str):
        super().__init__(id, nombre)
        self.project = project
        self.tipo = "Manager"

    def code(self):  
      print(f"{self.nombre} está escribiendo código en {self.lenguaje}")
  
    def coordinate_projects(self):
        print(f"{self.nombre} está Coordinando proyectos")


  
class ProjectManager(Empleado):
    def __init__(self, id: int, nombre: str, bonus: int):
        super().__init__(id, nombre)
        self.bonus = bonus
        self.tipo = "Project Manager"

    def coordinate_project(self):
        print(f"{self.nombre} está Coordinando su proyecto")


class Programmer(Empleado):
    def __init__(self, id: int, nombre: str, lenguaje: str):
        super().__init__(id, nombre)
        self.lenguaje = lenguaje
        self.tipo = "Programador"

    def code(self):
        print(f"{self.nombre} está escribiendo código en {self.lenguaje}")

    def add(self, empleado):
        print(f"Un programador no puede tener empleados, el empleado {empleado.nombre} no se puede agregar")

#instanciar
mi_manager = Manager(1, "Laura", "Proyecto 1")
mi_PM1 = ProjectManager(2, "Luis", 100)
mi_PM2 = ProjectManager(3, "Pedro", 100)
mi_programador1 = Programmer(4, "Maria", "Python")
mi_programador2 = Programmer(5, "Marta", "Dart")
mi_programador3 = Programmer(6, "Juan", "Java")

mi_manager.add(mi_PM1)
mi_manager.add(mi_PM2)

mi_PM1.add(mi_programador1)
mi_PM1.add(mi_programador2)
mi_PM2.add(mi_programador3)

mi_programador3.add(mi_programador1)

mi_manager.coordinate_projects()
mi_PM1.coordinate_project()
mi_PM2.coordinate_project()
mi_programador1.code()
mi_programador2.code()
mi_programador3.code()

mi_manager.print_empleados()
mi_PM1.print_empleados()  
mi_PM2.print_empleados()  
mi_programador1.print_empleados()
mi_programador2.print_empleados()
mi_programador3.print_empleados()
