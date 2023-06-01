# Escreva um programa que solicite ao usuário um número e, 
# em seguida, verifique se o número é par ou ímpar e imprima o resultado.


# aqui basicamente passamos um número e o dividimos por 2,
# checamos se o 'resto' dele for zero, caso seja é exibido que o número é par
# do contrário, ímpar




def checkNumber():
    number = float(input("Digite um número:"))

    if number % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")
    
checkNumber()