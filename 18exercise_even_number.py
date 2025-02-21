# Receba um número e mostre todos os números pares de 0 até ele mesmo:

while True:
    try:
        number = int(input('Digite um número inteiro: \n'))
        break
    except:
        print('Digite um valor inteiro válido.')

contagem = 0

while contagem <= number:
    if contagem % 2 == 0:
        print(contagem)
    contagem += 1
    