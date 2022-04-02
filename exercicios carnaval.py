
from math import radians, acos, sin, cos

print("Digite o primeiro ponto: ")
t1 = radians(float(input("Digite a latitude em graus: ")))
g1 = radians(float(input("Digite a longitude em graus: ")))

print("Digite o segundo ponto: ")
t2 = radians(float(input("Digite a latitude em graus: ")))
g2 = radians(float(input("Digite a longitude em graus: "))) 


distacia = 6371.01 * acos(sin(t1) *  sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2)) 

print(f"A distâcia em km calculada é: {distacia:.2f}.")

#outra opção

msg_primeira_coord = "Digite a primeira coordenada sem espaços e separadas por vírgulas: "
t1, g1 = list(map(float,input(msg_primeira_coord).split(",")))


msg_segunda_coord = input("Digite a segunda coordenada sem espaços e separadas por vírgulas: ")













#from random import sample

#def embaralha_palavra(palavra):    
    #embaralhado = sample(palavra, k=len(palavra))
    #return ''.join(embaralhado).lower()

#print(embaralha_palavra("Python"))








