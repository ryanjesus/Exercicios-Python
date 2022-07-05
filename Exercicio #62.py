"""
Melhore o desafio 061, perguntando para o usuario se ele quer
mostrar mais alguns termos. O programa encerra quando ele disser que
quer mostrar O termos
"""


primeiro = int(input("Digite o primeir termo: "))
razao = int(input("Digite a razão: "))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} ', end=' ')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Fim')