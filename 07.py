# Escreva um programa que solicite ao usuário um número e, 
# em seguida, imprima todos os números pares de 0 até o número fornecido.

def printEvenNumbers():
    number = int(input("Digite um número inteiro:"))
    message = ("Números pares de 0 até {}").format(number)
    print(message)
    # O que temos acima é tudo o que já vimos nos exercícios anteriores

    # agora explicando o item abaixo, criamos uma estrutura de repetição onde
    # declaramos um valor chamado de 'i', e fazemos um ciclo de repetição,onde:
    # 2 : seria o número onde começamos o ciclo, já que 0 é um número neutro;
    # number + 1 : seria o índice até onde iríamos, já que na programação o primeiro número em algum índice seria o 0, e não 1;
    # 2 : seria de quanto em quanto estaríamos incrementando a busca, ou seja, pulando de 2 em 2.

    for i in range(2, number , 2):
        print(i)


printEvenNumbers()