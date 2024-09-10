from fuzzywuzzy import fuzz

print("-----------------------------------------------------")
print("Compración por porcentaje de coincidencia")
print("-----------------------------------------------------")
texto1 = "Este es el texto pequeño."
texto2 = "Este es el texto pequeño de algo mas grande y poderoso."
similitud = fuzz.ratio(texto1, texto2)
print(f"Similitud: {similitud}%")
print("")
print("")


print("-----------------------------------------------------")
print("coincidencia de palabras independientemente del orden de palabras")
print("falten o sobren eliminando las difrencias de orden")
print("-----------------------------------------------------")
# METODO .token_set_ratio
similitud_token_set = fuzz.token_set_ratio("Apple Inc. Incorporated", "Apple Inc.")
print(f"Similitud con Conjunto de Tokens: {similitud_token_set}%")

print("")
print("")


print("-----------------------------------------------------")
print("extractOne: mejor coincidencia entre una lsita de opcoines")
print("extract: lsita de coincidencias con el % de cada una")
print("-----------------------------------------------------")
# METODO .extractOne y .extract
coincidencias = fuzz.extract("Apple Inc", opciones)
print(f"Coincidencias: {coincidencias}")

opciones = ["Apple Inc.", "Apple", "Microsoft Corp.", "Google LLC"]
mejor_coincidencia = fuzz.extractOne("Apple Inc", opciones)
print(f"Mejor coincidencia: {mejor_coincidencia}")
print("")
print("")