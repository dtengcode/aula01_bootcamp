### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

# 4) Calcule o valor do bônus final

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?'

import typing_extensions

CONSTANTE_DO_BÔNUS = 1.5

nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))
bônus = float(input("Digite o valor do bônus: "))
bônus_final = salario + bônus * CONSTANTE_DO_BÔNUS
print(
    f"Olá {nome}, seu salário é {salario} e o bônus é {bônus}, totalizando {bônus_final}"
)
