# Algoritmo Recursivo de Fibonacci

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Algoritmo Recursivo de Fatorial

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)