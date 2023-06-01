# Exercício de contar ocorrências:
# Escreva um programa que conte quantas vezes um determinado valor ocorre em uma lista e imprima o resultado.

def countAmountOfTimes():
    values = [1,1,1,1,3,4,4,4,2,1,1,3,3,3,10]
    valueToSearch = 3
    occurrences = 0

    for num in values:
        if num == valueToSearch:
            occurrences += 1

    message = "O número {} aparece {} vez(es) na lista.".format(valueToSearch,occurrences)
    print(message)

countAmountOfTimes()