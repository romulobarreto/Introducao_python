'''📌 Dicionários em Python (Dictionaries)

Os dicionários (dict) são estruturas de dados que armazenam pares de chave-valor. Diferente das listas, onde os elementos são acessados por índices numéricos, os dicionários usam chaves únicas para armazenar e recuperar valores rapidamente.'''

# 📝 1. Criando um Dicionário (dict)
# 📌 Podemos criar um dicionário de várias formas:
# Criando um dicionário com chaves e valores
pessoa = {
    "nome": "Carlos",
    "idade": 30,
    "cidade": "São Paulo"
}

# Outra forma de criar um dicionário
carro = dict(marca="Toyota", modelo="Corolla", ano=2022)

print(pessoa)  # {'nome': 'Carlos', 'idade': 30, 'cidade': 'São Paulo'}
print(carro)   # {'marca': 'Toyota', 'modelo': 'Corolla', 'ano': 2022}




# 🔍 2. Acessando Valores no Dicionário:
# 📌 Podemos acessar valores usando a chave correspondente:
print(pessoa["nome"])  # Carlos
print(carro.get("modelo"))  # Corolla

# ✅ Dica: get() é mais seguro, pois evita erro caso a chave não exista.
print(carro.get("cor"))  # Retorna None (não gera erro)




# ✏️ 3. Adicionando e Atualizando Valores (update):
# 📌 Podemos adicionar novas chaves ou atualizar valores existentes:
pessoa["profissao"] = "Engenheiro"  # Adicionando uma nova chave
pessoa["idade"] = 31  # Atualizando a idade

print(pessoa)
# {'nome': 'Carlos', 'idade': 31, 'cidade': 'São Paulo', 'profissao': 'Engenheiro'}

# 📌 Também podemos usar .update() para adicionar ou modificar múltiplos valores ao mesmo tempo:
pessoa.update({"idade": 32, "cidade": "Rio de Janeiro"})
print(pessoa)
# {'nome': 'Carlos', 'idade': 32, 'cidade': 'Rio de Janeiro', 'profissao': 'Engenheiro'}




# 🔄 4. Iterando sobre um Dicionário:
# 📌 Podemos percorrer um dicionário de diferentes maneiras:
# 🔹 Iterando pelas chaves (keys())
for chave in pessoa.keys():
    print(chave)  
# nome
# idade
# cidade
# profissao

# 🔹 Iterando pelos valores (values())
for valor in pessoa.values():
    print(valor)  
# Carlos
# 32
# Rio de Janeiro
# Engenheiro

# 🔹 Iterando pelas chaves e valores (items())
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
# nome: Carlos
# idade: 32
# cidade: Rio de Janeiro
# profissao: Engenheiro




# ❌ 5. Removendo Elementos do Dicionário:
# 📌 Podemos remover elementos usando pop(), del, ou clear():
pessoa.pop("idade")  # Remove e retorna o valor da chave "idade"
print(pessoa)
# {'nome': 'Carlos', 'cidade': 'Rio de Janeiro', 'profissao': 'Engenheiro'}

del pessoa["cidade"]  # Remove a chave "cidade"
print(pessoa)
# {'nome': 'Carlos', 'profissao': 'Engenheiro'}

pessoa.clear()  # Remove todos os elementos do dicionário
print(pessoa)  # {}




# 📌 6. Dicionários Aninhados (Nested Dictionaries):
# 📌 Podemos ter dicionários dentro de dicionários!
empresa = {
    "CEO": {"nome": "Ana", "idade": 40},
    "Gerente": {"nome": "Bruno", "idade": 35},
    "Funcionários": ["Carlos", "Maria", "João"]
}

print(empresa["CEO"]["nome"])  # Ana
print(empresa["Funcionários"][1])  # Maria