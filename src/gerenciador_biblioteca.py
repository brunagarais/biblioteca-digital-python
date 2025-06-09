import os
from datetime import datetime

def listar_documentos(caminho_base):
    """
    Lista os documentos digitais do diretório base, organizados por tipo de arquivo e ano de modificação.
    """
    if not os.path.exists(caminho_base):
        print(f"O diretório '{caminho_base}' não existe.")
        return

    documentos = {}

    for raiz, _, arquivos in os.walk(caminho_base):
        for nome_arquivo in arquivos:
            caminho_completo = os.path.join(raiz, nome_arquivo)
            extensao = os.path.splitext(nome_arquivo)[1].lower().strip(".")
            ano = datetime.fromtimestamp(os.path.getmtime(caminho_completo)).year

            chave = f"{extensao.upper()} - {ano}"
            if chave not in documentos:
                documentos[chave] = []
            documentos[chave].append(nome_arquivo)

    if not documentos:
        print("Nenhum documento encontrado.")
        return

    for chave in sorted(documentos):
        print(f"\n📁 {chave}")
        for doc in sorted(documentos[chave]):
            print(f"   └── {doc}")
# Exemplo de teste (ajuste o caminho conforme necessário)
if __name__ == "__main__":
    caminho_para_testar = "../docs"  # Você pode mudar para qualquer pasta com arquivos
    listar_documentos(caminho_para_testar)
import shutil

def adicionar_documento(origem, destino_base):
    """
    Move um documento para a biblioteca, organizando-o por tipo e ano de modificação.
    """
    if not os.path.isfile(origem):
        print(f"Arquivo '{origem}' não encontrado.")
        return

    extensao = os.path.splitext(origem)[1].lower().strip(".")
    ano = datetime.fromtimestamp(os.path.getmtime(origem)).year

    destino_final = os.path.join(destino_base, extensao, str(ano))

    os.makedirs(destino_final, exist_ok=True)

    nome_arquivo = os.path.basename(origem)
    destino_arquivo = os.path.join(destino_final, nome_arquivo)

    try:
        shutil.move(origem, destino_arquivo)
        print(f"✅ Documento movido para: {destino_arquivo}")
    except Exception as e:
        print(f"❌ Erro ao mover o documento: {e}")
if __name__ == "__main__":
    caminho_para_testar = "../docs"
    listar_documentos(caminho_para_testar)

    # Exemplo: mover um arquivo solto para a biblioteca
    # Crie um arquivo de teste fora da pasta docs antes de rodar
    arquivo_a_adicionar = "../livro_novo_2022.pdf"
    adicionar_documento(arquivo_a_adicionar, caminho_para_testar)
