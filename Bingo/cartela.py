from collections import defaultdict
from random import randint, seed

#seed(1) 

LETRAS = ("B", "I", "N", "G", "O")


def min_max(letra: str) -> tuple[int]:
    intervalo = {"B": (1, 15), "I": (16, 30), "N": (31, 45), "G": (46, 60), "O": (61, 75)}
    minimo, maximo = intervalo[letra][0], intervalo[letra][1] 
    return minimo, maximo 

def gerar():
    
    cartela = defaultdict(list)

    for letra in LETRAS:
        minimo, maximo = min_max(letra)

        while len(cartela[letra]) < 5: 
            num_aleatorio = randint(minimo, maximo)
            
            if num_aleatorio in cartela[letra]: 
                continue
            cartela[letra].append(num_aleatorio) 
            cartela[letra].sort()  
    return cartela

cartela_1 = gerar() 

def imprime(cartela_1: dict[str, list[int]]) -> None:
    print("B   I   N   G   O")  
    for linha in range(5):
        lista_str = [str(lista[linha]).zfill(2) for lista in cartela_1.values()]
        string = ", ".join(lista_str)
        print(string) 

def marca_numero(cartela: defaultdict, letra: str, numero: int, caracter: str):    
    indice = cartela[letra].index(numero)
    cartela[letra][indice] = caracter
    return cartela

def numero_existe(cartela, letra, numero):
    if numero in cartela[letra]:
        print("Você acertou um número!")
        return True 
    print("Você errou!")
    return False









        





    
