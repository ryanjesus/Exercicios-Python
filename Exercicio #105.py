"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings da função
"""

temp = list()
lista_notas = dict()


def nota(nota_aluno):
    """
    -> Adiciona a nota ao dicionário
    :param nota_aluno: Nota recebida do n
    :return: sem retorno
    """
    temp.append(nota_aluno)
    lista_notas["nota"] = temp
    # temp.clear()


def vw_notas():
    """
    ->Seguência de print
    :return:
    """
    print(f'Total: {len(temp)} Maior: {max(lista_notas["nota"])} Menor: {min(lista_notas["nota"])} Média: {sum(lista_notas["nota"]) / len(temp)}')


while True:
    n = float(input('Digite a notas dos alunos: '))
    nota(n)

    while True:
        res = str(input('Quer continuar? [S/N] ')).upper()[0]

        if res in 'SN':
            break
        else:
            print('Apenas Sim ou Não')
    if res in 'N':
        break

vw_notas()
