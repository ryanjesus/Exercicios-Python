""" Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são de maiores"""

total = 0
total_menor_idade = 0

for c in range(1, 8):
    nascimento = int(input(f'Digite o ano de nascimento da {c} pesso: '))
    if 2022 - nascimento>= 21:
        total += 1
    else:
        total_menor_idade += 1
print(f'Total de pessoas que atigiram a maioridade {total}\n'
      f'Total de pessoas que não atigiram a maioridade {total_menor_idade}')
