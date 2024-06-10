def return_suma_default(par1, par2, par3 = 3):
    nRet = 0

    try:
        nRet = par1 + par2 + par3
        print("pero seguimos ejecutando")
    except TypeError as e:
        print(f"error: {e}")
        print(f"  - {e.__cause__}")
    except Exception as e:
        print(f"Ha habido un error.....{e}")
    else:
        print("la ejecución continua normalmente")
    finally:
        print("Fin programa")

    return nRet