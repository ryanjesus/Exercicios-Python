from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastrada', 'Cadastrar nova Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # cabeçalho('Opção 1')
        lerArquivo(arq)
    elif resposta == 2:
        # cabeçalho('Opção 2')
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema')
        break
    else:
        print('ERRO! Digite uma opção válida!')