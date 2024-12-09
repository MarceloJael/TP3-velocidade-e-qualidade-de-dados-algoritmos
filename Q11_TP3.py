# PROBLEMA

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

if __name__ == "__main__":
    try:
        print(fatorial(1000))
    except RecursionError as e:
        print("Erro de Recursão:", e)
        
# SOLUÇÃO

def fatorial_iterativo(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

if __name__ == "__main__":
    print(fatorial_iterativo(1000))