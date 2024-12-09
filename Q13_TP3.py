def eh_palindromo(palavra):
    if len(palavra) <= 1:
        return True
    if palavra[0] != palavra[-1]:
        return False
    return eh_palindromo(palavra[1:-1])

if __name__ == "__main__":
    palavras_teste = ["arara", "radar", "python", "level", "deified", "hello"]
    for palavra in palavras_teste:
        resultado = eh_palindromo(palavra)
        print(f"A palavra '{palavra}' é um palíndromo? {resultado}")