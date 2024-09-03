import mariadb
import sys

def create_table_in_another_db(table_name):
    # Lee los detalles de la conexión desde el archivo "mariadb2"
    try:
        with open("mariadb2", "r") as f:
            lines = f.readlines()
            user = lines[0].strip()
            password = lines[1].strip()
            host = lines[2].strip()
            port = int(lines[3].strip())
            database = lines[4].strip()
    except FileNotFoundError:
        print("Error: el archivo mariadb2 no se encontró.")
        sys.exit(1)

    # Conéctate a la base de datos de origen
    try:
        source_conn = mariadb.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )
    except mariadb.Error as e:
        print(f"Error al conectar a la base de datos de origen: {e}")
        sys.exit(1)

    source_cursor = source_conn.cursor()

    # Obtiene la estructura y los datos de la tabla de origen
    try:
        source_cursor.execute(f"SELECT * FROM {table_name}")
        table_structure = source_cursor.description
        table_data = source_cursor.fetchall()
    except mariadb.Error as e:
        print(f"Error al recuperar los datos de la tabla de origen: {e}")
        sys.exit(1)

    # Conéctate a la base de datos de destino
    try:
        target_conn = mariadb.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database="nombre_base_de_datos_destino"  # Cambia esto al nombre de tu base de datos de destino
        )
    except mariadb.Error as e:
        print(f"Error al conectar a la base de datos de destino: {e}")
        sys.exit(1)

    target_cursor = target_conn.cursor()

    # Crea la tabla en la base de datos de destino
    try:
        create_table_query = f"CREATE TABLE {table_name} ("
        for column in table_structure:
            column_name = column[0]
            column_type = column[1]
            create_table_query += f"{column_name} {column_type}, "
        create_table_query = create_table_query.rstrip(", ") + ")"
        target_cursor.execute(create_table_query)
        print(f"Tabla {table_name} creada con éxito en la base de datos de destino.")
    except mariadb.Error as e:
        print(f"Error al crear la tabla en la base de datos de destino: {e}")
        sys.exit(1)

    # Inserta los datos en la tabla de destino
    try:
        for row in table_data:
            insert_query = f"INSERT INTO {table_name} VALUES ("
            for value in row:
                insert_query += f"'{value}', "
            insert_query = insert_query.rstrip(", ") + ")"
            target_cursor.execute(insert_query)
        target_conn.commit()
        print(f"Datos insertados con éxito en {table_name} en la base de datos de destino.")
    except mariadb.Error as e:
        print(f"Error al insertar datos en la base de datos de destino: {e}")
        sys.exit(1)

    # Cierra las conexiones
    source_conn.close()
    target_conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python create_table.py <nombre_tabla>")
        sys.exit(1)
    table_name = sys.argv[1]
    create_table_in_another_db(table_name)
