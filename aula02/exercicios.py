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

print(f"A área é {area_circulo:.2f}")

#------------------------------ 

# #### Inteiros (`int`)

# 3. Desenvolva um programa que multiplique dois números fornecidos 
# pelo usuário e mostre o resultado.

x = int(input("Digite o primeiro numero a ser multiplicado: "))
y = int(input("Digite o segundo numero a ser multiplicado: "))

resultado = x * y
print(f"O resultado da multiplicação é: {resultado}")

#------------------------------ 

# 4. Faça um programa que peça dois números inteiros 
# e imprima a divisão inteira do primeiro pelo segundo.
try: 
    x = int(input("Forneça um numero inteiro: "))
    y = int(input("Forneça um segundo número inteiro: "))
    z = x // y
    print("O resultado da divisão inteira é: ", z)

except ValueError:
    print("Os números fornecidos tem de ser números inteiros!")

except TypeError:
    print("Os números fornecidos tem de ser números inteiros!")

except ZeroDivisionError:
    print("O segundo número não pode ser 0!")


#------------------------------ 

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
temp_celsius = float(input("Forneça a temperatura em Celsius: "))
temp_fah = temp_celsius*1.8 + 32
print(f"A temperatura em fahrenheit é: {temp_fah}ºF")


# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data 
# no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.


# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação