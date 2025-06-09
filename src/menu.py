import os
from gerenciador_biblioteca import listar_documentos, adicionar_documento, renomear_documento, remover_documento

def menu():
    caminho_base = "../docs"

    while True:
        print("\n===== Biblioteca Digital =====")
        print("1. Listar documentos")
        print("2. Adicionar documento")
        print("3. Renomear documento")
        print("4. Remover documento")
        print("5. Sair")

        escolha = input("Escolha uma opção (1-5): ")

        if escolha == "1":
            listar_documentos(caminho_base)

        elif escolha == "2":
            origem = input("Digite o caminho do arquivo a adicionar: ")
            adicionar_documento(origem, caminho_base)

        elif escolha == "3":
            caminho = input("Digite o caminho atual do arquivo: ")
            novo_nome = input("Digite o novo nome do arquivo (ex: novo_nome.pdf): ")
            renomear_documento(caminho, novo_nome)

        elif escolha == "4":
            caminho = input("Digite o caminho do arquivo a remover: ")
            remover_documento(caminho)

        elif escolha == "5":
            print("Saindo da aplicação. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
