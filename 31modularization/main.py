# Importar as funções de outro arquivo para executar no main.py é a modularização:
from calculator import * 

print(soma(10, 5))        # 15
print(subtracao(10, 5))   # 5
print(multiplicacao(10, 5)) # 50
print(divisao(10, 0))     # Erro: divisão por zero!