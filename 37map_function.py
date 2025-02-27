'''
A função map() é usada para aplicar uma função a cada item de um iterável (como uma lista ou tupla) e retorna um iterador com os resultados. É útil quando você quer transformar todos os elementos de uma coleção sem precisar escrever um loop explícito.

Aqui estão alguns exemplos bem explicados para você entender o uso do map():
'''

# 📌 Exemplo 1: Dobrar todos os números de uma lista:
numeros = [1, 2, 3, 4, 5]

# Função que dobra um número
def dobrar(num):
    return num * 2

# Usando map para aplicar a função a todos os elementos
dobrados = list(map(dobrar, numeros))

print(dobrados)  # Saída: [2, 4, 6, 8, 10]
# ✅ Aqui usamos map() para dobrar todos os números da lista sem precisar de um loop for.




# 📌 Exemplo 2: Usando map() com lambda:
numeros = [1, 2, 3, 4, 5]

# Usando lambda para evitar criar uma função separada
dobrados = list(map(lambda num: num * 2, numeros))

print(dobrados)  # Saída: [2, 4, 6, 8, 10]
# ✅ O código fica mais curto e direto, já que usamos lambda.




# 📌 Exemplo 3: Converter uma lista de temperaturas de Celsius para Fahrenheit:
celsius = [0, 10, 20, 30, 40]

# Fórmula para converter Celsius para Fahrenheit
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

print(fahrenheit)  # Saída: [32.0, 50.0, 68.0, 86.0, 104.0]
#✅ O map() ajuda a converter todos os valores da lista sem precisar de um loop.




# 📌 Exemplo 4: Pegando apenas os nomes de uma lista de dicionários:
pessoas = [
    {"nome": "Alice", "idade": 25},
    {"nome": "Bruno", "idade": 17},
    {"nome": "Carlos", "idade": 30},
    {"nome": "Daniela", "idade": 16},
]

# Pegando apenas os nomes
nomes = list(map(lambda pessoa: pessoa["nome"], pessoas))

print(nomes)  # Saída: ['Alice', 'Bruno', 'Carlos', 'Daniela']
# ✅ Aqui usamos map() para extrair apenas os nomes das pessoas.




# 📌 Exemplo 5: Elevando números ao quadrado:
numeros = [2, 3, 4, 5]

# Aplicando a função de elevar ao quadrado
quadrados = list(map(lambda x: x ** 2, numeros))

print(quadrados)  # Saída: [4, 9, 16, 25]
# ✅ map() permite transformar rapidamente todos os elementos da lista.




# 📌 Exemplo 6: Trabalhando com múltiplas listas:
numeros1 = [1, 2, 3, 4]
numeros2 = [5, 6, 7, 8]

# Somando os elementos correspondentes das duas listas
soma = list(map(lambda x, y: x + y, numeros1, numeros2))

print(soma)  # Saída: [6, 8, 10, 12]
# ✅ map() pode trabalhar com múltiplas listas ao mesmo tempo.




'''
🤔 Quando usar map()?
	•	Quando você precisa aplicar a mesma função a todos os elementos de uma coleção.
	•	Quando quer evitar escrever um loop explícito (for).
	•	Quando quer deixar o código mais conciso e legível.
'''

# 🔹 Dica: Se o objetivo for apenas criar uma nova lista com os valores transformados, o uso de list comprehension pode ser uma alternativa mais legível:
dobrados = [num * 2 for num in numeros]
# Em muitos casos, list comprehension é preferida porque é mais fácil de entender do que map().