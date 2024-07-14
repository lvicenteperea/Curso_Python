'''
para asegurar copia desde portatil
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



# ----------------------------------------------------------------------------
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
def mi_func():
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
  print("---------- Programa finalizado sin sacar errores o si (no lo entiendo, habiendo un Finally)")


#-------------------------------------------------------------
mi_func()




print("")
print("")
print("")
print("---------------------------------------------")
print("  ejercicio 4. Ejemplo dado por chatGPT")
print("---------------------------------------------")
class MiError(Exception):
    def __init__(self, message, details=None):
        super().__init__(message)
        self.message = message
        self.details = details

    def __str__(self):
        if self.details:
            return f"{self.message}: {self.details}"
        return self.message

def ejemplo_funcion(param):
    try:
        if param < 0:
            raise ValueError("El parámetro no puede ser negativo")
        return param * 2
    except Exception as e:
        return MiError("Ocurrió un error en ejemplo_funcion", str(e))

# Uso de la función
resultado = ejemplo_funcion(-5)
if isinstance(resultado, MiError):
    print(f"Error: {resultado}")
else:
    print(f"Resultado: {resultado}")


print("")
print("")
print("")
print("---------------------------------------------")
print("  ejercicio 5. Ejemplo dado por chatGPT y modificado por mi")
print("---------------------------------------------")
class MiError(Exception):
    def __init__(self, message, details=None):
        super().__init__(message)
        self.message = message
        self.details = details

    def __str__(self):
        if self.details:
            return f"{self.message}: {self.details}"
        return self.message

def ejemplo_funcion(param):
    if param < 0:
        return MiError("Ocurrió un error en ejemplo_funcion", "El parámetro no puede ser negativo")

    return param * 2

        

# Uso de la función
resultado = ejemplo_funcion(-5)
if isinstance(resultado, MiError):
    print(f"Error: {resultado}")
else:
    print(f"Resultado: {resultado}")

resultado = ejemplo_funcion(5)
if isinstance(resultado, MiError):
    print(f"Error: {resultado}")
else:
    print(f"Resultado: {resultado}")



print("")
print("")
print("")
print("---------------------------------------------")
print("  ejercicio 6. Ejemplo dado por chatGPT y modificado por mi, maaaaaas")
print("---------------------------------------------")
class MiError(Exception):
    def __init__(self, message, details=None, *args):
        super().__init__(message)
        self.message = message
        self.details = details
        self.args = args
        
        # Imprimir argumentos adicionales en el terminal
        if args:
            print("Argumentos adicionales:", args)
        
    def __str__(self):
        base_message = self.message
        if self.details:
            base_message += f": {self.details}"
        return base_message



def ejemplo_funcion(param):
    try:
      if param < 0:
          return MiError("Ocurrió un error en ejemplo_funcion", 
                        "El parámetro no puede ser negativo",
                        "Argumento extra 1", "Argumento extra 2")

      return param * 2

    except Exception as e:
        return MiError("Ocurrió un error en ejemplo_funcion", str(e))

# Uso de la función


print("")
print("---  Usando como parámetro -5")
resultado = ejemplo_funcion(-5)
if isinstance(resultado, MiError):
    print(f"Error1: {resultado}")
else:
    print(f"Resultado: {resultado}")


print("")
print("---  Usando como parámetro 5")
resultado = ejemplo_funcion(5)
if isinstance(resultado, MiError):
    print(f"Error2: {resultado}")
else:
    print(f"Resultado: {resultado}")


print("")
print("---  Usando como parámetro un texto")
resultado = ejemplo_funcion("ww")
if isinstance(resultado, MiError):
    print(f"Error3: {resultado}")
else:
    print(f"Resultado: {resultado}")
