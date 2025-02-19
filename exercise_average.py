# Escreva um programa onde o usuário digite duas notas e ele mostre a média das notas

def calculo_media():
    nota_1 = float(input('Digite a primeira nota aqui, se houver decimal, use (.). \n'))
    nota_2 = float(input('Digite a segunda nota aqui, se houver decimal, use (.). \n'))
    
    resultado = (nota_1 + nota_2) / 2 
    print(f'A média das notas é: {resultado:.2f}')  

calculo_media()
