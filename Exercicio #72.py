"""
Crie um programa que tenha um tupla totalmente preenchida com uma contagem por extenso, de zero até
vinte

Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo por extenso
"""

n = 0
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um numero entre 0 e 20: '))
    if n < 0 or n > 20:
        continue
    if 0 <= n <= 20:
        print(f'Você digitou o numero {numeros[n]}')
        opcao = str(input('Quer continuar [S/N]')).strip().upper()[0]
        while opcao not in 'SsNn':
            opcao = str(input('Quer continuar [S/N]')).strip().upper()[0]
            if opcao in 'Ss':
                continue
            elif opcao in 'Nn':
                print('Programa finalizado')
                break



