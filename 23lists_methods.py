'''🔹 O que é uma lista em Python?

Uma lista é uma estrutura de dados que pode armazenar múltiplos valores em uma única variável. Esses valores podem ser de tipos diferentes (números, strings, booleanos, etc.), e a lista pode ser modificada (adicionar, remover ou alterar elementos).'''

# 📌 Criando uma lista:
# Lista vazia
minha_lista = []

# Lista com números
numeros = [10, 20, 30, 40]

# Lista com strings
nomes = ["Alice", "Bob", "Carlos"]

# Lista mista (com tipos diferentes)
mista = [25, "Python", True, 3.14]

# 📌 Acessando elementos da lista:
# Cada item da lista tem um índice, começando do 0.
frutas = ["maçã", "banana", "laranja"]
print(frutas[0])  # 'maçã'
print(frutas[2])  # 'laranja'
# 💡 Se precisar acessar do final para o início, use índices negativos:
print(frutas[-1])  # 'laranja' (último elemento)



# 🔹 1. Adicionar elementos à lista (append e insert):
# ➤ append(): Adiciona um item ao final da lista
frutas = ["maçã", "banana"]
frutas.append("laranja")
print(frutas)  # ['maçã', 'banana', 'laranja']

# ➤ insert(): Adiciona um item em um índice específico
frutas.insert(1, "uva")  # Adiciona "uva" na posição 1
print(frutas)  # ['maçã', 'uva', 'banana', 'laranja']



# 🔹 2. Remover elementos da lista (pop e remove):
# ➤ pop(): Remove e retorna um item pelo índice (ou o último, se não especificado)
frutas = ["maçã", "banana", "laranja"]
ultima = frutas.pop()  # Remove "laranja"
print(ultima)  # 'laranja'
print(frutas)  # ['maçã', 'banana']

frutas.pop(0)  # Remove o primeiro elemento ("maçã")
print(frutas)  # ['banana']

# ➤ remove(): Remove um elemento pelo valor
frutas = ["maçã", "banana", "laranja"]
frutas.remove("banana")  # Remove "banana"
print(frutas)  # ['maçã', 'laranja']
# 🔹 Diferença: remove() busca e exclui pelo valor, enquanto pop() exclui pelo índice.



# 🔹 3. Encontrar elementos (index):
# ➤ index(): Retorna o índice de um elemento na lista
numeros = [10, 20, 30, 40]
indice = numeros.index(30)
print(indice)  # 2
# ⚠️ Se o valor não estiver na lista, ele gera um erro.



# 🔹 4. Ordenar listas (sort e sorted):
# ➤ sort(): Ordena a lista modificando-a diretamente
numeros = [4, 2, 8, 1]
numeros.sort()
print(numeros)  # [1, 2, 4, 8]

# ➤ sorted(): Retorna uma nova lista ordenada (sem alterar a original)
numeros = [4, 2, 8, 1]
ordenados = sorted(numeros)
print(ordenados)  # [1, 2, 4, 8]
print(numeros)  # [4, 2, 8, 1] (permanece igual)

# ➤ sort(reverse=True): Ordenação decrescente
numeros.sort(reverse=True)
print(numeros)  # [8, 4, 2, 1]



# 🔹 5. Enumerar listas (enumerate):
# ➤ enumerate(): Obtém índice e valor ao percorrer uma lista
nomes = ["Alice", "Bob", "Carlos"]

for indice, nome in enumerate(nomes):
    print(f"Índice {indice}: {nome}")
# Saída:
'''
Índice 0: Alice
Índice 1: Bob
Índice 2: Carlos
'''



# 🔹 6. Listas dentro de listas (matriz):
# ➤ Criando e acessando uma matriz 3x3
matriz = [
    [1, 2, 3],  # Linha 0
    [4, 5, 6],  # Linha 1
    [7, 8, 9]   # Linha 2
]

print(matriz[0])  # [1, 2, 3] (primeira linha)
print(matriz[1][2])  # 6 (linha 1, coluna 2)

# ➤ Percorrendo uma matriz
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()  # Pula para a próxima linha
# Saída:
'''
1 2 3 
4 5 6 
7 8 9
'''