# Escreva um programa que solicite ao usuário um raio e, em seguida, 
# calcule e imprima a área de um círculo com base no raio fornecido (use a fórmula: área = π * raio²).

import math

def calculateCircleArea():
    # usando float antes do input, convertemos o valor para um número para que possamos fazer um cálculo.
    radius = float(input("Digite a área de um círculo:"))

    area = math.pi * radius ** 2
    print("A área do círculo é de:",area)

calculateCircleArea()