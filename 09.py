# Escreva um programa que calcule a soma de todos os elementos em uma lista e imprima o resultado.

def calculateList():
    values = [3,7,8,1,15]

    sum = 0

    # ao fazer for item in values, fazemos um ciclo de repetição dentro do array de values, que contém 5 valores,
    # então ele irá passar por cada um dos 5 valores, sendo cada valor descrito como item.
    # portanto, em cada um dos números é feita uma incrementação do valor de soma passando por cada um
    # dos itens no array

    for item in values:
        sum += item

    print(sum)

calculateList()