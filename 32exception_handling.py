'''📌 Tratamento de Exceções (Exception Handling) em Python

O tratamento de exceções é usado para lidar com erros inesperados durante a execução do programa. Em Python, usamos try, except, else e finally para capturar e tratar exceções sem interromper o fluxo do código.'''

# 📌 1. Capturando Exceções com try e except:
# Quando um erro ocorre, Python normalmente interrompe a execução e exibe uma mensagem de erro. Podemos evitar que o programa pare usando try e except:

#🔹 Exemplo: Lidando com erro de divisão por zero (ZeroDivisionError)
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero  # Pode gerar ZeroDivisionError
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")
'''
✅ Explicação:
	•	Se o usuário digitar 0, a divisão falharia, mas com except, exibimos uma mensagem amigável em vez de um erro no console.
'''




# 📌 2. Capturando Exceções Específicas: 
# Podemos capturar tipos específicos de exceções para tratar cada caso de forma diferente.

# 🔹 Exemplo: Capturando ValueError e ZeroDivisionError separadamente
try:
    numero = int(input("Digite um número: "))  # Pode gerar ValueError
    resultado = 10 / numero  # Pode gerar ZeroDivisionError
    print(f"Resultado: {resultado}")
except ValueError:
    print("Erro: Você precisa digitar um número inteiro.")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")
'''
✅ Explicação:
	•	Se o usuário digitar um texto em vez de número, ocorre um ValueError.
	•	Se o usuário digitar 0, ocorre um ZeroDivisionError.
	•	Cada erro é tratado separadamente.
'''




# 📌 3. Capturando Exceções Genéricas:
# Podemos capturar qualquer erro com um except genérico:
try:
    arquivo = open("arquivo_inexistente.txt", "r")  # Pode gerar FileNotFoundError
    conteudo = arquivo.read()
    print(conteudo)
except Exception as erro:  # Captura qualquer erro
    print(f"Ocorreu um erro: {erro}")
'''
✅ Explicação:
	•	Se o arquivo não existir, capturamos o erro e exibimos uma mensagem amigável.
	•	Exception é a classe base para todas as exceções em Python.
	•	erro recebe a descrição do erro gerado.

⚠ Atenção: Usar except Exception é útil para evitar que o programa quebre, mas pode mascarar erros importantes. Sempre que possível, capture exceções específicas.
'''




# 📌 4. Usando else no Tratamento de Exceções:
# O bloco else é executado se nenhuma exceção for levantada dentro do try.

# 🔹 Exemplo: Se não houver erro, executa else
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")
except ValueError:
    print("Erro: Você precisa digitar um número válido.")
else:
    print(f"Resultado: {resultado}")  # Executado apenas se não houver erro
'''
✅ Explicação:
	•	Se o usuário inserir um valor correto, o código no else será executado.
	•	Se houver erro, o else não será executado.
'''




# 📌 5. Usando finally para Executar Código Sempre:
# O bloco finally sempre será executado, independentemente de ocorrer erro ou não. Isso é útil para fechar arquivos, liberar recursos, fechar conexões com bancos de dados, etc.

# 🔹 Exemplo: Garantindo que um arquivo seja fechado
try:
    arquivo = open("meuarquivo.txt", "r")  # Pode gerar FileNotFoundError
    conteudo = arquivo.read()
    print(conteudo)
except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")
finally:
    print("Finalizando operação...")
'''
✅ Explicação:
	•	Se o arquivo for aberto com sucesso, ele será lido.
	•	Se o arquivo não existir, tratamos o erro com except.
	•	O finally será executado de qualquer jeito, útil para garantir que o código finalize corretamente.
'''




# 📌 6. Criando Exceções Personalizadas (raise):
# Podemos levantar (raise) exceções manualmente se uma condição específica for atendida.

# 🔹 Exemplo: Criando uma exceção personalizada
def dividir(a, b):
    if b == 0:
        raise ValueError("Erro: O denominador não pode ser zero.")  # Lançando uma exceção
    return a / b

try:
    resultado = dividir(10, 0)
    print(resultado)
except ValueError as erro:
    print(erro)
'''
✅ Explicação:
	•	A função dividir() verifica se b é zero e lança um ValueError.
	•	O try captura essa exceção e exibe uma mensagem personalizada.
'''




# 📌 7. Criando Exceções Personalizadas (class Exception):
# Podemos criar nossas próprias exceções para situações específicas.

# 🔹 Exemplo: Criando uma exceção SaldoInsuficienteError
class SaldoInsuficienteError(Exception):
    def __init__(self, mensagem="Erro: Saldo insuficiente para saque!"):
        super().__init__(mensagem)

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError()
    return saldo - valor

try:
    novo_saldo = sacar(100, 200)
    print(f"Novo saldo: R$ {novo_saldo}")
except SaldoInsuficienteError as erro:
    print(erro)
'''
✅ Explicação:
	•	Criamos a exceção SaldoInsuficienteError que herda de Exception.
	•	Se o saque for maior que o saldo, a exceção será lançada.
	•	O try captura a exceção e exibe a mensagem personalizada.
'''