"""
Crie um programa que vai ler varios numeros e colocar em uma lista

Depois disso, mostre:

a) Quantos numeros foram digitados

b) A lista de valores, ordenada de forma decresecente

c) Se valor 5 foi digitado e esta ou nao na lista
"""


opcao = 'S'
qtdcindo = qtd = 0
lista = []
while opcao in 'Ss':
    n = lista.append(int(input('Digite qualquer valor: ')))
    opcao = str(input('Quer continua? [S/N] ')).strip().upper()[0]
    qtd += 1
    if n == 5:
        qtdcindo += 1
print(f'O total de numeros digitado é {qtd}')
print(f'A lista em ordem decresecente é {sorted(lista, reverse=True)}')
print(f'O valor 5 foi digita {qtdcindo} vezes' if 5 in lista else 'Não tem o valor 5 na lista')