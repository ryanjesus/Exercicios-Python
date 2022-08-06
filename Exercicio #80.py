
"""
Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort())


No final, mosre a lista ordenada na tela
"""

opcao = 's'
lista = []
qtd = 0

while opcao in 'Ss':
    print('-=-'*20)
    numero = int(input('Digite um número: '))
    print('-=-' * 20 if qtd == 0 else '\033[0;33m Processando...\033[0;0m')
    if qtd == 0:
        lista.append(numero)
    else:
        for v in lista:
            if numero > v:
                print('\033[0;32mAdicionando no final da fila\033[0;0m')
                lista.append(numero)
                break
            else:
                print('\033[0;32mAdicionando no começo da fila\033[0;0m')
                lista.append(numero)
                break
    qtd += 1
    opcao = str(input('Quer continuar [S/N]'))
print(sorted(lista))