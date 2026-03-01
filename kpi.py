CONSTANTE_BONUS = 1000
user_name = input("Digite seu nome: ")
salario_usuario = float(input("Digite seu salário mensal: "))
percentagem_bonus = float(input("Insira a porcentagem do seu bônus: "))

valor_bonus = CONSTANTE_BONUS + salario_usuario * percentagem_bonus

print(f"Olá {user_name}, o valor do seu bônus é {(valor_bonus:.2f}")