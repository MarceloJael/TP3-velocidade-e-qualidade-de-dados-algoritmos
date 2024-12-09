def hanoi(n, origem, destino, auxiliar):
    """Resolve o problema da Torre de Hanói."""
    if n == 1:
        print(f"Mover disco 1 de {origem} para {destino}")
        return
    hanoi(n - 1, origem, auxiliar, destino)
    
    print(f"Mover disco {n} de {origem} para {destino}")
    
    hanoi(n - 1, auxiliar, destino, origem)

if __name__ == "__main__":
    num_discos = 3  # Número de discos
    hanoi(num_discos, 'A', 'C', 'B')  # A, C e B são os pinos