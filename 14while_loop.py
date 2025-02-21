#🔹 Exemplo 1: while Simples
#✅ Descrição: Um loop while que conta até 5.
contador = 1

while contador <= 5:
    print(f"Contando: {contador}")
    contador += 1  # Incrementa o contador

print("Fim do loop!")
'''📝 O que acontece?
	•	O loop continua rodando enquanto contador for menor ou igual a 5.
	•	Quando contador chega a 6, a condição while contador <= 5 se torna False, e o loop para.'''




# 🔹 Exemplo 2: Usando break para Sair do Loop
#✅ Descrição: O loop para imediatamente se o usuário digitar "sair".
while True:
    comando = input("Digite algo (ou 'sair' para encerrar): ")
    
    if comando.lower() == "sair":
        print("Saindo do loop...")
        break  # Sai do loop imediatamente
    
    print(f"Você digitou: {comando}")

print("Loop encerrado!")
'''📝 O que acontece?
	•	O loop é infinito (while True), mas para quando o usuário digita "sair", pois o break interrompe a repetição.
	•	Sem o break, o loop rodaria para sempre.'''




#🔹 Exemplo 3: Usando continue para Pular uma Iteração
#✅ Descrição: Pula os números pares e exibe apenas os ímpares.
numero = 0

while numero < 10:
    numero += 1
    
    if numero % 2 == 0:
        continue  # Pula para a próxima repetição do loop
    
    print(f"Número ímpar: {numero}")
'''📝 O que acontece?
	•	O continue faz com que o loop ignore os números pares e continue para a próxima iteração.
	•	Quando numero é par, o print() nunca é executado.'''




#🔹 Exemplo 4: Simulação de Login com Tentativas Limitadas
#✅ Descrição: O usuário tem 3 tentativas para digitar a senha correta.
senha_correta = "1234"
tentativas = 0

while tentativas < 3:
    senha = input("Digite a senha: ")
    
    if senha == senha_correta:
        print("Acesso permitido!")
        break  # Sai do loop se a senha estiver correta
    else:
        print("Senha incorreta. Tente novamente.")
    
    tentativas += 1

if tentativas == 3:
    print("Número máximo de tentativas atingido. Acesso bloqueado!")
'''📝 O que acontece?
	•	O usuário tem 3 chances de acertar a senha.
	•	Se acertar, o break interrompe o loop.
	•	Se errar 3 vezes, o acesso é bloqueado.'''