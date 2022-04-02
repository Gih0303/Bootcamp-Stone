qtd_km = int(input("Digite a quantidade de quilometros percorridos: "))

qtd_dias = int(input("Digite quantos dias você ficou com o carro:"))

preco_por_dia = 15
preco_por_km = 0.5

preco_total_km = qtd_km * preco_por_km
preco_total_dia = qtd_dias * preco_por_dia

preco_a_pagar = preco_total_km + preco_total_dia

print(f"Total a pagar: R$ {preco_a_pagar:7.2f}")
