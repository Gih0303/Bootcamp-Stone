
import cartela

def sorteia():
    letra_sorteada = "G"
    minimo, maximo = cartela.min_max(letra_sorteada) 
    numero_sorteado = 60
    print(f"A combinação sorteada foi {letra_sorteada}{numero_sorteado}.") 
    return letra_sorteada, numero_sorteado 



