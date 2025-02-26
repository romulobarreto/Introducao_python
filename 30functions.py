# 📌 1. Criando uma Função Simples:
def saudacao():
    print("Olá, seja bem-vindo!")

saudacao()
#✅ Explicação: Criamos uma função saudacao() que exibe uma mensagem quando chamada.



# 📌 2. Função com Parâmetros:
def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo!")

saudacao("Rômulo")
saudacao("Maria")
# ✅ Explicação: A função recebe um parâmetro nome, permitindo personalizar a saudação.




# 📌 3. Função com Retorno de Valor:
def soma(a, b):
    return a + b  # Retorna o resultado da soma

resultado = soma(5, 3)
print(f"O resultado da soma é {resultado}")
# ✅ Explicação: A função soma() retorna um valor, que pode ser armazenado em uma variável e utilizado depois.




# 📌 4. Parâmetros Opcionais com Valores Padrão:
def apresentar(nome, idade=18):
    print(f"Nome: {nome}, Idade: {idade}")

apresentar("João", 25)
apresentar("Ana")  # Usa o valor padrão 18
# ✅ Explicação: Se o usuário não informar a idade, o valor padrão será 18.



# 📌 5. *args – Múltiplos Argumentos Posicionais:
def soma(*args):
    return sum(args)

print(soma(1, 2, 3))  # 6
print(soma(10, 20, 30, 40))  # 100
# ✅ Explicação: *args permite receber múltiplos valores e tratá-los como uma tupla dentro da função.




# 📌 6. **kwargs – Argumentos Nomeados Variáveis:
def exibir_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

exibir_info(nome="Carlos", idade=30, cidade="São Paulo")
# ✅ Explicação: **kwargs recebe argumentos nomeados e os armazena em um dicionário.

# 📌 Exemplo Prático – Criando um Perfil de Usuário
def criar_perfil(nome, **informacoes):
    print(f"Perfil de {nome}:")
    for chave, valor in informacoes.items():
        print(f"- {chave}: {valor}")

criar_perfil("Alice", idade=30, cidade="Rio de Janeiro", profissão="Engenheira")

# Saída:
'''Perfil de Alice:  
- idade: 30  
- cidade: Rio de Janeiro  
- profissão: Engenheira  
'''



# 📌 7. Função Retornando Múltiplos Valores:
def operacoes(a, b):
    soma = a + b
    subtracao = a - b
    return soma, subtracao  # Retorna uma tupla

resultado_soma, resultado_subtracao = operacoes(10, 5)
print(f"Soma: {resultado_soma}, Subtração: {resultado_subtracao}")
# ✅ Explicação: Podemos retornar múltiplos valores de uma função, e depois desempacotá-los.