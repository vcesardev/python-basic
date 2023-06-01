# Exercício de encontrar o maior elemento:
# Escreva um programa que encontre o maior elemento em uma lista e o imprima.

def findBiggerNumber():
    values = [10,13,20,21,1,18,50,0,13]

    biggestValue = 0

    for num in values:
        # neste caso, fazemos uma checagem de que se o maior valor atual for menor do que o item que está na lista,
        # o número da lista é atribuído como maior valor.
        if biggestValue < num:
            biggestValue = num

    print("O maior valor é:",biggestValue)

findBiggerNumber()
