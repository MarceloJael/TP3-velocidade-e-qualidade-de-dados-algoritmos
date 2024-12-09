def soma_lista(lista):
    if not lista:
        return 0
    return lista[0] + soma_lista(lista[1:])

if __name__ == "__main__":
    lista_exemplo = [1, 2, 3, 4, 5]
    resultado = soma_lista(lista_exemplo)
    print("A soma dos elementos da lista é:", resultado)