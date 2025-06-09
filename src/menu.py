import os
from gerenciador_biblioteca import (
    listar_documentos,
    adicionar_documento,
    renomear_documento,
    remover_documento,
    buscar_documentos_por_nome,
    resumo_documentos
)

CAMINHO_BASE = "../docs"

def exibir_menu():
    print("\n===== Biblioteca Digital =====")
    print("1. Listar documentos")
    print("2. Adicionar documento")
    print("3. Renomear documento")
    print("4. Remover documento")
    print("5. Buscar por nome")
    print("6. Resumo por tipo e ano")
    print("7. Sair")

def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            listar_documentos(CAMINHO_BASE)

        elif escolha == "2":
            origem = input("Digite o caminho do documento a adicionar: ")
            if not os.path.exists(origem):
                print("❌ Caminho inválido. Certifique-se de que o arquivo existe.")
            else:
                adicionar_documento(origem, CAMINHO_BASE)

        elif escolha == "3":
            caminho = input("Digite o caminho completo do documento a renomear: ")
            if not os.path.isfile(caminho):
                print("❌ Arquivo não encontrado. Exemplo de caminho: ../docs/pdf/2025/arquivo.pdf")
            else:
                novo_nome = input("Digite o novo nome do documento: ")
                renomear_documento(caminho, novo_nome)

        elif escolha == "4":
            caminho = input("Digite o caminho completo do documento a remover: ")
            if not os.path.isfile(caminho):
                print("❌ Arquivo não encontrado. Exemplo de caminho: ../docs/pdf/2025/arquivo.pdf")
            else:
                remover_documento(caminho)

        elif escolha == "5":
            termo = input("Digite o termo de busca: ")
            buscar_documentos_por_nome(CAMINHO_BASE, termo)

        elif escolha == "6":
            resumo_documentos(CAMINHO_BASE)

        elif escolha == "7":
            print("Saindo da biblioteca digital. Até logo!")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()