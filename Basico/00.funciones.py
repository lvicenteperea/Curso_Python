"""
print("Hola munod")

# Se traba todo.....
def print_name(nombre: int, apellido):
    print (f"{nombre} - {apellido}")
    print (nombre + apellido)

print_name("Luis","Vicente")
print_name("5","7")
print_name(5,7)
"""

def return_suma(par1, par2):
    return par1 + par2

print ("return_suma(5, 7)")
print (return_suma(5, 7))


def return_suma_default(par1, par2, par3 = 3):
    return par1 + par2 + par3

print ("return_suma_default(5, 7)")
print (return_suma_default(5, 7))
print ("return_suma_default(5, 7, 4)")
print (return_suma_default(5, 7, 4))


def print_en_May( *texts ):
    print("Tipo parámetro: %s" % type(texts))
    for text in texts:
        print(f"Tipo campo3: %s{type(text)}")
        print (text.upper())

print("print_en_May('Texto1', 'Texto2')")
print(print_en_May("Texto1", "Texto2"))

