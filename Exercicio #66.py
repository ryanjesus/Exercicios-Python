"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles
"""

contador = resultado = n = 0
while n != 999:
    n = int(input('Digite um numero qualquer: '))
    if n != 999:
        resultado += n
        contador += 1
    else:
        break
print(f'Voce digitou 999 e por esse motivo o programa finalizou. \nA quantidade de numero digitado é {contador} e a soma é {resultado}')