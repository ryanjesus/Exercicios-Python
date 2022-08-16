"""
Faça um programa que tenha uma função chamada maior(), que receba vários
parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
qtd = 0

def maior(*numeros):
    max(numeros)


while True:
    numeros = int(input('Digite qualquer valor: '))
    qtd += 1
    res = str(input('Quer continuar? [S/N] ')).upper()[0]

    while True:
        if res in 'SN':
            break
        else:
            print('Apenas Sim ou Não')
    if res in 'Nn':
        break

print(f'O maior valor é {maior(numeros)} e foram informados {qtd}')