"""Desenvolva um program que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:

A média de idade do grupo
Qual é o nome do homem mais velho
E quantas mulher tem menos de 21 anos"""

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
total_mulher_20 = 0

for c in range(1, 5):
    nome = str(input(f'Digite o {c} nome: ')).strip()

    idade = int(input(f'Digite a idade da {c} pessoa: '))
    soma_idade += idade

    sexo = str(input(f'Digite o sexo da {c} pessoa: ')).strip()
    if c == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulher_20 += 1

media_idade = soma_idade / 4

print(f'A média de idade do grupo é {media_idade}')

print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_velho}')

print(f'Ao todo são {total_mulher_20} mulheres com menos de 20 anos')