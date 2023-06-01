# Escreva um programa que solicite ao usuário um número e, 
# conte até o fim desse número

def countNumber():
    number = int(input("Digite um número:"))
    message = "Certo, vamos contar até o número {}".format(number);
    print(message)

    for i in range(1,number + 1, 1):
        print(i)

countNumber()