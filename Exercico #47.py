""" Crie um programa que mostre na tela todos os números pares
que estão no intervalo entre 1 e 50"""

print('Todos os números pares ente 1 e 50')

for c in range(1, 50, 1):
    if c % 2 == 0:
        print(c)
print('Fim')