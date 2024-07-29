
# 1) Solicita ao usuário que digite seu nome
# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
# 4) Calcule o valor do bônus final
# 5) Imprime a mensagem personalizada incluindo o nome do usuário e o valor do bonus
# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?




nome_usuario = input("Digite o seu nome: ");

salario = float(input("Informe o Seu Salário: "))

bonus = float(input("Informe o Valor do Bônus Recebido: "))

valorFinal = 1000 + salario * bonus;

print(f"O usuario {nome_usuario} possui o bonus de {valorFinal}")