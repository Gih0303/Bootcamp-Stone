
consumo = int(input("Consumo em kWh: "))
tipo = input("Tipo da instalação (R, C ou I): ")

if tipo == "R":
    if consumo <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo == "C":
    if consumo <= 1000:
        preco = 0.55
    else:
        preco = 0.60
elif tipo == "I":
    if consumo <=5000:
        preco = 0.55
    else:
        preco = 0.60
else:
    preco = 0
    print("Erro ! Tipo de instalação desconhecido!")

custo = preco * consumo
print(f"Valor a pagar é: R$ {custo:7.2f}.")














