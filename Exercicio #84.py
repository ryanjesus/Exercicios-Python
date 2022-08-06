"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.

No final mostre:

a) Quantas pessoas foram cadastrada

b) Uma listagem com as pessoas com o peso maior que 100

b) Uma listagem com as pessoas com o peso menor que 70
"""

temp = list()
dados = list()
acima_peso = list()
abaixo_peso = list()

while True:
    temp.append((input('Digite o seu nome: ')))
    temp.append(float(input('Digite o seu peso: ')))

    dados.append(temp[:])
    temp.clear()

    opcao = str(input('Quer continuar [S/N] '))
    if opcao in 'Nn':
        break

for c in dados:
    if c[1] >= 100:
        acima_peso.append(c[:])
    elif c[1] <= 70:
        abaixo_peso.append(c[:])

print(f'O total de pessoas cadastradas foi {len(dados)}')
print(f'Lista de pessoas acima do peso: {acima_peso}' if len(acima_peso) > 0 else 'Não foi registrado pessoas acima do peso')
print(f'Lista de pessoas abaixo do peso: {abaixo_peso}' if len(abaixo_peso) > 0 else 'Não foi registrado pessoas abaixo do peso')