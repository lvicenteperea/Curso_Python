# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=3239

### List Comprehension ###
'''
my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(f"Lista 1 {my_original_list}")

my_range = range(8)
print(f"Lista 2 {list(my_range)}")

# Definición

my_list = [i + 1 for i in range(8)]
print(f"Lista 3 {my_list}")

my_list = [i * 2 for i in range(8)]
print(f"Lista 4 {my_list}")

my_list = [i * i for i in range(8)]
print(f"Lista 5 {my_list}")


def sum_five(number):
    return number + 5


my_list = [sum_five(i) for i in range(8)]
print(f"Lista 6 {my_list}")

# Tu lista de usuarios
usuarios = [
    {
        "id": 1,
        "nombre": "Usuario_1",
        "apellido": "Apellido_1",
        "email": "email_1@dominio.com",
        "edad": 21
    },
    {
        "id": 2,
        "nombre": "Usuario_2",
        "apellido": "Apellido_2",
        "email": "email_2@dominio.com",
        "edad": 22
    }
]

 
print("")
print("----  Obtén el ID más alto  ----")
id_mas_alto = max(usuario["id"] for usuario in usuarios)
print(f"El ID más alto es: {id_mas_alto}")



print("")
print("----  FECHAS  ----")
from datetime import datetime, timedelta
ahora = datetime.utcnow()
print(ahora)
print(timedelta(minutes=1))
print(ahora+timedelta(minutes=1))


print("")
print("----  Buscar en un diccionario  ----")
users_db = {
    "luis": {"username": "lvicente",
                    "full_name": "Luis Vicente",
                    "email": "lvicente@hangarxxi.com",
                    "disable": False,
                    "password": "123456"
    },
    "luis3": {"username": "lvicente2",
                    "full_name": "Luis Vicente 2",
                    "email": "lvicente2@hangarxxi.com",
                    "disable": True,
                    "password": "654321",
    }
}

print(users_db["luis"])
print(users_db.get("luis"))
print("luis" in users_db)

print("")
print("----  Encriptar  ----")
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
pwd = "123456"
pwd_hashed = pwd_context.hash(pwd)

#print(f"Verificando ({pwd}): {pwd_context.verify(pwd, pwd_hashed)}")
print(f"tokenizando: {pwd_hashed}")

if pwd_context.verify(pwd, pwd_hashed):
    print(f"Verificando {pwd} = {pwd_hashed}")


print("")
print("----  Buscando en un Dict  ----")
users_db = {
    "usuario1": {"username": "lvicente",
                    "full_name": "Luis Vicente",
                    "email": "lvicente@hangarxxi.com",
                    "disable": False,
                    "password": "$2a$12$jjRhXRlQ.XIDjniPDqJituayYjNbR91FVn1.AwHIxEqW2VVA69ZtS"  # "123456"
    },
    "usuario2": {"username": "lvicente2",
                    "full_name": "Luis Vicente 2",
                    "email": "lvicente2@hangarxxi.com",
                    "disable": True,
                    "password": "$2a$12$VYB0VWvNJMlxC07CtE3jbuamePDLc8V0xnG.rzS4vindKL.xlef2."  #"654321"
    }
}
print(users_db.get("usuario2"))

### Dictionaries ###
# Definición
my_dict = dict()
my_other_dict = {}

print(f"1 - {type(my_dict)}")
print(f"2 - {type(my_other_dict)}")

my_other_dict = {"Nombre": "Brais",
                 "Apellido": "Moure", "Edad": 35, 1: "Python"}

my_dict = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
}

print(f"3 - {my_other_dict}")
print(f"4 - {my_dict}")

print(f"5 - {len(my_other_dict)}")
print(f"6 - {len(my_dict)}")

# Búsqueda

print(f"7 - {my_dict[1]}")
print(f'8 - {my_dict["Nombre"]}')

print(f'9 - {"Moure" in my_dict}')
print(f'10 - {"Apellido" in my_dict}')

# Inserción

my_dict["Calle"] = "Calle MoureDev"
print(f"11 - {my_dict}")

# Actualización

my_dict["Nombre"] = "Pedro"
print(f'12 - {my_dict["Nombre"]}')
print(f'12a - {my_dict}')

# Eliminación

del my_dict["Calle"]
print(f"13 - {my_dict}")

# Otras operaciones

print(f"14 - {my_dict.items()}")
print(f"15 - {my_dict.keys()}")
print(f"16 - {my_dict.values()}")

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(f"17 - {my_new_dict}")
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(f"18 - {(my_new_dict)}")
my_new_dict = dict.fromkeys(my_dict)
print(f"19 - {(my_new_dict)}")
my_new_dict = dict.fromkeys(my_dict, "MoureDev")
print(f"20 - {(my_new_dict)}")

my_values = my_new_dict.values()
print(f"21 - {type(my_values)}")

print(f"22 - {my_new_dict.values()}")
print(f"23 - {list(dict.fromkeys(list(my_new_dict.values())).keys())}")
print(f"24 - {tuple(my_new_dict)}")
print(f"25 - {set(my_new_dict)}")



### Lists ###
# Definición
my_list = list()
my_other_list = []

print(f'01 - {len(my_list)}')

my_list = [35, 24, 62, 52, 30, 30, 17]
my_other_list = [35, 1.77, "Brais", "Moure"]

print(f'01 - {my_list}')
print(f'01 - {my_other_list}')
print(f'02 - {len(my_list)}')


print(f'03 - {type(my_list)}')
print(f'04 - {type(my_other_list)}')

# Acceso a elementos y búsqueda

print(f'05 - {my_other_list[0]}')
print(f'06 - {my_other_list[1]}')
print(f'07 - {my_other_list[-1]}')
print(f'08 - {my_other_list[-4]}')
print(f'09 - {my_list.count(30)}')
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

print(f'10 - {my_other_list.index("Brais")} - {my_other_list.index(35)}')

age, height, name, surname = my_other_list
print(f'11 - {name}')

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(f'12 - {age}')
age, height, name, surname = my_other_list
print(f'12a - {age}')

# Concatenación

print(f'13 - {my_list + my_other_list}')
#print(my_list - my_other_list)

# Creación, inserción, actualización y eliminación

my_other_list.append("MoureDev")
print(f'14 - {my_other_list}')

my_other_list.insert(1, "Rojo")
print(f'15 - {my_other_list}')

my_other_list[1] = "Azul"
print(f'16 - {my_other_list}')

my_other_list.remove("Azul")
print(f'17 - {my_other_list}')

my_list.remove(30)
print(f'18 - {my_list}')

print(f'19 - {my_list.pop()}')
print(f'20 - {my_list}')

my_pop_element = my_list.pop(2)
print(f'21 - {my_pop_element}')
print(f'22 - {my_list}')

del my_list[2]
print(f'23 - {my_list}')

# Operaciones con listas

my_new_list = my_list.copy()

my_list.clear()
print(f'24 - {my_list}')
print(f'25 - {my_new_list}')

my_new_list.reverse()
print(f'26 - {my_new_list}')

my_new_list.sort()
print(f'27 - {my_new_list}')

# Sublistas

print(f'28 - {my_new_list[1:3]}')

# Cambio de tipo

my_list = "Hola Python"
print(f'29 - {my_list}')
print(f'30 - {type(my_list)}')
'''

# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=14711
### Tuples ###
# Definición
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_other_tuple = (35, 60, 30)

print(f'01 - {my_tuple}')
print(f'01 - {type(my_tuple)}')

# Acceso a elementos y búsqueda

print(f'01 - {my_tuple[0]}')
print(f'01 - {my_tuple[-1]}')
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(f'01 - {my_tuple.count("Brais")}')
print(f'01 - {my_tuple.index("Moure")}')
print(f'01 - {my_tuple.index("Brais")}')

# my_tuple[1] = 1.80 'tuple' object does not support item assignment

# Concatenación

my_sum_tuple = my_tuple + my_other_tuple
print(f'01 - {my_sum_tuple}')

# Subtuplas

print(f'01 - {my_sum_tuple[3:6]}')

# Tupla mutable con conversión a lista

my_tuple = list(my_tuple)
print(f'01 - {type(my_tuple)}')

my_tuple[4] = "MoureDev"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(f'01 - {my_tuple}')
print(f'01 - {type(my_tuple)}')

# Eliminación

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(f'01 - {my_tuple) NameError: name 'my_tuple' is not defined


# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=16335


'''
### Sets ###
# Definición
my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))  # Inicialmente es un diccionario

my_other_set = {"Brais", "Moure", 35}
print(type(my_other_set))

print(len(my_other_set))

# Inserción

my_other_set.add("MoureDev")

print(my_other_set)  # Un set no es una estructura ordenada

my_other_set.add("MoureDev")  # Un set no admite repetidos

print(my_other_set)

# Búsqueda

print("Moure" in my_other_set)
print("Mouri" in my_other_set)

# Eliminación

my_other_set.remove("Moure")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

# Transformación

my_set = {"Brais", "Moure", 35}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

# Otras operaciones

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))
print(my_new_set.difference(my_set))

'''

'''
# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=29327

### Classes ###

# Definición

class MyEmptyPerson:
    pass  # Para poder dejar la clase vacía


print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con constructor, funciones y popiedades privadas y públicas


class Person:
    def __init__(self, name, surname, alias="Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
        self.__name = name  # Propiedad privada

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person("Brais", "Moure")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Brais", "Moure", "MoureDev")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)
'''


'''
# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=34583
### Modules ###
### Módulo para pruebas ###

def sumValue(numberOne, numberTwo, numberThree):
    print(numberOne + numberTwo + numberThree)


def printValue(value):
    print(value)


----------------------------------------------------------------
### MAIN ###
from math import pi as PI_VALUE
import math
from my_module import sumValue, printValue
import my_module

my_module.sumValue(5, 3, 1)
my_module.printValue("Hola Python!")

sumValue(5, 3, 1)
printValue("Hola python")


print(math.pi)
print(math.pow(2, 8))


print(PI_VALUE)




'''