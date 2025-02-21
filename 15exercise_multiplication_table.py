# Receba um número inteiro do usuário e mostre a tabuada desse número:

number = int(input("Digite um número inteiro: \n"))
table = 1

while table < 11:
    multiplication = number * table
    print(f'{number}x{table}= {multiplication}')
    table += 1