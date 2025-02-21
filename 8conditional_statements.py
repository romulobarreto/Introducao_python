#🔹 Exemplos Práticos de if, elif, else:

#📌 Exemplo 1: Verificando se um número é positivo, negativo ou zero:
numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
''' 📌 Explicação:
	•	Se numero for maior que 0, imprime “O número é positivo”.
	•	Se for menor que 0, imprime “O número é negativo”.
	•	Se não for nem maior nem menor, então só pode ser 0.'''




# 📌 Exemplo 2: Verificando a maioridade:
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
'''📌 Explicação:
	•	Se a idade for 18 ou mais, a pessoa é maior de idade.
	•	Caso contrário, é menor de idade.'''




#📌 Exemplo 3: Classificação de notas:
nota = float(input("Digite sua nota: "))

if nota >= 9:
    print("Sua nota é A.")
elif nota >= 7:
    print("Sua nota é B.")
elif nota >= 5:
    print("Sua nota é C.")
else:
    print("Sua nota é D.")
'''📌 Explicação:
	•	Se a nota for 9 ou mais → A
	•	Se for entre 7 e 8.9 → B
	•	Se for entre 5 e 6.9 → C
	•	Abaixo de 5 → D'''

