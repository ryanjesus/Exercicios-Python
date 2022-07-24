"""
Crie um tupla preenchida com os 20 primeiros colocados da tabela
do campeonato brasileiro de futebol, na ordem de coloção. Depois mostre

A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense.
"""

tabela = 'Palmeiras', 'Corinthians', 'Atlético-MG', 'Fluminense', 'Athletico-PR', 'Flamengo', 'internacional', 'Bragantino', 'São Paulo', 'Santo', 'Botafogo', 'Ceará SC', 'Goiáis', 'Avaí', 'Cuibá', 'Coritiba', 'Améria-MG', 'Atlético-GO', 'Fortaleza', 'Juventude'

print('-=-'*20)
print('Tabela do campeonato brasileiro de futebol')

print('Os 5 primeiros colocados')
for time in range(0, len(tabela)):
    if time <= 4:
        print(f'{time + 1}º {tabela[time]}')
    else:
        print('-=-' * 20)
        break

print('Os 4 ultimos colocados')
for c in range(-4, len(tabela)):
    # print(tabela[16:])
    print(f'{tabela[c]}' if c != 0 or c != None else print('-=-' * 20))
    if c == 0:
        break
print('-=-' * 20)
print('Lista com os times em ordem alfabética.')
for ordem in sorted(tabela):
    print(ordem)
print('-=-' * 20)

while True:
    n = str(input('Digite o nome do seu time: '))
    if n in tabela:
        print(f'O {n} está na posição {tabela.index(n) + 1}º')
        break
    else:
        print('O seu time não está na lista')