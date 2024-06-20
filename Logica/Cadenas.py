s1 = "Hola"
s2 = "Luis Alberto"

print(list(s1))

l1 = [s1, ",", s2, "!"]
print("".join(l1))
print(" ".join(l1))


#--------------------------------------------------------------------
def check_palindrome(word:str):
  return word == word[::-1]

print(f"radar es un palindromo? {check_palindrome('radar')}")
print(check_palindrome(s1))

#--------------------------------------------------------------------
def isograma(word: str):
  word_dict = dict()
  
  for letra in word:
    word_dict[letra] = word_dict.get(letra, 0) + 1

  isogram = True
  values = list(word_dict.values())
  isogram_len = values[0]
  for word_count in values:
    if word_count != isogram_len:
      isogram = False
      break
    
  return isogram

def isograma2(cadena: str):
    conteo_caracteres = {}

    for char in cadena:
        conteo_caracteres[char] = conteo_caracteres.get(char, 0) + 1

    array_conteo_caracteres = list(conteo_caracteres.values())

    # Convertir la lista en un conjunto para eliminar duplicados
    set_conteo_caracteres = set(array_conteo_caracteres)

    # Imprimir la lista sin duplicados
    print("Lista sin duplicados:", set_conteo_caracteres)

  
    # Contar la cantidad de claves únicas, que son los caracteres únicos
    long_set_conteo_caracteres = len(set_conteo_caracteres)
    
    # Imprimir el resultado
    print("Cantidad de caracteres únicos:", long_set_conteo_caracteres)
    
    return (long_set_conteo_caracteres == 1)



c1 = "Muy buenos dias caballero"
print(f"{c1} es un isograma? {isograma(c1)} - ({isograma2(c1)})")

print("")
c1 = "luisluisluis"
print(f"{c1} es un isograma? {isograma(c1)} - ({isograma2(c1)})")
#--------------------------------------------------------------------
