# Os operadores lógicos são usados para combinar expressões booleanas (True ou False). Eles são muito usados em estruturas condicionais e filtros.

# 1️⃣ Verificando se um Usuário Pode Acessar um Sistema:
usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "1234":
    print("Acesso permitido! ✅")
else:
    print("Acesso negado! ❌")
# 💡 Explicação:
# O usuário só pode acessar se usuario for "admin" e senha for "1234".
# Se qualquer um estiver errado, o acesso é negado.



# 2️⃣ Verificando Se Um Número Está Dentro de um Intervalo:
numero = int(input("Digite um número entre 1 e 100: "))

if numero >= 1 and numero <= 100:
    print("Número dentro do intervalo! ✅")
else:
    print("Número fora do intervalo! ❌")
# 💡 Explicação: O número precisa ser maior ou igual a 1 e menor ou igual a 100 para ser aceito.



# 3️⃣ Verificando Aprovação de um Aluno:
nota = float(input("Digite sua nota: "))
frequencia = int(input("Digite sua frequência (%): "))

if nota >= 7 and frequencia >= 75:
    print("Aprovado! 🎉")
else:
    print("Reprovado! ❌")
# 💡 Explicação:
# O aluno só é aprovado se a nota for 7 ou mais e a frequência for 75% ou mais.



# 4️⃣ Verificando se um Usuário Pode Comprar um Produto:
saldo = float(input("Digite seu saldo: "))
preco = float(input("Digite o preço do produto: "))
cupom = input("Você tem cupom de desconto? (s/n): ")

if saldo >= preco or cupom.lower() == "s":
    print("Compra autorizada! ✅")
else:
    print("Saldo insuficiente e sem cupom! ❌")
# 💡 Explicação:
# A compra é autorizada se o saldo for suficiente ou se o usuário tiver um cupom de desconto.



# 5️⃣ Negação com not:
tem_ingresso = False

if not tem_ingresso:
    print("Você precisa comprar um ingresso! 🎟️")
else:
    print("Entrada liberada! ✅")
# 💡 Explicação: O not inverte o valor lógico. Se tem_ingresso for False, a mensagem será "Você precisa comprar um ingresso!".
