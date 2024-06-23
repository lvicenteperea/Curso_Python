
def decimal_a_binnario(decimal: int):

    binario = ""

    while decimal > 0:
        binario = f"{decimal % 2}{binario}"
        decimal //= 2
        print(decimal)

    return "0" if binario == "" else binario


decimal = int(input("Por favor, introduce un número entero: "))
print(decimal_a_binnario(decimal))


