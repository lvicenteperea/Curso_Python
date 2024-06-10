### Manejo de errores ###


def control_error(n1, n2):
    try:
        print(n1+n2)
        print("pero seguimos ejecutando")
    except TypeError as e:
        print(f"error: {e}")
        print(f"  - {e.__cause__}")
        print(f"  - {e.}")
        print(f"  - {e}")
    except Exception as e:
        print(f"Ha habido un error.....{e}")
    else:
        print("la ejecución continua normalmente")
    finally:
        print("Fin programa")

    


print(" Todo OK ".center(35,"*"))
control_error(1, 1)
print(" Con Error ".center(35,"*"))
control_error(1, "1")