import os

def listar_diretorio(caminho):
    """Lista todos os arquivos e subdiretórios em um diretório especificado, recursivamente."""
    try:
        itens = os.listdir(caminho)
    except PermissionError:
        print(f"Permissão negada para acessar o diretório: {caminho}")
        return
    except FileNotFoundError:
        print(f"O diretório não foi encontrado: {caminho}")
        return

    for item in itens:
        caminho_completo = os.path.join(caminho, item)
        
        if os.path.isdir(caminho_completo):
            print(f"Diretório: {caminho_completo}")
            listar_diretorio(caminho_completo)
        else:
            print(f"Arquivo: {caminho_completo}")

if __name__ == "__main__":
    caminho_inicial = input("Digite o caminho do diretório que deseja listar: ")
    listar_diretorio(caminho_inicial)