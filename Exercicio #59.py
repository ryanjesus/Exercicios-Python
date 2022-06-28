"""
Crie um programa que leia dois valores e mostre um menu na tela:

[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] sair do programa

Seu programa deverá realizar a péração solicitada em cada caso
"""

v1 = v2 = n = 0
v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))
while n != 5:
    print(' [1] Somar\n [2] Multiplicar\n [3] Maior\n [4] Novos números\n [5] sair do programa\n')
    n = int(input("Escolha a função: "))
    if n == 1:
        resultado = v1 + v2
        print(f'{v1} + {v2} = {resultado}')
    elif n == 2:
        resultado = v1 * v2
        print(f'{v1} + {v2} = {resultado}')
    elif n == 3:
        resultado = [v1, v2]
        print(f'O maior valor é {max(resultado)}')
    elif n == 4:
        v1 = int(input("Digite o primeiro valor: "))
        v2 = int(input("Digite o segundo valor: "))
    elif n == 5:
        print('Você escolheu sair do programa')
    else:
        print('Apenas numero entre 1 a 5')
print('Saindo do programa')
