""" Crie um programa que leia uma frase qualquer e diga se ela é polindroma,
desconsiderando os espaços"""

frase = input('Digite uma frase: ')
frase.replace(" ", "")
frase_invertida = (frase [::-1])

if frase == frase_invertida:
    print('É um polidromo')
else:
    print('Não é um polidromo')


