'''
A função filter() é usada para filtrar elementos de uma coleção (como listas e tuplas) com base em uma condição. Ela retorna um iterador contendo apenas os elementos que atenderem à condição especificada.

Aqui estão alguns exemplos bem explicados para você entender o uso do filter():
'''

# 📌 Exemplo 1: Filtrando números pares:
# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Função que verifica se um número é par
def eh_par(num):
    return num % 2 == 0

# Usando filter para pegar apenas os números pares
pares = list(filter(eh_par, numeros))

print(pares)  # Saída: [2, 4, 6, 8, 10]
# ✅ Aqui usamos uma função normal (def) para verificar se o número é par. O filter() percorre a lista e retorna apenas os valores que retornam True.




# 📌 Exemplo 2: Usando filter() com lambda:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usando lambda dentro do filter
pares = list(filter(lambda num: num % 2 == 0, numeros))

print(pares)  # Saída: [2, 4, 6, 8, 10]
# ✅ Aqui usamos uma função lambda diretamente dentro do filter(), o que deixa o código mais curto e direto.




# 📌 Exemplo 3: Filtrando palavras com mais de 5 letras:
palavras = ["banana", "uva", "maçã", "abacaxi", "kiwi", "laranja"]

# Filtrar palavras com mais de 5 letras
longas = list(filter(lambda palavra: len(palavra) > 5, palavras))

print(longas)  # Saída: ['banana', 'abacaxi', 'laranja']
# ✅ Aqui filtramos apenas as palavras que têm mais de 5 letras.




# 📌 Exemplo 4: Filtrando valores negativos de uma lista:
valores = [-10, -5, 0, 5, 10, 15, -20, 30]

# Pegando apenas os valores positivos
positivos = list(filter(lambda x: x >= 0, valores))

print(positivos)  # Saída: [0, 5, 10, 15, 30]
# ✅ Isso é útil quando você quer remover valores negativos de uma lista.




# 📌 Exemplo 5: Filtrando dicionários (exemplo mais avançado):
pessoas = [
    {"nome": "Alice", "idade": 25},
    {"nome": "Bruno", "idade": 17},
    {"nome": "Carlos", "idade": 30},
    {"nome": "Daniela", "idade": 16},
]

# Filtrar apenas maiores de idade
maiores = list(filter(lambda pessoa: pessoa["idade"] >= 18, pessoas))

print(maiores)
# Saída:
# [{'nome': 'Alice', 'idade': 25}, {'nome': 'Carlos', 'idade': 30}]
# ✅ Aqui usamos filter() para pegar apenas as pessoas que têm 18 anos ou mais.

'''
🤔 Quando usar filter()?
	•	Quando você precisa remover elementos indesejados de uma lista com base em uma condição.
	•	Quando a lógica de filtragem é simples e não precisa de loops explícitos.
	•	Quando você quer um código mais limpo e conciso.

🔹 Dica: Se a filtragem precisar de regras mais complexas ou manipular os dados, pode ser melhor usar list comprehensions ao invés de filter().
'''
