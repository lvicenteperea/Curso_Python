import os
import xml.etree.ElementTree as xml
import json

persona = {
    "name" : "Luis Alberto",
    "age" : 57,
    "nacimiento" : "31/08/1967",
    "lenguajes" : ["Sql", "Kotlin", "Java", "Python"]
}

print("-------------------------------------------")
print("Ejercicio1:  XML")
print("-------------------------------------------")
xml_file = "persona.xml"

def create_xml():
  padre = xml.Element("persona")

  for key, value in persona.items():
    hijo = xml.SubElement(padre, key)
    if isinstance(value, list):
      for item in value:
        otro_hijo = xml.SubElement(hijo, "item")
        otro_hijo.text = str(item)
    else:
      hijo.text = str(value)

  tree = xml.ElementTree(padre)
  tree.write(xml_file)

create_xml()

with open(xml_file, "r") as xml_data:
  cadena_xml = xml_data.read()
  print(cadena_xml)
  
  root = xml.fromstring(cadena_xml)
  print(xml.tostring(root, encoding='unicode', method='xml'))


os.remove(xml_file)
#-------------------------------------------------------------------
print("-------------------------------------------")
print("Ejercicio2:  JSON")
print("-------------------------------------------")

json_file = "persona.json"

def create_json():
  with open(json_file, "w") as json_data:
    json.dump(persona, json_data, indent=4)

create_json()

with open(json_file, "r") as json_data:
  cadena_json = json_data.read()
  print(cadena_json)

os.remove(json_file)

#-------------------------------------------------------------------
print("-------------------------------------------")
print("Ejercicio3:")
print("-------------------------------------------")
#----------------------------------------------------------------
create_xml()

class  Data:
  xml_file = "persona.xml"
  
  def __init__(self, name, age , nacimiento, lenguajes):
      self.name = name
      self.age = age
      self.nacimiento = nacimiento
      self.lenguajes = lenguajes



with open(xml_file, "r") as xml_data:
  root = xml.fromstring(xml_data.read())
  name = root.find("name").text
  age = root.find("age").text
  nacimiento = root.find("nacimiento").text
  lenguajes = []
  for item in root.find("lenguajes"):
    lenguajes.append(item.text)
  
data_from_xml = Data(name, age, nacimiento, lenguajes)
print("------- IMPRIMIENDO DE XML --------")
print(f"Objeto: {data_from_xml}")
print(f"Un Elemento: {data_from_xml.name}")
print(f"en formato Diccionario: {data_from_xml.__dict__}")
print("------------------------------------")

os.remove(xml_file)

#----------------------------------------------------------------
create_json()

with open(json_file, "r") as json_data:
  json_dict = json.load(json_data) # para convertir la cadena leida a un diccionario
  name = json_dict["name"]
  age = json_dict["age"]
  nacimiento = json_dict["nacimiento"]
  lenguajes = json_dict["lenguajes"]
  
data_from_json = Data(name, age, nacimiento, lenguajes)
print("------- IMPRIMIENDO DE JSON --------")
print(f"Objeto: {data_from_json}")
print(f"Un Elemento: {data_from_json.name}")
print(f"en formato Diccionario: {data_from_json.__dict__}")
print("------------------------------------")

os.remove(json_file)