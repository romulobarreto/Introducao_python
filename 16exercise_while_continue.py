# Escreva um programa que recebe as notas de um aluno (0 - 10), caso a nota digitada esteja fora desse intervalo, peça para o usuário digitar novamente:


notas = []

while len(notas) < 4:
    try:
        nota = float(input("Digite a nota: \n"))
    except:
        print('Digite uma nota válida.')
        continue
    if nota < 0 or nota > 10:
        print('Digite uma nota válida.')
        continue
    else:
        notas.append(nota)

print(f'As notas são: {notas}.')