'''
📌 raise e assert (Raising and Asserting Exceptions) em Python

Em Python, usamos raise para lançar exceções manualmente e assert para criar verificações que garantem que certas condições sejam atendidas durante a execução do código.
'''

# 📌 1. Lançando Exceções com raise:
# O comando raise nos permite forçar um erro intencionalmente, interrompendo a execução do programa e exibindo uma mensagem personalizada.

# 🔹 Sintaxe básica do raise
class TipoDeErro(Exception):
    pass
raise TipoDeErro("Mensagem de erro personalizada")
'''
	•	TipoDeErro: Deve ser uma classe de exceção válida, como ValueError, TypeError, KeyError, etc.
	•	Mensagem de erro: Texto explicativo sobre o erro.
'''




# 📌 2. Exemplo Simples de raise:
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Erro: O denominador não pode ser zero!")  
    return a / b

try:
    resultado = dividir(10, 0)
    print(resultado)
except ZeroDivisionError as erro:
    print(erro)
'''
✅ Explicação:
	•	Se b for 0, o código levanta um erro com raise.
	•	O try-except captura o erro e exibe a mensagem.
'''




# 📌 3. Criando Exceções Personalizadas com raise:
# Podemos definir nossas próprias classes de exceção herdando de Exception.

# 🔹 Exemplo: Criando e lançando uma exceção personalizada
class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, valor):
        super().__init__(f"Erro: Saldo insuficiente! Saldo disponível: R$ {saldo}, Tentativa de saque: R$ {valor}")

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError(saldo, valor)
    return saldo - valor

try:
    novo_saldo = sacar(100, 200)
    print(f"Novo saldo: R$ {novo_saldo}")
except SaldoInsuficienteError as erro:
    print(erro)
'''
✅ Explicação:
	•	Criamos a classe SaldoInsuficienteError.
	•	Se o valor do saque for maior que o saldo, lançamos essa exceção personalizada.
	•	O try-except captura e exibe a mensagem de erro.
'''




# 📌 4. O Que é assert?:
# O assert é usado para garantir que uma condição seja verdadeira durante a execução do programa. Se a condição for falsa, ele lança automaticamente um AssertionError.

# 🔹 Sintaxe básica do assert
assert condição, "Mensagem de erro opcional"
'''
	•	condição: Expressão que deve ser verdadeira.
	•	Mensagem de erro: Opcional, mas útil para identificar o problema.
'''




# 📌 5. Exemplo Simples de assert:
def dividir(a, b):
    assert b != 0, "Erro: O denominador não pode ser zero!"
    return a / b

print(dividir(10, 2))  # OK
print(dividir(10, 0))  # Gera AssertionError
'''
✅ Explicação:
	•	O assert verifica se b não é zero.
	•	Se b == 0, um AssertionError é gerado com a mensagem personalizada.
'''




# 📌 6. Exemplo Completo com raise e assert:
def cadastrar_usuario(nome, idade):
    assert isinstance(nome, str), "Erro: O nome deve ser uma string!"  
    assert isinstance(idade, int), "Erro: A idade deve ser um número inteiro!"
    
    if idade < 18:
        raise ValueError("Erro: O usuário deve ter pelo menos 18 anos.")

    print(f"Usuário {nome} cadastrado com sucesso!")

try:
    cadastrar_usuario("João", "21")  # Vai gerar AssertionError
except Exception as erro:
    print(erro)

try:
    cadastrar_usuario("Ana", 16)  # Vai gerar ValueError
except Exception as erro:
    print(erro)
'''
✅ Explicação:
	•	assert verifica se os tipos são corretos.
	•	raise impede o cadastro de menores de idade.
	•	Se houver erro, o try-except captura e exibe a mensagem.
'''