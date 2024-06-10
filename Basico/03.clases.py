####  CLASES ####

"""
class MyEmptyPerson:
    pass


print(MyEmptyPerson())
print(MyEmptyPerson)
"""

class Person:
    # name = ""
    # surname = ""
    por_probar = "está caminando"

    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname
        self.__full_name = f"{name} {surname}"

    def walk(self):
        print (f"{self.__full_name} {self.por_probar}")

    def get_name (self):
        return self.__name

    def get_surname (self):
        return self.__surname

    def get_full_name (self):
        return self.__full_name


my_person = Person("Luis", "Vicente")
print(f"{my_person.get_name()} {my_person.get_surname()}")
my_person.walk()
