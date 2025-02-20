# Os operadores relacionais (ou comparação) são usados para comparar valores e retornam um valor booleano (True ou False).

# 1️⃣ Verificando Idade:
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade! ✅")
else:
    print("Você é menor de idade! ❌")
# 💡 Explicação: idade >= 18 verifica se a pessoa tem 18 anos ou mais.



# 2️⃣ Comparando Dois Números:
num1 = 10
num2 = 20

print(num1 < num2)   # True
print(num1 > num2)   # False
print(num1 == num2)  # False
print(num1 != num2)  # True
#💡 Explicação:
# 10 < 20 → Verdadeiro (True)
# 10 > 20 → Falso (False)
 


# 3️⃣ Verificando Notas e Aprovação:
nota = float(input("Digite sua nota: "))

if nota >= 7.0:
    print("Aprovado! 🎉")
elif nota >= 5.0:
    print("Recuperação! 🟡")
else:
    print("Reprovado! ❌")
# 💡 Explicação:
# Se a nota for 7 ou mais → Aprovado ✅
# Se for entre 5 e 6.9 → Recuperação 🟡
# Se for menor que 5 → Reprovado ❌



#4️⃣ Verificando Senha Correta:
senha_correta = "python123"
senha_digitada = input("Digite sua senha: ")

if senha_digitada == senha_correta:
    print("Acesso permitido! ✅")
else:
    print("Senha incorreta! ❌")
# 💡 Explicação: == compara se a senha digitada é exatamente igual à correta.



# 5️⃣ Verificando se um Número Está Dentro de um Intervalo:
numero = int(input("Digite um número entre 1 e 100: "))

if numero >= 1 and numero <= 100:
    print("Número dentro do intervalo! ✅")
else:
    print("Fora do intervalo! ❌")
# 💡 Explicação: O número precisa ser maior ou igual a 1 e menor ou igual a 100.