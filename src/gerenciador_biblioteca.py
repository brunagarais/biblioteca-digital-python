import os
import shutil
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

def renomear_documento(caminho_arquivo, novo_nome):
    """
    Renomeia um documento mantendo-o na mesma pasta.
    """
    if not os.path.isfile(caminho_arquivo):
        print(f"❌ Arquivo '{caminho_arquivo}' não encontrado.")
        return

    pasta = os.path.dirname(caminho_arquivo)
    novo_caminho = os.path.join(pasta, novo_nome)

    try:
        os.rename(caminho_arquivo, novo_caminho)
        print(f"✅ Documento renomeado para: {novo_caminho}")
    except Exception as e:
        print(f"❌ Erro ao renomear o documento: {e}")

def remover_documento(caminho_arquivo):
    """
    Remove um documento da biblioteca.
    """
    if not os.path.isfile(caminho_arquivo):
        print(f"❌ Arquivo '{caminho_arquivo}' não encontrado.")
        return

    try:
        os.remove(caminho_arquivo)
        print(f"🗑️ Documento removido: {caminho_arquivo}")
    except Exception as e:
        print(f"❌ Erro ao remover o documento: {e}")

def buscar_documentos_por_nome(caminho_base, termo):
    """
    Busca por documentos cujo nome contenha o termo fornecido (ignorando maiúsculas/minúsculas).
    """
    if not os.path.exists(caminho_base):
        print(f"O diretório '{caminho_base}' não existe.")
        return

    encontrados = []

    for raiz, _, arquivos in os.walk(caminho_base):
        for nome_arquivo in arquivos:
            if termo.lower() in nome_arquivo.lower():
                encontrados.append(os.path.join(raiz, nome_arquivo))

    if encontrados:
        print(f"\n🔍 Resultados para '{termo}':")
        for caminho in encontrados:
            print(f"   └── {caminho}")
    else:
        print(f"🔍 Nenhum documento encontrado com o termo: '{termo}'")

def resumo_documentos(caminho_base):
    """
    Exibe um resumo com o total de documentos por tipo (extensão) encontrados na biblioteca.
    """
    if not os.path.exists(caminho_base):
        print(f"O diretório '{caminho_base}' não existe.")
        return

    resumo = {}

    for raiz, _, arquivos in os.walk(caminho_base):
        for nome_arquivo in arquivos:
            extensao = os.path.splitext(nome_arquivo)[1].lower().strip(".")
            resumo[extensao] = resumo.get(extensao, 0) + 1

    if resumo:
        print("\n📊 Resumo de documentos por tipo:")
        for tipo, quantidade in sorted(resumo.items()):
            print(f"   - {tipo.upper()}: {quantidade} arquivo(s)")
    else:
        print("Nenhum documento encontrado.")
