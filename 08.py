# Escreva um programa que solicite ao usuário um número e, 
# em seguida, imprima todos os números ímpares de 0 até o número fornecido.

def printUnevenNumbers():
    number = int(input("Digite um número inteiro:"))
    message = ("Números ímpares de 0 até {}").format(number)
    print(message)
    # O que temos acima é tudo o que já vimos nos exercícios anteriores

    for i in range(1, number+1 , 1):
        # o if abaixo checa se o número atual divido por dois tem resto
        if i % 2 != 0:
            print(i)


printUnevenNumbers()