# 🔹 1. Verificando o Endereço de Memória:
# O Python tem a função id() que permite ver o endereço de memória de um objeto.
x = 10
y = x

print(id(x))  # Exemplo: 140711882231216
print(id(y))  # Mesmo endereço que x
# ✅ Como y = x, ambos apontam para o mesmo endereço de memória.




# 🔹 2. Referência em Listas (Mutáveis):
# Os tipos mutáveis, como listas, dicionários e conjuntos, compartilham a referência ao mesmo objeto.
lista1 = [1, 2, 3]
lista2 = lista1  # lista2 agora aponta para o mesmo endereço de lista1

lista2.append(4)

print(lista1)  # [1, 2, 3, 4] -> lista1 também foi alterada!
print(lista2)  # [1, 2, 3, 4]
print(id(lista1) == id(lista2))  # True, pois ambas referenciam o mesmo objeto
# ✅ Como lista1 e lista2 compartilham a mesma referência, qualquer mudança em uma afeta a outra.




# 🔹 3. Evitando a Referência Compartilhada (Criando uma Cópia):
# Se quiser criar uma cópia independente de uma lista, use copy() ou [:].
lista1 = [1, 2, 3]
lista2 = lista1.copy()  # Agora lista2 é uma nova lista, independente de lista1

lista2.append(4)

print(lista1)  # [1, 2, 3] (não foi alterada)
print(lista2)  # [1, 2, 3, 4] (apenas lista2 mudou)
print(id(lista1) == id(lista2))  # False, agora são objetos diferentes

# Outra forma:
lista2 = lista1[:]  # Também cria uma cópia




# 🔹 4. Referência com Objetos Personalizados:
# O mesmo conceito se aplica a classes e objetos.
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

p1 = Pessoa("Ana")
p2 = p1  # p2 aponta para o mesmo objeto de p1

p2.nome = "Carlos"

print(p1.nome)  # "Carlos" (foi alterado em p1 também)
print(p2.nome)  # "Carlos"
print(id(p1) == id(p2))  # True, pois compartilham a referência




# 🔹 5. Criando Objetos Independentes:
# Para criar uma cópia independente de um objeto, usamos copy.deepcopy().
import copy

p1 = Pessoa("Ana")
p2 = copy.deepcopy(p1)  # Agora p2 é um novo objeto independente

p2.nome = "Carlos"

print(p1.nome)  # "Ana" (não foi alterado)
print(p2.nome)  # "Carlos"
print(id(p1) == id(p2))  # False, agora são objetos diferentes
