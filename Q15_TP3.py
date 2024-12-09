def contar_repeticoes(string, caractere):
    if not string:
        return 0
    if string[0] == caractere:
        return 1 + contar_repeticoes(string[1:], caractere)
    else:
        return contar_repeticoes(string[1:], caractere)

resultado = contar_repeticoes("banana", "a")
print(resultado)