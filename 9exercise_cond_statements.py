# Receba 4 notas de um aluno e exiba se ele foi aprovado (nota maior ou igual a 6);
# Se ele ficou de recuperação (nota maior ou igual a 4);
# Ou se ele foi reprovado (nota menor que 4):

def calculo_nota():
    nota1 = float(input('Digite a primeira nota aqui, se houver decimal, use (.). \n'))
    nota2 = float(input('Digite a segunda nota aqui, se houver decimal, use (.). \n'))
    nota3 = float(input('Digite a terceira nota aqui, se houver decimal, use (.). \n'))
    nota4 = float(input('Digite a quarta nota aqui, se houver decimal, use (.). \n'))
    
    resultado = (nota1 + nota2 + nota3 + nota4) / 4  # Calcula a média
    
    if resultado >= 6:
        status = "APROVADO"
    elif resultado >= 4:
        status = "RECUPERAÇÃO"
    else:
        status = "REPROVADO"

    return resultado, status  # Retorna os valores

# Captura o retorno e imprime
media, situacao = calculo_nota()
print(f"Sua média é {media:.1f}")  # Exibe a média com duas casas decimais
if situacao == "RECUPERAÇÃO":
    print(f"Você está em: {situacao}")
else:
    print(f"Você foi: {situacao}")