'''
1. Dobrar os números pares:
Receba uma lista de números inteiros e crie uma nova lista contendo o dobro de cada número par da lista original.

Exemplo de entrada: [1, 2, 3, 4, 5, 6]
Exemplo de saída: [4, 8, 12]
'''

#numeros = [1, 2, 3, 4, 5, 6]
#dobro = [num * 2 for num in numeros if num % 2 == 0]
#print(dobro)




'''
2.	Converter nomes para maiúsculas
Receba uma lista de nomes (strings) e crie uma nova lista contendo apenas os nomes que tenham mais de 5 letras, todos em maiúsculas.

Exemplo de entrada: ["Ana", "Gabriel", "Lucas", "João", "Fernanda"]
Exemplo de saída: ["GABRIEL", "FERNANDA"]
'''

#nomes = ["Ana", "Gabriel", "Lucas", "João", "Fernanda"]

#maisculo = [nome.upper() for nome in nomes if len(nome) > 5]

#print(maisculo)




'''
3. Números Divisíveis por 3 e 5

Escreva um programa que gere uma lista contendo todos os números entre 100 e 500 que sejam divisíveis tanto por 3 quanto por 5.

Utilize List Comprehension para criar essa lista e exiba o resultado na tela.
'''

div = [i for i in range(100, 500) if i % 3 == 0 and i % 5 == 0]
print(div)

#div = []  

#for i in range(100, 500):  
    #if i % 3 == 0 and i % 5 == 0:
       #div.append(i)
#print(div)





'''
4. Filtrando Palavras com Vogais Duplicadas

Dada a seguinte lista de palavras:
palavras = ["cooperar", "saída", "coordenação", "livro", "teste", "abacaxi", "oportunidade", "reunião"]

Crie uma nova lista contendo apenas as palavras que possuem pelo menos uma vogal duplicada consecutiva (por exemplo, “cooperar” e “coordenação” devem ser incluídas na nova lista).

Você deve utilizar List Comprehension para resolver esse problema. Considere apenas as vogais (a, e, i, o, u) e desconsidere acentos.
'''

palavras = ["cooperar", "saída", "coordenação", "livro", "teste", "abacaxi", "oportunidade", "reunião"]

vogais = "aeiou"
resultado = []  # Lista para armazenar palavras com vogais duplicadas consecutivas

for palavra in palavras:
    palavra_sem_acentos = palavra.lower().replace("á", "a").replace("í", "i").replace("ó", "o").replace("é", "e").replace("ú", "u")  # Remove acentos
    for i in range(len(palavra_sem_acentos) - 1):
        if palavra_sem_acentos[i] in vogais and palavra_sem_acentos[i] == palavra_sem_acentos[i + 1]:
            resultado.append(palavra)
            break  # Para de verificar essa palavra, pois já sabemos que ela atende ao critério

print(resultado)  # Deve exibir ['cooperar', 'coordenação']

# list comprehension:
palavras = ["cooperar", "saída", "coordenação", "livro", "teste", "abacaxi", "oportunidade", "reunião"]
vogais = "aeiou"

resultado = [
    palavra for palavra in palavras 
    if any(
        palavra.lower().replace("á", "a").replace("í", "i").replace("ó", "o").replace("é", "e").replace("ú", "u")[i] in vogais and 
        palavra.lower().replace("á", "a").replace("í", "i").replace("ó", "o").replace("é", "e").replace("ú", "u")[i] == palavra.lower().replace("á", "a").replace("í", "i").replace("ó", "o").replace("é", "e").replace("ú", "u")[i + 1]
        for i in range(len(palavra) - 1)
    )
]

print(resultado)  # Deve exibir ['cooperar', 'coordenação']