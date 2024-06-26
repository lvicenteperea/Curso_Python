import inspect

# Define una función para imprimir el nombre de la función actual y el número de línea
def print_function_name_and_line():
    # Obtén el marco actual
    frame = inspect.currentframe()

    # Obtén el marco de llamada
    calling_frame = frame.f_back

    # Obtén el objeto de código del marco de llamada
    code = calling_frame.f_code

    # Obtén el nombre de la función
    function_name = code.co_name

    # Obtén el número de línea
    line_number = calling_frame.f_lineno
    
    # Imprime el nombre de la función y el número de línea
    print(f"Function: {function_name}, Line: {line_number}")

# Ejemplo de uso de la función
def my_test_function():
    print_function_name_and_line()  # Esto imprimirá "Function: my_test_function, Line: 23"

# Llama a la función de ejemplo
my_test_function()