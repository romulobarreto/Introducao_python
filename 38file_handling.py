'''
A manipulação de arquivos em Python envolve operações como leitura, escrita, adição de conteúdo e manipulação de arquivos binários. Aqui estão alguns exemplos bem explicados para cada situação:
'''

# 📌 1. Abrindo e Lendo um Arquivo de Texto (open + read):
# Abrindo um arquivo em modo de leitura ('r')
with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()  # Lendo todo o conteúdo do arquivo
    print(conteudo)
# ✅ Explicação: O arquivo é aberto no modo de leitura ("r"). O with garante que ele será fechado automaticamente.




# 📌 2. Lendo um Arquivo Linha por Linha (readline e readlines):
with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    print(arquivo.readline())  # Lê apenas a primeira linha

with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()  # Retorna uma lista com todas as linhas
    print(linhas)
'''
✅ Explicação:
	•	readline() lê uma única linha do arquivo.
	•	readlines() retorna uma lista onde cada elemento é uma linha do arquivo.
'''




# 📌 3. Escrevendo em um Arquivo (write):
# Modo "w" sobrescreve o arquivo se ele já existir
with open("novo_arquivo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Primeira linha do arquivo.\n")
    arquivo.write("Segunda linha do arquivo.\n")
# ✅ Explicação: O modo "w" cria o arquivo caso ele não exista. Se já existir, ele é sobrescrito.




# 📌 4. Adicionando Conteúdo a um Arquivo (append):
# Modo "a" adiciona conteúdo ao final do arquivo sem apagar o que já existe
with open("novo_arquivo.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Essa linha foi adicionada!\n")
# ✅ Explicação: O modo "a" mantém o conteúdo do arquivo e apenas adiciona novas linhas.




# 📌 5. Trabalhando com Arquivos Binários:
# 🔹 Escrevendo Dados Binários (wb)
dados_binarios = b'\x50\x79\x74\x68\x6F\x6E'  # Representação binária da palavra "Python"

with open("arquivo_binario.dat", "wb") as arquivo:
    arquivo.write(dados_binarios)
# ✅ Explicação: O modo "wb" escreve arquivos em formato binário.

# 🔹 Lendo Dados Binários (rb)
with open("arquivo_binario.dat", "rb") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)  # Saída: b'Python'
# ✅ Explicação: O modo "rb" lê o conteúdo do arquivo binário e retorna os dados como bytes.




# 📌 6. Gravando e Lendo Objetos com pickle (Serialização de Dados):
# O módulo pickle permite salvar estruturas de dados Python (listas, dicionários, etc.) em arquivos binários e recuperá-las depois.

# 🔹 Salvando um Objeto com pickle
import pickle

dados = {"nome": "Alice", "idade": 25, "cidade": "São Paulo"}

with open("dados.pickle", "wb") as arquivo:
    pickle.dump(dados, arquivo)  # Serializa e salva os dados
# ✅ Explicação: O pickle.dump() grava os dados no arquivo binário.

# 🔹 Lendo um Objeto com pickle
with open("dados.pickle", "rb") as arquivo:
    dados_carregados = pickle.load(arquivo)  # Lê e desserializa os dados
    print(dados_carregados)  # Saída: {'nome': 'Alice', 'idade': 25, 'cidade': 'São Paulo'}
# ✅ Explicação: O pickle.load() reconstrói o objeto original.




# 📌 7. Usando os para Manipular Arquivos (Renomear, Apagar, Verificar):
import os

# Renomear um arquivo
os.rename("novo_arquivo.txt", "arquivo_renomeado.txt")

# Verificar se um arquivo existe
if os.path.exists("arquivo_renomeado.txt"):
    print("O arquivo existe.")

# Remover um arquivo
os.remove("arquivo_renomeado.txt")
print("Arquivo removido.")
# ✅ Explicação: O módulo os permite renomear, verificar e excluir arquivos do sistema.




# 📌 8. Usando shutil para Copiar Arquivos:
import shutil

# Copiando um arquivo
shutil.copy("dados.pickle", "backup_dados.pickle")
print("Arquivo copiado com sucesso!")
# ✅ Explicação: O shutil.copy() copia um arquivo para outro local.