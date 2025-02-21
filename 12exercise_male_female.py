# Receba F para feminino e M para masculino e exiba o sexo da pessoa:

def genero():
    gen = input("Digite a sigla do seu gênero. (F ou M): \n")
    if gen == "F" or gen == "f":
        gen = "FEMININO"
    elif gen == "M" or gen == "m":
        gen = "MASCULINO"
    else:
        gen = "VALOR INVÁLIDO"
    return gen

gen = genero()
print(f'Seu gênero é: {gen}.')