def soma_lista(lista):
    
    if not lista:
        return 0

    return lista[0] + soma_lista(lista[1:])

resultado = soma_lista([1, 2, 3, 4])
print(resultado)