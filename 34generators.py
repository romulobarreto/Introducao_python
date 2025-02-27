from pympler.asizeof import asizesof

'''
📌 Geradores (Generators) em Python

Os geradores (generators) são uma maneira eficiente de criar iteradores em Python sem armazenar todos os valores na memória. Eles são úteis para lidar com grandes quantidades de dados ou quando queremos gerar valores sob demanda.
'''

# 📌 1. Criando um Gerador Simples com yield:
def contar_ate(n):
    for i in range(1, n + 1):
        yield i  # Pausa aqui e retorna o valor

# Criando um gerador
contador = contar_ate(5)

# Iterando sobre o gerador
for numero in contador:
    print(numero)
'''
🔹 Saída:
1
2
3
4
5
✅ Explicação:
	•	A função contar_ate não retorna todos os valores de uma vez.
	•	Em cada yield, a execução pausa, armazenando o estado atual.
	•	Quando a próxima iteração ocorre, a execução continua de onde parou.
'''




# 📌 2. Comparação: Função Normal vs. Gerador:
#🔹 Função Normal (Usando return)
def quadrados_lista(n):
    return [x ** 2 for x in range(n)]  # Retorna uma lista completa

print(quadrados_lista(5))
'''
🔹 Saída: [0, 1, 4, 9, 16]
🚨 Problema: Se n for muito grande, isso ocupa muita memória.
'''

# 🔹 Gerador (Usando yield)
def quadrados_gerador(n):
    for x in range(n):
        yield x ** 2  # Retorna um valor por vez

# Criando o gerador
quadrados = quadrados_gerador(5)

# Consumindo os valores um por um
print(next(quadrados))  # 0
print(next(quadrados))  # 1
print(next(quadrados))  # 4
# ✅ Vantagem: Economiza memória, pois gera um valor por vez, sem criar uma lista inteira na memória.




# 📌 3. Gerador Infinito (Lazy Evaluation):
# Podemos criar um gerador infinito, útil para streams de dados, leitura de logs, etc.
def numeros_infinitos():
    n = 0
    while True:
        yield n
        n += 1

gerador = numeros_infinitos()

print(next(gerador))  # 0
print(next(gerador))  # 1
print(next(gerador))  # 2
# ⚠ Cuidado! Se usado em um for, ele nunca vai parar!




# 📌 4. yield from (Delegando Iteração):
# Podemos usar yield from para delegar a geração de valores para outro iterável.
def gerador_lista():
    yield from [1, 2, 3, 4, 5]  # Equivalente a fazer vários `yield`

for numero in gerador_lista():
    print(numero)
'''
🔹 Saída:
1
2
3
4
5
✅ Vantagem: Código mais limpo ao reutilizar iteráveis!
'''




# 📌 5. Convertendo Geradores para Listas:
# Se for necessário, podemos converter um gerador em uma lista:
def gerar_pares(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

pares = list(gerar_pares(10))
print(pares)  # [0, 2, 4, 6, 8]
# 🚀 Isso deve ser feito apenas se a lista for pequena, pois perde a eficiência dos geradores.




# 📌 6. Geradores com Expressões (Generator Expressions):
# Podemos criar geradores com uma sintaxe compacta, semelhante à list comprehension.
gerador = (x ** 2 for x in range(5))  # Parênteses em vez de colchetes!

print(next(gerador))  # 0
print(next(gerador))  # 1
print(next(gerador))  # 4
# ✅ Vantagem: Mais eficiente do que listas quando não precisamos armazenar todos os valores de uma vez.




# 📌 7. Comparando Memória: Lista vs. Gerador:
from pympler.asizeof import asizesof

# Criando uma lista com 1 milhão de números
lista = [x for x in range(1_000_000)]

# Criando um gerador com 1 milhão de números
gerador = (x for x in range(1_000_000))

# Medindo o tamanho em memória
memoria_lista, memoria_gerador = asizesof(lista, gerador)

print(f"Lista ocupa: {memoria_lista / 1024 ** 2:.2f} MB")
print(f"Gerador ocupa: {memoria_gerador / 1024 ** 2:.2f} MB")
'''
🔹 Saída esperada (pode variar):
Lista ocupa: 37.26 MB
Gerador ocupa: 0.00 MB
'''