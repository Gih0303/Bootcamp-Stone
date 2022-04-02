#Funções

def calcula_media(lst: list) -> float:
    return sum(lst) / len (lst)

def calcula_media_ponderada(valores: list, pesos: tuple|none = none) -> float:
    numerador = 0
    denominador = sum(pesos)
    for valor, peso in zip(valores, pesos):
        numerador = numerador + valor * peso
    return numerador / denominador 


fechamento = dict()

numero_alunos = int(input("Querido usuário, quantos alunos serão?"))
numero_notas = int(input("Quantas notas por aluno?"))

for _ in range(numero_alunos): 
    nome = input("Digite o nome do aluno: ")

    fechamento[nome] = [] 

for _ in range(numero_notas):
    nota = int(input(f"Digite a nota do {nome}: "))

    fechamento[nome].append(nota)

media = sum(fechamento[nome]) / len(fechamento[nome])

for aluno, notas in fechamento.items():
    media = calcula_media_ponderada(notas, [1, 2, 3])
    print(f"A media do aluno {aluno} foi {media}!")


    










