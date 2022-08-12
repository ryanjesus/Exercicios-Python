"""
Aprimore o DESAFIO 093 para que ele funcione com varios jogadores,
incluindo um sistema de visualizçao de detalhes
do aproveitamento de cada jogador
"""

jogador = dict()
temp = list()
lista = list()

while True:

    print('-='*30)

    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for p in range(0, partidas):
        temp.append(int(input(f'Quantos gols na partida {p + 1}? ')))

    jogador['gols'] = temp[:]
    jogador['total'] = sum(temp)
    temp.clear()
    lista.append(jogador.copy())

    while True:
        op = str(input('Quer continuar? [S/N]')).upper()[0]

        if op in 'SN':
            break
        else:
            print('ERRO! Por favor, digite apenas S ou N')
    if op == 'N':
        break

print('-='*30)
print(lista)
print('-='*30)


print('Cod', end=' ')
for f in jogador.keys():
    print(end=' 'f'{f:^8}')

print()

for k in range(0, len(lista)):
    print(f'{k:^5} {lista[k]["nome"]:^8} {lista[k]["gols"]} {lista[k]["total"]:^4}')

print('-='*30)

while True:

    dados = int(input('Mostra dados de qual jogador? [999 sair]'))
    if dados == 999:
        print('Finalizando o programa')
        break

    if dados >= len(lista):
        print('\033[0:33mErro! Menssagem: Não tem jogador com esse ID\033[0:0m')

    else:
        print('-' * 30)
        print(f'O jogando {lista[dados]["nome"]} jogou {len(lista[dados]["gols"])} partidas')

        for p in range(0, partidas):
            print(f'Na partida {p + 1}, fez {lista[dados]["gols"][p]} gols')

