# Receba uma temperatura em fareheith e exiba em graus celsius:

def conversor():
    farenheith = float(input('Digite a temperatura atual em farenheith: \n'))
    celsius = 5/9 *(farenheith - 32)
    return celsius

celsius = conversor()
print(f'Agora está {celsius:.1f}°.')