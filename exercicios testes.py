metros = float(input("Digite o valor em metros: "))
milimetros = metros * 1000
print(f"{metros} metros equivalem a {milimetros} milimetros.")


dias = int(input("Dias:"))
horas = int(input("Horas:"))
minutos = int(input("Minutos:"))
segundos = int(input("Segundos:")) 
total_em_segundos = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos
print(f"Convertido em segundos é igual a {total_em_segundos} segundos.")

salario = float(input("Digite seu salario atual:"))
p_aumento = float(input("Digite a porcentagem de aumento:"))
aumento = salario * p_aumento/100
novo_salario = salario + aumento
print(f"Um aumento de {p_aumento} % em um salario de {salario} ")
print(f"É igual a um aumento de {aumento} ")
print(f"Resultando em um novo salario de {novo_salario} ")

preco = float(input("Digite o preco da mercadoria:"))
desconto = float(input("Digite o percentual de desconto:"))
valor_desconto = preco * desconto/100
a_pagar = preco - valor_desconto 
print(f"Um desconto de {desconto} em uma mercadoria de {preco} ")
print(f"vale R$ {valor_desconto}")
print(f"O valor a pagar é de {a_pagar}")


C = float(input("Digite a temperatura em °C:"))
F = (9 * C / 5) + 32
print(f"A temperatura de {C} ceusius equivale a {F} F.")






 












