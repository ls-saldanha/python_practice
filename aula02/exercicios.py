# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
num_1 = int(input("Escreva um número: "))
num_2 = int(input("Escreva outro número: "))

soma = num_1 + num_2
print(f"A soma dos números é {soma}")

# Crie um programa que receba um número do usuário e calcule o resto da 
# divisão desse número por 5.

num_user = int(input("Insira um número: "))

resto_divisao = num_user % 5

print(f"O resto do número inserido dividido por 5 é {resto_divisao}")

#fazer commit desses dois exercicios

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio 
# como entrada.
import math
raio_user = int(input("Digite o raio da circunferência: "))
area_circulo = ((raio_user ** 2) * math.pi)

print(f"A área é {area_circulo}")

