
import cartela 
import sorteio 

cartela_1 = cartela.gerar() 

cartela.imprime(cartela_1) 

letra_sorteada, numero_sorteado = sorteio.sorteia() 

if cartela.numero_existe(cartela_1, letra_sorteada, numero_sorteado):
    cartela_1 = cartela.marca_numero(cartela_1, letra_sorteada, numero_sorteado, "xx")
cartela.imprime(cartela_1) 










 










