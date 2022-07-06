"""
Faça um programa que jogue par ou impar com o computador.
O jogo só será interrompido quando o jogador perde,
mostrando o total de vitórias consecutivas que ele conquistou no
final do jogo.
"""

while True:
    valor_usuario = int(input('Digite um valor: '))
    escolha = str(input('Escolha entre Par ou Impar [P/I]: ')).upper()
    if valor_usuario % 2 == 0:
        print('Você Escolheu' if escolha == 'I' 'Impar' else 'Par')
    elif valor_usuario % 2 != 0 and escolha == 'I':
        print('Você Escolheu' if escolha == 'I' 'Impar' else 'Par')