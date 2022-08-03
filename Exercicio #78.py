"""
 Faça um programa que leia 5 valores numéricos e guarde-so em uma lista

 No final, mostre qual foi o maior e o menor valor digitado
 e as suas respectivas posições na lista
"""


"""num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.remove(2)
print(num)"""

lista = []
for contagem in range(0, 5):
    lista.append(int(input(f'Digite o valor na posição {contagem}: ')))

# for c, v in enumerate(lista):
#     print(f'Na posição {c} está o valor {v}')
print('-=-'*20)
print(f'Você digiou os valores: \033[0;31m{lista}')

print('\033[0;0m-=-'*20)
print(f'\033[0;0m O menor valor digitado é \033[0;31m{min(lista)} \033[0;0mnas posições \033[0;31m{lista.index(min(lista))}')
print(f'\033[0;0m O maior valor digitado é \033[0;31m{max(lista)} \033[0;0mnas posições \033[0;31m{lista.index(max(lista))}')
