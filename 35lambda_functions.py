'''
📌 O que são funções lambda?

Funções lambda são funções anônimas em Python, ou seja, funções sem um nome definido, usadas para operações curtas e rápidas. Elas são úteis quando precisamos de funções pequenas sem a necessidade de def.
'''

# 🔹 1. Sintaxe Básica:
# Função normal
def somar(a, b):
    return a + b

# Função lambda equivalente
somar_lambda = lambda a, b: a + b

print(somar(3, 5))        # Saída: 8
print(somar_lambda(3, 5)) # Saída: 8




# 🔹 2. Usando Lambda com map():
# O map() aplica uma função a todos os elementos de um iterável.
numeros = [1, 2, 3, 4, 5]
dobrados = list(map(lambda x: x * 2, numeros))

print(dobrados)  # Saída: [2, 4, 6, 8, 10]




# 🔹 3. Usando Lambda com filter():
# O filter() filtra elementos de um iterável que atendem a uma condição.
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)  # Saída: [2, 4, 6]




# 🔹 4. Usando Lambda com sorted():
# Podemos personalizar a ordenação com key.
nomes = ["Lucas", "Ana", "Matheus", "Bruna"]
ordenado = sorted(nomes, key=lambda nome: len(nome))  

print(ordenado)  # Saída: ['Ana', 'Lucas', 'Bruna', 'Matheus']




# 🔹 5. Lambda Dentro de Funções:
def multiplicador(n):
    return lambda x: x * n  # Retorna uma função lambda

dobro = multiplicador(2)
triplo = multiplicador(3)

print(dobro(5))  # Saída: 10
print(triplo(5)) # Saída: 15

'''
✅ Quando Usar Lambda?

✔ Quando a função for pequena e rápida.
✔ Quando for usada como argumento de funções (map, filter, sorted).
✔ Quando for descartável e não precisar de um nome.

💡 Evite lambdas muito complexas! Se a lógica for difícil de entender, prefira def.
'''






# Exemplos para o post de quarta 05/03/25:
'''
O lambda pode parecer meio desnecessário à primeira vista, mas ele resolve um problema bem específico: quando você precisa de uma função para algo pontual, mas o método ou função que você está usando exige um “caminho” para personalizar o comportamento.
'''

# 🔥 1. Por que não usar só .sort()?
# O método .sort() funciona normalmente sem lambda, porque ele ordena os elementos no modo padrão (do menor para o maior).

#Exemplo sem lambda (funciona sem problemas)
numeros = [3, 1, 5, 2, 4]
numeros.sort()  
print(numeros)  # Saída: [1, 2, 3, 4, 5]
# ✅ Aqui não precisa de lambda, porque ele já sabe como ordenar números!




# 🔥 2. Mas e se eu quiser ordenar de um jeito diferente?
# O problema surge quando queremos ordenar por um critério específico.
# Por exemplo, vamos supor que temos uma lista de nomes e queremos ordenar pelo tamanho da palavra, e não em ordem alfabética.

# Tentando usar .sort() sozinho:
nomes = ["Carlos", "Ana", "Matheus", "Pri"]
nomes.sort()  

print(nomes)  
# Saída: ['Ana', 'Carlos', 'Matheus', 'Pri']  
# (Ele ordenou alfabeticamente, mas eu queria por tamanho!)

# 🚨 Aqui .sort() sozinho não resolve, porque ele não sabe que queremos ordenar pelo tamanho da palavra.
# Agora que precisamos definir uma regra de ordenação personalizada, entra o lambda!

# Com lambda, passamos um critério personalizado:
nomes = ["Carlos", "Ana", "Matheus", "Pri"]
nomes.sort(key=lambda nome: len(nome))  

print(nomes)  
# Saída: ['Ana', 'Pri', 'Carlos', 'Matheus']
# Agora sim, ordenamos por tamanho da palavra!
# ✅ Aqui o lambda faz sentido porque .sort() sozinho não conseguiria fazer isso!




# 🔥 3. Mas eu poderia usar um def, né?
# Sim! Se você achar o lambda confuso, pode usar um def, e o resultado será o mesmo:
def tamanho_palavra(nome):
    return len(nome)

nomes.sort(key=tamanho_palavra)

print(nomes)  
# Saída: ['Ana', 'Pri', 'Carlos', 'Matheus']
'''
✅ Aqui o código fica mais legível, mas você cria uma função que talvez só use uma vez.

Se for algo pequeno e rápido, lambda evita precisar nomear a função.
Se for algo maior, def deixa o código mais organizado.
'''




# 🔥 4. Outro exemplo: filter() e map() exigem uma função!
# O lambda também brilha em funções como filter() e map(), porque elas exigem que passemos uma função como argumento.
# Por exemplo, queremos filtrar apenas os números pares de uma lista:

# Com lambda (rápido e direto):
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)  # Saída: [2, 4, 6]

# Com def (mais legível, mas mais longo):
def eh_par(x):
    return x % 2 == 0

pares = list(filter(eh_par, numeros))

print(pares)  # Saída: [2, 4, 6]
'''
✅ Se a função for simples e usada só uma vez, lambda pode ser útil.
✅ Se for mais complexa ou reutilizável, prefira def.
'''