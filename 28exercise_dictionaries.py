# Faça um programa que o usuário possa cadastrar quantas pessoas quiser;
# Armazene nome, idade e altura.


users = []

while True:
        try:
            user = {'nome': input('Digite um nome: \n'), 'idade': int(input('Digite uma idade: \n')), 'altura': int(input('Digite uma altura: \n'))}
            users.append(user)
        except:
             (print('Digite informações válidas.'))
        if input('Deseja adicionar mais alguém? Digite(S/N): \n') == 'S':
            continue
        else:
            break
print(users)

