'''📌 Conjuntos em Python (Sets)

Os conjuntos (set) em Python são coleções não ordenadas e não permitem elementos duplicados. Eles são úteis quando precisamos armazenar itens únicos e realizar operações matemáticas como união, interseção e diferença.'''

# 📝 1. Criando um Conjunto (set):
# 📌 Podemos criar conjuntos de duas formas:
# Criando um conjunto com elementos únicos
numeros = {1, 2, 3, 4, 5, 5, 5}  # Elementos duplicados são removidos automaticamente!
print(numeros)  # {1, 2, 3, 4, 5}

# Criando um conjunto usando set()
frutas = set(["maçã", "banana", "uva", "banana"])
print(frutas)  # {'maçã', 'uva', 'banana'}

# ✅ Dica: Conjuntos são representados com {}, mas um dicionário vazio é {}, enquanto um conjunto vazio deve ser criado com set().
conjunto_vazio = set()  # Correto
dicionario_vazio = {}   # Isso é um dicionário!




# ➕ 2. Adicionando Elementos (add):
# 📌 Para adicionar um único elemento ao conjunto, usamos .add():
numeros.add(6)
print(numeros)  # {1, 2, 3, 4, 5, 6}




# ➕ 3. Adicionando Múltiplos Elementos (update):
# 📌 Para adicionar vários elementos de uma vez, usamos .update():
numeros.update([7, 8, 9])
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}




# ❌ 4. Removendo Elementos (remove, discard, pop):
# 📌 Podemos remover elementos de diferentes formas:
numeros.remove(4)  # Remove o número 4 (se não existir, dá erro)
print(numeros)  # {1, 2, 3, 5, 6, 7, 8, 9}

numeros.discard(10)  # Não dá erro se o número não existir

removido = numeros.pop()  # Remove e retorna um elemento aleatório
print(removido)




# 🔄 5. Operações com Conjuntos:
# 🔹 União (union ou |) → Junta os elementos dos conjuntos, sem repetir duplicados.
A = {1, 2, 3}
B = {3, 4, 5}

uniao = A.union(B)
print(uniao)  # {1, 2, 3, 4, 5}

# Outra forma:
print(A | B)  # {1, 2, 3, 4, 5}

# 🔹 Interseção (intersection ou &) → Retorna apenas os elementos comuns.
intersecao = A.intersection(B)
print(intersecao)  # {3}

# Outra forma:
print(A & B)  # {3}

# 🔹 Diferença (difference ou -) → Retorna os elementos que estão no primeiro conjunto, mas não no segundo.
diferenca = A.difference(B)
print(diferenca)  # {1, 2}

# Outra forma:
print(A - B)  # {1, 2}

# 🔹 Diferença Simétrica (symmetric_difference ou ^) → Retorna os elementos que não estão em ambos.
dif_simetrica = A.symmetric_difference(B)
print(dif_simetrica)  # {1, 2, 4, 5}

# Outra forma:
print(A ^ B)  # {1, 2, 4, 5}




# 🔄 6. Iterando sobre um Conjunto:
# 📌 Podemos percorrer um conjunto com um loop for, igual às listas:
for fruta in frutas:
    print(fruta)
# maçã
# uva
# banana




# 🏆 7. Verificando Elementos (in):
# 📌 Podemos checar se um item está no conjunto:
print("banana" in frutas)  # True
print(10 in numeros)  # False




# 🔍 8. Convertendo Conjuntos:
# 📌 Podemos transformar um conjunto em lista ou tupla para ordenar ou acessar índices:
numeros_lista = list(numeros)
print(numeros_lista)  # [1, 2, 3, 5, 6, 7, 8, 9]

numeros_tupla = tuple(numeros)
print(numeros_tupla)  # (1, 2, 3, 5, 6, 7, 8, 9)
# ✅ Dica: Como conjuntos não possuem ordem, ao converter para lista, os elementos podem aparecer em qualquer posição.


