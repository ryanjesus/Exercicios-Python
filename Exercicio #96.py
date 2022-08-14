
"""
Faça um programa que tenha uma função chamada área(), que 
receba as dimesões de um terreno retangular(largura e comprimento) e 
mostre a área do terreno
"""

def area(a, b):
    s = a * b
    print(f'A área de um terreno {a}x{b} é de {s}m².')


print('Controle de Terrenos:^8')
print('-'*30)

a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
area(a, b)

