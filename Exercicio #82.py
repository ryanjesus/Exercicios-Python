"""
Crie um programa que vai ler vários números e colocar em uma lista

Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores
impares digitados, respectivamente.

Ao final, mostre os conteúdo das três lista geradas
"""
n = 0
one = []
three = []
two = []
opcao = 'S'
while opcao in 'Ss':
    n = int(input('Digite qualquer valor: '))
    one.append(n)
    opcao = str(input('Quer conitnuar? [S/N]')).strip().upper()[0]
    if n % 2 == 0:
        two.append(n)
    else:
        three.append(n)
print(f'Lista 1 {one}')
print(f'Lista 1 {two}')
print(f'Lista 1 {three}')
