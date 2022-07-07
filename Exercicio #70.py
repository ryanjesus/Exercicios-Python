"""
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar. No final, mostre:

a) Qual é o total gasto na compra
b) Quantos produtos custam mais de R$1000.
c) Qual é o nome do produto mais barato.
"""

print('-'*20)
print('LOJA SUPER BARATÃO')
print('-'*20)

totalcompra = mais = 0
carrinnho = []
while True:
    produto = str(input('Nome do produto: '))
    preco = int(input('Preço: R$ '))
    carrinnho += [produto]
    totalcompra += totalcompra
    print(f'Cainho: {carrinnho}')
    if preco > 1000:
        mais += 1
    questao = ' '
    while questao not in 'SsNn':
        print('-'*20)
        questao = str(input('Quer continua? [S/N] ')).strip().upper()[0]
    if questao == 'N':
        print('Saindo do programa')
        break
print(f'Valor total: {totalcompra} ')
print(f'{mais} custam mais de R$1000')
print(f'O produto mais barato é {min(carrinnho)}')