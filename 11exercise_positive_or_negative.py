# Receba um número e exiba se ele é positivo ou negativo:

def categoria_numero():
    number = float(input("Digite um número positivo ou negativo: \n"))
    if number >0:
        categoria = "POSITIVO"
    elif number == 0:
        categoria = "ZERO"
    else:
        categoria = "NEGATIVO"
    return number, categoria

number, categoria = categoria_numero()
print(f'O número digitado foi {number:.1f}.')
print(f'Ele é {categoria}.')