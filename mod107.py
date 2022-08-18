
def metade(n, formato=False):
    m = n / 2
    return m if formato is False else moeda(n)


def dobro(n, formato=False):
    m = n * 2
    return m if formato is False else moeda(n)


def aumentar(n, formato=False):
    m = n + n * 0.10
    return m if formato is False else moeda(n)


def reduzir(n, formato=False):
    m = n - n * 0.13
    return m if formato is False else moeda(n)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n):
    print('-'*30)
    print('RESUMO DO VALOR')
    print('-' * 30)
    print(f'Preço analisado: {moeda(n):^}')
    print(f'Dobro do preço: {moeda(dobro(n)):^}')
    print(f'Metade do preço: {moeda(metade(n)):^}')
    print(f'10% de aumento: {moeda(aumentar(n)):^}')
    print(f'13% de redução: {moeda(reduzir(n)):^}')
