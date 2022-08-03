"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
lista. Caso o númmero já exista lá dentro, ele não será adicionado.

No final, serão exibidos todos os valores únicos digitadosm em ordem crescente
"""
op = 'S'
lista = []
while op in 'Ss':
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('\033[0;31mValor ja existe\033[0;0m')
        # print(f'\033[0;33mSegue lista {lista}\033[0;0m')
    else:
        lista.append(valor)
        print('\033[0;32mValor adcionado com sucesso!\033[0;0m')
        op = str(input('Quer continuar[S/N] ')).upper().strip()[0]
        if op in 'sS':
            continue
        elif op in 'nN':
            print(f'Os valores digitados foram \033[0;33m{sorted(lista)}\033[0;0m')
            break

