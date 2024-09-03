import os

print("-------------------------------------------------------------")
print("Ejercicio 1")
print("-------------------------------------------------------------")


nombre_fichero = "mi_fichero.txt"

with open(nombre_fichero, "w") as fichero:
    fichero.write("Luis Alberto\n")
    fichero.write("36\n")
    fichero.write("Python\n")
    
with open(nombre_fichero, "r") as fichero:
    print(fichero.read())

os.remove(nombre_fichero)

print("-------------------------------------------------------------")
print("Ejercicio 2")
print("-------------------------------------------------------------")

def escribir_fichero(nombre_fichero:str, nombre:str, cantidad:str, precio:str, metodo="a"):
  with open(nombre_fichero, metodo) as fichero:
    fichero.write(f"{nombre}|")
    fichero.write(f"{cantidad}|")
    fichero.write(f"{precio}\n")


nombre_fichero = "mi_fichero2.txt"
escribir_fichero(nombre_fichero, "nombre", "cantidad", "precio", "w")
escribir_fichero(nombre_fichero, "p1", "10", "12.50")
escribir_fichero(nombre_fichero, "p2", "1", "9.20")
escribir_fichero(nombre_fichero, "p3", "12", "2.00")

while True:
  print("1. Añadir un producto")
  print("2. Consultar Producto")
  print("3. Actualizar producto")
  print("4. Borrar producto")
  print("5. Ver lista de productos")
  print("6. Calcular venta total")
  print("7. Calcular venta por producto")
  print("8. Salir")

  opcion = input("Seleccione una opción: ")

  if opcion == "1":
    nombre = input("Nombre producto: ")
    cantidad = input("Cantidad: ")
    precio = input("Precio: ")
    escribir_fichero(nombre_fichero, nombre, cantidad, precio)

  elif opcion == "2":
    print("-------------------------------------------")
    nombre = input("Nombre producto: ")
    with open(nombre_fichero, "r") as fichero:
        for linea in fichero.readlines():
          if linea.split(sep="|")[0] == nombre:
            print(linea)
    print("-------------------------------------------")
      
  elif opcion == "3":
    print("-------------------------------------------")
    nombre = input("Nombre producto a actualizar: ")
    cantidad = input("Cantidad: ")
    precio = input("Precio: ")  
    
    with open(nombre_fichero, "r") as fichero:
      lineas = fichero.readlines()
      
    with open(nombre_fichero, "w") as fichero:
      for linea in lineas:
        if linea.split(sep="|")[0] == nombre:
          escribir_fichero(nombre_fichero, nombre, cantidad, precio)
        else:
          #fichero.write(linea)
          escribir_fichero(nombre_fichero, linea.split(sep="|")[0], linea.split(sep="|")[1], linea.split(sep="|")[2].rstrip())
    print("-------------------------------------------")
    
  elif opcion == "4":
    print("-------------------------------------------")
    nombre = input("Nombre producto a BORRAR: ")
    
    with open(nombre_fichero, "r") as fichero:
      lineas = fichero.readlines()

    with open(nombre_fichero, "w") as fichero:
      for linea in lineas:
        if linea.split(sep="|")[0] != nombre:
          escribir_fichero(nombre_fichero, linea.split(sep="|")[0], linea.split(sep="|")[1], linea.split(sep="|")[2].rstrip())
    print("-------------------------------------------")
    
  elif opcion == "5":
    print("-------------------------------------------")
    print("Listando mis produdctos:")
    with open(nombre_fichero, "r") as file:
      print(file.read())
    print("-------------------------------------------")

  elif opcion == "6":
    print("-------------------------------------------")
    venta_total = 0
    with open(nombre_fichero, "r") as fichero:
      for linea in fichero.readlines():
        if linea.split(sep="|")[0] != "nombre": # es la cabecera
          cantidad = int(linea.split(sep="|")[1])
          precio = float(linea.split(sep="|")[2].rstrip())
          venta_total += (cantidad * precio)
    print(f"la cantidad de total de ventas es de {venta_total:.2f}")
    print("-------------------------------------------")
    
  elif opcion == "7":
    print("-------------------------------------------")
    venta_producto = 0
    nombre = input("Nombre producto a calcular venta: ")
    venta_total = 0
    with open(nombre_fichero, "r") as fichero:
      for linea in fichero.readlines():
        if linea.split(sep="|")[0] == nombre:
          cantidad = int(linea.split(sep="|")[1])
          precio = float(linea.split(sep="|")[2].rstrip())
          venta_producto = (cantidad * precio)
    print(f"la cantidad de ventas del producto {nombre} es de {venta_producto:.2f}")
    print("-------------------------------------------")
    
  elif opcion == "8":
    os.remove(nombre_fichero)
    break
    
  else:
    print("Selecciona una opción válida")


  
    



