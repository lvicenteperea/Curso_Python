'''
print("---------------------------------------------")
print("  ejercicio 1")
print("---------------------------------------------")

try:
  print(10/0)  # Error a capturar

except ZeroDivisionError:
  print("No se puede dividir por cero")

except Exception:
  print("No se pueden cometer errores")


print("---------------------------------------------")
print("  ejercicio 2")
print("---------------------------------------------")
try:
  print(10/1)

  my_list = [1,2,3]
  print(my_list[5])

except ZeroDivisionError:
  print("No se puede dividir por cero")

except Exception as e:
  print(f"No se pueden cometer errores: {e}")
  print(f"\t{type(e).__name__}")
'''


print("---------------------------------------------")
print("  ejercicio 3")
print("---------------------------------------------")
class MiExcepcion(Exception):
  pass


def process_params(parametros: list):

  if len(parametros) < 3:
    raise IndexError()
  elif type(parametros[1]) == str:
    raise MiExcepcion("El segundo parametro no puede ser un string")
  elif parametros[1] == 0:
    raise ZeroDivisionError()

  print(parametros[2])
  print(parametros[0]/parametros[1])
  print(parametros[1]+5)
  print(parametros[0]/parametros[2])

#-------------------------------------------------------------

try:
  #print("")
  #print("  No da eror")
  #process_params([1,2,3])

  #print("")
  #print("  error de tamaño - Comentar si se quiere ver el siguiente")
  #process_params([1,2])


  #print("")
  #print("  Error de división - Comentar si se quiere ver el siguiente")
  #process_params([1,0,3])
  
  #print("")
  #print("  Error con excepción creada por mi 'MiExcepcion' - Comentar si se quiere ver el siguiente")
  #process_params([1,"Texto",3])
  

  print("")
  print("  Error No controlado específicamente - Comentar si se quiere ver el siguiente")
  process_params([1, 2, "Texto"])
  
except ZeroDivisionError as e:
  print(f"No se puede dividir por cero {type(e).__name__}") 
except IndexError as e:
  print(f"No se han pasado suficientes parametros: {type(e).__name__}")  
except MiExcepcion as e:
  print(f"Error de tipo MiExcepcion: {type(e).__name__}")  
except Exception as e:
  print(f"Error inexperado {type(e).__name__}: {e}")
else:
  print("")
  print("---------- No se ha producido error.....")
finally:
  print("")
  print("---------- Esto se ejecuta siempre.....")


print("")
print("---------- Programa finalizado sin sacar errores")

