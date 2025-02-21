# Receba 3 números inteiros e exiba o maior deles:

def maior_numero():
    num1 = int(input("Digite o primeiro número inteiro aqui. \n")) 
    num2 = int(input("Digite o segundo número inteiro aqui. \n")) 
    num3 = int(input("Digite o terceiro número inteiro aqui. \n")) 
    nums = (num1, num2, num3)
    return max(nums)

nums = maior_numero()
print(f'O maior número é o {nums}.')