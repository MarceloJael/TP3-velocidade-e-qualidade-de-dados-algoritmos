def inverter_string(string):
    if not string:
        return ""
    return string[-1] + inverter_string(string[:-1])

resultado = inverter_string("recursao")
print(resultado)