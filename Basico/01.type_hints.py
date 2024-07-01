print("************************************************************")
print("Type Hints")
print("************************************************************")
mi_string = "Este es mi string" 
print(f"{type(mi_string)} - {mi_string}")

mi_string = 10
print(f"{type(mi_string)} - {mi_string}")

print("")
print("Puedo tipar la variable, pero es un tipado debil, ya que no pasa nada")
mi_typed_string: str = "Este es mi string Tipado"
print(f"{type(mi_typed_string)} - {mi_typed_string}")

mi_typed_string = 10
print(f"{type(mi_typed_string)} - {mi_typed_string}")

print("")
print("pero me ayuda con el IDE")
mi_typed_string: str = "este es mi string Tipado"
mi_typed_int = 10

print(f"{type(mi_typed_string)} - {mi_typed_string}")
print(f"{type(mi_typed_int)} - {mi_typed_int}")

print(f"Longitud: {mi_typed_int.bit_length()}")
print(mi_typed_string.capitalize() + " --> Capitalizado")

