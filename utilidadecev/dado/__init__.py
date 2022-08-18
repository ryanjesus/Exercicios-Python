from utilidadecev import moeda


def metade(n, formato=False):
    m = n / 2
    return m if formato is False else moeda.moeda(n)


def dobro(n, formato=False):
    m = n * 2
    return m if formato is False else moeda.moeda(n)


def aumentar(n, formato=False):
    m = n + n * 0.10
    return m if formato is False else moeda.moeda(n)


def reduzir(n, formato=False):
    m = n - n * 0.13
    return m if formato is False else moeda.moeda(n)


def leiaDinehiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'ERRO: \"{entrada}\" é um preço inválido')
        else:
            valido = True
            return float(entrada)
