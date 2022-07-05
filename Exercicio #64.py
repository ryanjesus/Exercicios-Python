"""
Crie um programa que leia varios numeros inteiros pelos teclados.
O programa so vai parar quando o usuario digitar o valor 999, que e a condicao
de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles
"""
contador = resultado = n = 0
while n != 999:
    n = int(input('Digite um numero qualquer: '))
    if n != 999:
        resultado += n
        contador += 1
    else:
        print()
print(f'Voce digitou 999 e por esse motivo o programa finalizou. \nA quantidade de numero digitado é {contador} e a soma é {resultado}')