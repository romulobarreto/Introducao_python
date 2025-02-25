# Receba um número e mostre a tabuada completa dele usando o laço for.

while True:
    try:
        number = int(input("Digite um número inteiro: \n"))
        break
    except:
        print(f'Erro, digite novamente.')

for i in range(0, 11):
    multiplication = i * number
    print(f'{number}x{i} = {multiplication}')