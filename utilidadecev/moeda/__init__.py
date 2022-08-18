from utilidadecev import dado


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n):
    print('-'*30)
    print('RESUMO DO VALOR')
    print('-' * 30)
    print(f'Preço analisado: {moeda(n):^}')
    print(f'Dobro do preço: {moeda(dado.dobro(n)):^}')
    print(f'Metade do preço: {moeda(dado.metade(n)):^}')
    print(f'10% de aumento: {moeda(dado.aumentar(n)):^}')
    print(f'13% de redução: {moeda(dado.reduzir(n)):^}')