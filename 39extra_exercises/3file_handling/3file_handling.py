'''
📌 Exercício: Gerenciamento de Notas em Arquivo

Você foi contratado para desenvolver um pequeno sistema que gerencie notas de alunos. O sistema deve permitir armazenar, ler e processar informações de um arquivo de texto.

Requisitos

1️⃣ Criação de Arquivo:
	•	Crie um arquivo chamado notas.txt e escreva nele as notas de cinco alunos.
	•	Cada linha do arquivo deve conter o nome do aluno e três notas separadas por vírgula.
	•	Exemplo de conteúdo do arquivo:

Ana,7.5,8.0,9.0
Bruno,6.0,5.5,7.0
Carla,9.0,8.5,10.0
Daniel,4.5,6.0,5.5
Eduardo,7.0,7.5,8.0

2️⃣ Leitura e Processamento dos Dados:
	•	Leia o conteúdo do arquivo e armazene os dados em uma estrutura apropriada.
	•	Calcule a média das três notas de cada aluno.

3️⃣ Gravação de um Novo Arquivo:
	•	Crie um novo arquivo chamado medias.txt.
	•	Escreva nele o nome do aluno e sua média, separando os valores por dois pontos (:).
	•	Exemplo do novo arquivo gerado:

Ana: 8.17
Bruno: 6.17
Carla: 9.17
Daniel: 5.33
Eduardo: 7.5

4️⃣ Exibição dos Resultados:
	•	Após processar os dados, exiba no terminal o nome do aluno e sua média.

🔹 Dicas:
	•	Utilize open() para abrir e escrever arquivos.
	•	Use with open(...) para garantir que os arquivos sejam fechados corretamente.
	•	Lembre-se de converter as notas para float antes de calcular a média.
	•	Utilize round(valor, 2) para arredondar a média para duas casas decimais.
'''

'''with open("notas.txt", "w") as arq:
	while int(input('Digite 1 para seguir cadastrando ou 2 para salvar: ')) == 1:
		arq.write(input('Digite o nome do aluno: ') + ',')
		arq.write(input('Digite as notas do aluno separado por vírgula: \n'))
'''


def cadastrar_aluno():
    """Cadastra um aluno e suas notas no arquivo notas.txt."""
    with open("notas.txt", "a") as arquivo:
        nome = input("Digite o nome do aluno: ").strip()
        notas = []  # Lista para armazenar as notas

        qtd_notas = int(input(f"Quantas notas deseja cadastrar para {nome}? "))

        for i in range(qtd_notas):
            while True:
                try:
                    nota = float(input(f"Digite a nota {i + 1}: "))
                    notas.append(str(nota))  # Armazena como string
                    break
                except ValueError:
                    print("Entrada inválida! Digite um número válido.")

        # Escreve no arquivo no formato: Nome,Nota1,Nota2,...
        linha = nome + "," + ",".join(notas) + "\n"
        arquivo.write(linha)
        
        print(f"Aluno {nome} cadastrado com sucesso!\n")


def exibir_notas():
    """Lê e exibe todas as notas cadastradas."""
    try:
        with open("notas.txt", "r") as arquivo:
            linhas = arquivo.readlines()

            if not linhas:
                print("Nenhum aluno cadastrado.\n")
                return

            print("📋 Lista de alunos e notas:")
            for linha in linhas:
                dados = linha.strip().split(",")  # Remove espaços extras e separa por vírgula
                nome = dados[0]
                notas = dados[1:]  # Pega todas as notas

                print(f"Aluno: {nome} - Notas: {', '.join(notas)}")
            print()
    except FileNotFoundError:
        print("Ainda não há notas cadastradas.\n")


def salvar_medias(medias):
    """Salva as médias dos alunos no arquivo medias.txt."""
    with open("medias.txt", "w") as arquivo:
        arquivo.writelines(medias)


def calcular_media():
    """Calcula e exibe a média das notas de cada aluno."""
    try:
        with open("notas.txt", "r") as arquivo:
            linhas = arquivo.readlines()

            if not linhas:
                print("Não há notas cadastradas para calcular a média.\n")
                return

            medias = []
            print("📊 Médias dos alunos:")
            for linha in linhas:
                dados = linha.strip().split(",")  # Remove espaços extras e separa por vírgula
                nome = dados[0]  # O primeiro item é o nome
                notas = list(map(float, dados[1:]))  # Converte as notas para float
                
                if notas:  # Se houver notas, calcula a média
                    media = sum(notas) / len(notas)
                    print(f"Aluno: {nome} - Média: {media:.2f}")
                    medias.append(f"{nome}: {media:.2f}\n")
                else:
                    print(f"Aluno: {nome} - Nenhuma nota cadastrada.")

            salvar_medias(medias)
            print("Médias salvas no arquivo 'medias.txt'.\n")

    except FileNotFoundError:
        print("Ainda não há notas cadastradas.\n")


def menu():
    """Exibe um menu para o usuário interagir com o programa."""
    while True:
        print("📌 Menu:")
        print("1 - Cadastrar Aluno e Notas")
        print("2 - Exibir Notas")
        print("3 - Calcular Média e Salvar")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            exibir_notas()
        elif opcao == "3":
            calcular_media()
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.\n")


# 🚀 Inicia o programa chamando o menu
menu()