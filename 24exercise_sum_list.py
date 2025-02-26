# Receba 10 valores e exiba a soma de todos eles:

x = []

while len(x) <= 10:
    try:
        x.append(float(input('Digite um número para a lista x: \n')))
    except:
        print('Digite um número válido.')

soma = sum(x)
print(f'A lista final é: {x}. O resultado da soma é: {soma:.1f}.')
