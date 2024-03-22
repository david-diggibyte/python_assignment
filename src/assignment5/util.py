def string_formatted(number):
    width = len(bin(number)[2:])
    formatted_output = ""

    for i in range(1, number + 1):
        deci = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]

        formatted_output += f"{deci.rjust(width)} {octa.rjust(width)} {hexa.rjust(width)} {bina.rjust(width)}\n"

    return formatted_output.rstrip("\n")

