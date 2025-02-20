'''
Em Python, podemos converter valores de um tipo para outro usando conversões explícitas. Aqui estão os principais métodos:

int() → Converte para número inteiro (descarta decimais).
float() → Converte para número decimal (float).
str() → Converte para string (texto).
bool() → Converte para True ou False.
'''

# 1️⃣ Convertendo um número inteiro para string (int → str)
idade = 25  # Tipo: int
idade_str = str(idade)  # Agora é uma string

print(idade_str)  # '25'
print(type(idade_str))  # <class 'str'>
# Usado quando queremos exibir números em mensagens formatadas.



# 2️⃣ Convertendo um número decimal para inteiro (float → int)
altura = 1.71  # Tipo: float
altura_int = int(altura)  # Converte para int (corta a parte decimal)

print(altura_int)  # 1
print(type(altura_int))  # <class 'int'>
# ⚠️ Cuidado: O int() simplesmente remove a parte decimal, sem arredondar!

# Se precisar arredondar corretamente:
import math
altura_arredondada = round(altura)  # Arredonda corretamente
print(altura_arredondada)  # 2



# 3️⃣ Convertendo um número inteiro para decimal (int → float)
idade1 = 22  # Tipo: int
idade_float = float(idade1)  # Agora é float

print(idade_float)  # 22.0
print(type(idade_float))  # <class 'float'>
# Útil quando precisamos de operações que exigem valores decimais.



# 4️⃣ Convertendo texto para número (str → int ou str → float)
salario = "3000"  # Tipo: str
salario_int = int(salario)  # Converte para inteiro
salario_float = float(salario)  # Converte para float

print(salario_int)  # 3000
print(type(salario_int))  # <class 'int'>

print(salario_float)  # 3000.0
print(type(salario_float))  # <class 'float'>
# ⚠️ Se o texto contiver caracteres inválidos ("3000 reais"), a conversão falha!



# 5️⃣ Convertendo valores para booleano (bool())
print(bool(0))  # False
print(bool(1))  # True
print(bool(""))  # False (string vazia)
print(bool("Python"))  # True (qualquer string não vazia é True)
# Útil em verificações condicionais.
