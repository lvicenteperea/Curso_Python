# pip install pandas
# pip install openpyxl No hace falta en este programa, pero es aconsejable para el uso de excel
import pandas as pd
from datetime import datetime

# Definir las rutas de los archivos
ruta_base = "Ejercicios/combinar_excel/"
archivo_a = ruta_base + "LISTADO PRODUCTOS SQLPyme en TPV.xlsx"
archivo_b = ruta_base + "Listados Productos TPVs 20240926.xlsx"
ruta_salida = ruta_base + "LISTADO_PRODUCTOS_COMBINADO.xlsx"
ruta_log = ruta_base + "log.txt"

# Registrar el inicio en el archivo de log
with open(ruta_log, "a") as log:
    log.write(f"{datetime.now()}: Inicio del proceso\n")

# Leer Excel_A
excel_a = pd.read_excel(archivo_a, sheet_name="LISTADO PRODUCTOS TPV")
excel_a.set_index("Código", inplace=True)  # Índice para búsquedas rápidas

# Leer todas las pestañas de Excel_B una vez y crear diccionarios para búsquedas rápidas
prioridades = ["velazquez", "quevedo", "mg quiosco", "mg norte", "tienda y bombo SOL", "barra sol", "salon sol"]
hojas_b = {hoja: pd.read_excel(archivo_b, sheet_name=hoja).set_index("Id Plato") for hoja in prioridades if hoja in pd.ExcelFile(archivo_b).sheet_names}

# Columnas de Excel_B con el mapeo a Excel_A
mapeo_columnas = {
    "Barra": "Barra",
    "Comedor": "Comedor",
    "Orden Factura": "Orden Factura",
    "Orden Cocina": "Orden Cocina",
    "OrdenTactil": "Orden Tactil",
    "Grupo Carta 1": "Gcarta",
    "Familia": "Familia",
    "Centro": "Centro 1",
    "Centro 2": "Centro 2",
    "Centro 3": "Centro 3"
}

# Función para buscar y asignar un valor de una columna específica de acuerdo a la prioridad de hojas
def buscar_valor(codigo, columna, prioridad_hojas):
    for hoja in prioridad_hojas:
        if codigo in hojas_b[hoja].index:
            return hojas_b[hoja].at[codigo, columna]
    return None

# Recorrer cada fila de Excel_A
for codigo in excel_a.index:
    # Buscar y asignar valores mapeados según la prioridad de hojas general
    for columna_b, columna_a in mapeo_columnas.items():
        valor = buscar_valor(codigo, columna_b, prioridades)
        if valor is not None:
            excel_a.at[codigo, columna_a] = valor

    # Asignar valores específicos para Salón Sol y Terraza con sus prioridades específicas
    excel_a.at[codigo, "Salón Sol"] = buscar_valor(codigo, "Comedor", ["salon sol", "tienda y bombo SOL", "barra sol", "velazquez", "quevedo", "mg quiosco", "mg norte"])
    excel_a.at[codigo, "Terraza"] = buscar_valor(codigo, "Terraza", ["quevedo", "velazquez", "mg quiosco", "mg norte", "tienda y bombo SOL", "barra sol", "salon sol"])

# Guardar el archivo combinado
excel_a.reset_index().to_excel(ruta_salida, index=False)

# Registrar el fin en el archivo de log
with open(ruta_log, "a") as log:
    log.write(f"{datetime.now()}: Fin del proceso\n")

print(f"Proceso completado. Archivo combinado guardado en: {ruta_salida}")





'''
# Registrar el inicio del proceso en el archivo de log
with open(ruta_log, "a") as log:
    log.write(f"Inicio del proceso: {datetime.now()}\n")

# Leer Excel_A
excel_a = pd.read_excel(ruta_excel_a, sheet_name=0)

# Diccionario de mapeo entre columnas de Excel_B y Excel_A
mapeo_columnas = {
    "Barra": "Barra",
    "Comedor": "Comedor",
    "Terraza": "Terraza",
    "Orden Factura": "Orden Factura",
    "Orden Cocina": "Orden Cocina",
    "OrdenTactil": "Orden Tactil",
    "Grupo Carta 1": "Gcarta",
    "Familia": "Familia",
    "Centro": "Centro 1",
    "Centro 2": "Centro 2",
    "Centro 3": "Centro 3"
}

# Prioridades de búsqueda para cada conjunto de campos
prioridad_general = ["velazquez", "quevedo", "mg quiosco", "mg norte", "tienda y bombo SOL", "barra sol", "salon sol"]
prioridad_salon_sol = ["salon sol", "tienda y bombo SOL", "barra sol", "velazquez", "quevedo", "mg quiosco", "mg norte"]

# Leer todas las pestañas de Excel_B
excel_b = pd.ExcelFile(ruta_excel_b)
pestañas_b = excel_b.sheet_names

# Convertir pestañas de Excel_B en un diccionario de DataFrames
dfs_b = {sheet: excel_b.parse(sheet) for sheet in pestañas_b}

# Función para buscar y completar datos de Excel_A usando una pestaña específica de Excel_B
def completar_fila(codigo, df, pestaña_prioridad, columna_salon_sol=None):
    for pestaña in pestaña_prioridad:
        if pestaña not in dfs_b:
            continue  # Si la pestaña no existe en Excel_B, saltarla
        df_b = dfs_b[pestaña]
        resultado = df_b[df_b["Id Plato"] == codigo]
        if not resultado.empty:
            # Completar las columnas de mapeo general
            for col_b, col_a in mapeo_columnas.items():
                if pd.notna(resultado[col_b].values[0]):
                    df.loc[i, col_a] = resultado[col_b].values[0]
            # Completar "Salón Sol" desde Excel_B.Comedor si corresponde
            if columna_salon_sol:
                if pd.notna(resultado["Comedor"].values[0]):
                    df.loc[i, "Salón Sol"] = resultado["Comedor"].values[0]
            break

# Completar el DataFrame Excel_A
for i, row in excel_a.iterrows():
    codigo = row["Código"]
    
    # Completar las columnas según la prioridad general (excepto "Salón Sol")
    completar_fila(codigo, excel_a, prioridad_general)
    
    # Completar "Salón Sol" con la prioridad específica
    completar_fila(codigo, excel_a, prioridad_salon_sol, columna_salon_sol=True)

# Guardar el DataFrame resultante en un nuevo archivo Excel
ruta_salida = ruta + "LISTADO_PRODUCTOS_SQLPyme_COMPLETADO.xlsx"
with pd.ExcelWriter(ruta_salida, engine="openpyxl") as writer:
    excel_a.to_excel(writer, sheet_name="Combinado", index=False)

# Registrar el fin del proceso en el archivo de log
with open(ruta_log, "a") as log:
    log.write(f"Fin del proceso: {datetime.now()}\n")

print(f"El archivo combinado se ha guardado en {ruta_salida}")
'''