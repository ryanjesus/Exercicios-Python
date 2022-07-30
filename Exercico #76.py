"""
Crie um programa que tenha um tupla única com nomes de produtos e seus
respectivos preços na sequência.

No final, mostre uma listagem de preços, organizado os dados em forma tabular
"""

c = 0
listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

while True:
    for item in listagem:
        print(f'\n{listagem[c]}.............. R$' if c % 2 == 0 else listagem[c], end=' ')
        c += 1
    break

