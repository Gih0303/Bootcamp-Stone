#Estruturas de repetição

fechamento = dict()

nome = input("Digite o nome do aluno: ")

fechamento[nome] = []

condicao = "S"

while condicao == "S":
    nota = int(input("Digite uma nota: "))
    fechamento[nome].append(nota)
    condicao = input("Deseja entrar com outra nota? S ou N? ")
    if len(condicao) == 1 and condicao == "S":
        continue
    if len(condicao) == 1 and condicao == "N":
        break
    else:
        print("Condição inválida! Digite uma condição válida!") 
        condicao = input("Deseja entrar com outra nota? S ou N? ")

        