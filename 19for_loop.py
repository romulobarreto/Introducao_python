# 🔹 Exemplo 1: Percorrendo uma lista de números:
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(f"O número atual é {numero}")
# Explicação: O laço for percorre a lista numeros e exibe cada elemento.



# 🔹 Exemplo 2: Iterando sobre uma string (caractere por caractere):
palavra = "Python"

for letra in palavra:
    print(letra)
# Explicação: Cada caractere da string "Python" será impresso separadamente.



# 🔹 Exemplo 3: Usando range() para contar de 1 a 5:
for i in range(1, 6):
    print(f"Contagem: {i}")
# Explicação: range(1, 6) gera os números de 1 a 5 (o último valor não é incluído).



# 🔹 Exemplo 4: Somando os números de 1 a 10 com range():
soma = 0

for num in range(1, 11):
    soma += num  # soma = soma + num

print(f"A soma dos números de 1 a 10 é {soma}")
# Explicação: O for percorre de 1 a 10 e acumula os valores na variável soma.



# 🔹 Exemplo 5: Iterando sobre um dicionário:
aluno = {"nome": "Carlos", "idade": 20, "curso": "Engenharia"}

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
# Explicação: items() retorna pares chave: valor, permitindo percorrer um dicionário.



# 🔹 Exemplo 6: Laço for com break e continue:
for num in range(1, 11):
    if num == 5:
        print("Número 5 encontrado! Parando o loop...")
        break  # Interrompe o loop quando `num` for 5
    print(num)
#------------------------------------------------------
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Pula os números pares
    print(num)
'''Explicação:

break: Interrompe o loop quando encontra o número 5.
continue: Pula os números pares e continua a execução.
'''