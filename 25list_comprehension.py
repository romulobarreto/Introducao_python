# 🔹 O que é List Comprehension?
'''
List comprehension é uma forma concisa e eficiente de criar listas em Python. Em vez de usar um loop for tradicional para preencher uma lista, você pode gerar a lista em uma única linha.
'''

# A estrutura básica é:
# 📌 nova_lista = [expressão for item in iterável if condição]
'''
	•	expressão → O que será adicionado à lista
	•	item → Cada elemento do iterável
	•	iterável → A sequência de elementos que será percorrida
	•	condição (opcional) → Filtra os elementos antes de adicioná-los
'''

#📌 1. Criando uma lista com valores ao quadrado:
#Tradicional (usando for)
numeros = [1, 2, 3, 4, 5]
quadrados = []

for num in numeros:
    quadrados.append(num ** 2)

print(quadrados)  # [1, 4, 9, 16, 25]

#Usando List Comprehension
numeros = [1, 2, 3, 4, 5]
quadrados = [num ** 2 for num in numeros]

print(quadrados)  # [1, 4, 9, 16, 25]




# 📌 2. Criando uma lista apenas com números pares:
#Tradicional
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)

print(pares)  # [2, 4, 6, 8, 10]

# Usando List Comprehension
pares = [num for num in range(1, 11) if num % 2 == 0]
print(pares)  # [2, 4, 6, 8, 10]




# 📌 3. Criando uma lista de palavras com mais de 5 letras:
# Tradicional
palavras = ["gato", "elefante", "tigre", "leão", "girafa"]
longas = []

for palavra in palavras:
    if len(palavra) > 5:
        longas.append(palavra)

print(longas)  # ['elefante', 'girafa']

# Usando List Comprehension
longas = [palavra for palavra in palavras if len(palavra) > 5]
print(longas)  # ['elefante', 'girafa']




# 📌 4. Criando uma lista de tuplas (número e seu quadrado):
# Tradicional
numeros = [1, 2, 3, 4, 5]
tuplas = []

for num in numeros:
    tuplas.append((num, num ** 2))

print(tuplas)  # [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

#Usando List Comprehension
tuplas = [(num, num ** 2) for num in numeros]
print(tuplas)  # [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]




# 📌 5. Transformando uma lista de Celsius para Fahrenheit:
# Tradicional
celsius = [0, 10, 20, 30, 40]
fahrenheit = []

for temp in celsius:
    fahrenheit.append((temp * 9/5) + 32)

print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]

# Usando List Comprehension
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]




# 📌 6. Substituindo valores em uma lista (if-else dentro de list comprehension):
# Tradicional
numeros = [1, 2, 3, 4, 5]
nova_lista = []

for num in numeros:
    if num % 2 == 0:
        nova_lista.append("par")
    else:
        nova_lista.append("ímpar")

print(nova_lista)  # ['ímpar', 'par', 'ímpar', 'par', 'ímpar']

# Usando List Comprehension
nova_lista = ["par" if num % 2 == 0 else "ímpar" for num in numeros]
print(nova_lista)  # ['ímpar', 'par', 'ímpar', 'par', 'ímpar']




# 📌 7. Criando uma matriz (lista de listas):
# Tradicional
matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(j)
    matriz.append(linha)

print(matriz)  # [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# Usando List Comprehension
matriz = [[j for j in range(3)] for i in range(3)]
print(matriz)  # [[0, 1, 2], [0, 1, 2], [0, 1, 2]]