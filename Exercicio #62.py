"""
Melhore o desafio 061, perguntando para o usuario se ele quer
mostrar mais alguns termos. O programa encerra quando ele disser que
quer mostrar O termos
"""


termo = int(input("Digite o primeir termo: "))
razao = int(input("Digite a razão: "))

c = 0
f = 0
n = 0

while c != 10:
    termo -= razao
    c += 1
    print(termo, end=' ')
    if c == 10:
        n = int(input('\nQuer mostrar mais quantos termos? '))
        if n != 0:
            while f != n:
                termo -= razao
                f += 1
                print(termo, end=' ')
        else:
            print('Saindo do programa')
