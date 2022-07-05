"""
Crie um program que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
"""
n = 0
media = contador = maior = menor = soma = 0
s = ''
while s != 'Não':
    n = int(input('Digite um número: '))
    s = str(input('Quer digitar mais valores [Sim/Não] '))
    contador += 1
    soma += n
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
media = soma / contador
print(f'A média é {media}, o maior numero é {maior} e o menor numero é {menor}')