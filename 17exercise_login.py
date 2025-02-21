# Defina um usuário e senha e depois verifique 
# se login e senha do usuário são válidos:

usuario = 'romenix'
senha = 'Romulo@1999'

while True:
    user = input('Digite o seu usuário: \n')
    password = input('Digite a sua senha: \n')
    if usuario == user and password == senha:
        print(f'{usuario} logado com sucesso.')
        break
    elif usuario == user and password != senha:
        print(f'A senha digitada está incorreta.')
        continue
    else:
        print(f'Usuário não encontrado nos registros.')
        continue


