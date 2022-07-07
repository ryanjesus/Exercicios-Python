"""
Faça um programa que jogue par ou impar com o computador.
O jogo só será interrompido quando o jogador perde,
mostrando o total de vitórias consecutivas que ele conquistou no
final do jogo.
"""
from random import randint
v = 0
while True:
    valor_usuario = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = valor_usuario + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar? ')).strip().upper()[0]
    print(f'Você jogou {valor_usuario} e o computador {computador}. total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu')
    print('Vamos jogar novamente...')
print(f'Game over! Você venceu {v} vezes')