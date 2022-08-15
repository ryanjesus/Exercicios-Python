"""
Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer com parâmetro e mostre
uma mensagem com tamanho adaptável
"""

def escreva(msg):
    tamanho = len(msg) + 4
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)


escreva('Oi')