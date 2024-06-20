'''
def recursiva():
    recursiva()

recursiva()

Un ejemplo muy claro es el de la torres de hanoi, que es un problema de programación dinámica que consiste en mover n discos de una torre
'''

#-------------------------------------------------------------------
# lo hace, pero la recursividad no es para esto..... es mas complicado, mas propensa a errores,....
def cuenta_atras(n: int):
  if n >= 0:
    print(n)
    cuenta_atras(n-1)
  

cuenta_atras(10)
#-------------------------------------------------------------------

def factorial(n: int) -> int:
  if n == 0:
    return 1
  elif n < 0:
    print(f"{n} es un negativo y no se puede factorizar")
    return 0
  else:
    return n * factorial(n-1)


factorial_de = 0
print(f"El factorial de {factorial_de} es: {factorial(factorial_de)}")

factorial_de = 1
print(f"El factorial de {factorial_de} es: {factorial(factorial_de)}")

factorial_de = -1
print(f"El factorial de {factorial_de} es: {factorial(factorial_de)}")

factorial_de = 5
print(f"El factorial de {factorial_de} es: {factorial(factorial_de)}")

#-------------------------------------------------------------------
def fibonacci(posicion: int) -> int:
  if posicion <= 0:
    return -1 # No es real, pero el calculo de fibonacci empieza con el 0 y el 1 son dos valores obligatorios para calcular el resto de la serie. Por eso pongo -1, Es una convención mia
  elif posicion == 1:
    return 0 # el calculo de fibonacci empieza con el 0 y el 1 son dos valores obligatorios para calcular el resto de la serie
  elif posicion == 2:
    return 1 # el calculo de fibonacci empieza con el 0 y el 1 son dos valores obligatorios para calcular el resto de la serie
  else:
    return fibonacci(posicion-1) + fibonacci(posicion-2)


print("----------------------------------------")
print("----------------------------------------")
fibonacci_de = 0
print(f"El fibonacci de {fibonacci_de} es: {fibonacci(fibonacci_de)}")

fibonacci_de = 1
print(f"El fibonacci de {fibonacci_de} es: {fibonacci(fibonacci_de)}")

fibonacci_de = 2
print(f"El fibonacci de {fibonacci_de} es: {fibonacci(fibonacci_de)}")

fibonacci_de = 3
print(f"El fibonacci de {fibonacci_de} es: {fibonacci(fibonacci_de)}")

fibonacci_de = 10
print(f"El fibonacci de {fibonacci_de} es: {fibonacci(fibonacci_de)}")

#-------------------------------------------------------------------
#-------------------------------------------------------------------
print("----------------------------------------")
print("----------------------------------------")
print("TORRE DE HANOI")

def hanoi(n, source, target, auxiliary):
  if n > 0:
      # Mover n - 1 discos de origen a auxiliar
      hanoi(n - 1, source, auxiliary, target)

      # Mover el disco n de origen a destino
      print(f"Mover disco {n} de {source} a {target}")

      # Mover los n - 1 discos de auxiliar a destino
      hanoi(n - 1, auxiliary, target, source)

  return n

# Número de discos
n_discos = 3

# Los postes se nombran A, B y C
print(hanoi(n_discos, 'A', 'B', 'C'))
#-------------------------------------------------------------------

#-------------------------------------------------------------------
#-------------------------------------------------------------------
print("----------------------------------------")
print("Backtracking")
print("----------------------------------------")

list_numbers1 = [1, 5, 3, 2]
list_numbers2 = [1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,]
objetivo = 6

def find_sums(numbers: list, objetivo: int) -> list:
  
    def find_sum(start:int, objetivo: int, combinacion: list):
        #solución encontrada
        if objetivo == 0:
          result.append(combinacion[:])
          return combinacion
        
    
        #no posee solución
        if objetivo < 0 or start == len(numbers):
          return  
  
        #búsqueda
        for index in range(start, len(numbers)):
  
          if index > start and numbers[index] == numbers[index - 1]:
              continue
  
            
          combinacion.append(numbers[index])
          find_sum(index+1, objetivo - numbers[index], combinacion)
          combinacion.pop()

  
  
    numbers.sort()
    result = []
    find_sum(0, objetivo, [] )
    return result



print(f"Para la lsita {list_numbers1} sales estos resutlados {find_sums(list_numbers1, objetivo)}")
print(f"Para la lsita {list_numbers2} sales estos resutlados {find_sums(list_numbers2, objetivo)}")
print("----------------------------------------")

#-------------------------------------------------------------------
#-------------------------------------------------------------------
print("----------------------------------------")
print("Sumar los primeros N números")
print("----------------------------------------")

def suma_recursiva(n):
  if n == 0:
    return 0
  else:
    return n + suma_recursiva(n-1)

n = 5
print(f"La suma de los {n} primeros números da {suma_recursiva(n)}")