'''
1. Exercício de lambda

📌 Criação de uma Função Anônima para Calcular o Dobro
Crie uma função anônima (lambda) que receba um número inteiro e retorne o seu dobro.

Em seguida, utilize essa função para calcular o dobro dos seguintes números: 3, 7, 10 e 15, imprimindo os resultados na tela.
'''
dobraveis = [3, 7, 10, 15]

dobro = lambda x: x * 2

dobros = [dobro(i) for i in dobraveis]  

print(dobros) 



'''
2. Exercício de filter

📌 Filtrando Números Ímpares de uma Lista
Dada a seguinte lista de números:

Utilize a função filter() para criar uma nova lista contendo apenas os números ímpares dessa lista original.

Imprima a nova lista ao final.
'''
numeros = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]

impares = list(filter(lambda x : x % 2 != 0, numeros))

print(impares)


'''
3. Exercício de map

📌 Convertendo Temperaturas de Celsius para Fahrenheit
Dada a lista de temperaturas em graus Celsius:
Utilize a função map() para converter todas as temperaturas para Fahrenheit usando a fórmula:


F = C \times \frac{9}{5} + 32


Crie uma nova lista com as temperaturas convertidas e imprima o resultado.
'''
temperaturas_celsius = [0, 10, 20, 30, 40, 100]

fahrenheit = list(map(lambda x : (x * 9/5) + 32, temperaturas_celsius))
print(fahrenheit)