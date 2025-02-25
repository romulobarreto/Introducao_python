# Mostra a tabuada completa de todos os números do 1 ao 10:

for i in range(1, 11):
    print(f'=====[TABUADA DO {i}]=====')
    for j in range(1, 11):
        multiplication = i * j
        print(f'{j}x{i} = {multiplication}')
        