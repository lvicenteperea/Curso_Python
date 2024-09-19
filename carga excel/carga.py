#  pip install pandas mysql-connector-python openpyxl

import pandas as pd
import mysql.connector
from mysql.connector import Error

# Conexión a la base de datos MySQL
def conectar_db():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Admin',
            database='world'
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
        return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Cerrar conexión
def cerrar_conexion(conexion):
    if conexion.is_connected():
        conexion.close()
        print("Conexión cerrada.")

# Crear la tabla en MySQL basada en el nombre de la pestaña y el contenido del DataFrame
def crear_tabla(cursor, nombre_tabla, df):
    # Crear el esquema SQL para la tabla
    columnas_sql = []
    for columna in df.columns:
        tipo_dato = inferir_tipo_dato(df[columna])
        columnas_sql.append(f"`{columna}` {tipo_dato}")

    columnas_definicion = ", ".join(columnas_sql)
    sql_creacion = f"CREATE TABLE IF NOT EXISTS `{nombre_tabla}` ({columnas_definicion})"
    
    # Ejecutar la creación de la tabla
    cursor.execute(sql_creacion)

# Inferir el tipo de dato SQL basado en los valores de la columna
def inferir_tipo_dato(serie):
    if pd.api.types.is_integer_dtype(serie):
        return "INT"
    elif pd.api.types.is_float_dtype(serie):
        return "FLOAT"
    elif pd.api.types.is_datetime64_any_dtype(serie):
        return "DATETIME"
    else:
        return "VARCHAR(255)"

# Insertar los datos del DataFrame en la tabla MySQL
def insertar_datos(cursor, conexion, nombre_tabla, df):
    columnas = ", ".join([f"`{col}`" for col in df.columns])
    valores = ", ".join(["%s"] * len(df.columns))
    sql_insert = f"INSERT INTO `{nombre_tabla}` ({columnas}) VALUES ({valores})"

    # Insertar fila por fila
    for fila in df.itertuples(index=False, name=None):
        cursor.execute(sql_insert, fila)
    
    # Confirmar los cambios
    conexion.commit()

# Función principal para procesar el archivo Excel y cargar en la BBDD
def procesar_excel_y_cargar_datos(ruta_excel):
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()

        # Leer todas las pestañas del archivo Excel
        xls = pd.ExcelFile(ruta_excel)

        for nombre_pestana in xls.sheet_names:
            # Leer cada pestaña en un DataFrame
            df = pd.read_excel(xls, sheet_name=nombre_pestana)
            
            # Crear la tabla en MySQL
            crear_tabla(cursor, nombre_pestana, df)
            # Insertar los datos
            insertar_datos(cursor, conexion, nombre_pestana, df)
            print(f"Tabla '{nombre_pestana}' creada y datos insertados.")

        cerrar_conexion(conexion)

# Ruta del archivo Excel (reemplaza con la ruta correcta)
ruta_excel = "/mnt/data/todos juntos.xlsx"

# Procesar el archivo Excel y cargar los datos en MySQL
procesar_excel_y_cargar_datos(ruta_excel)

