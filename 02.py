# Escreva um programa que solicite ao usuário dois números e, em seguida, 
# imprima a soma dos dois números.



# abaixo criamos uma função onde recebemos dois números, obviamente você poderia somente exibir os dois números utilizando:

# def sumNumbers(value1,value2):
#     sum = value1+value2
#     print("A soma é:",sum)


# porém é interessante para ter uma visão mais clara dos valores utilizados, mas por enquanto não se
# importe com o exemplo que utilizei, foque no exemplo acima ^.

def sumNumbers(value1,value2):
    mensagem = ("A soma de {} e {} é de: {}").format(value1, value2, value1+value2)
    print(mensagem)

sumNumbers(5,10)