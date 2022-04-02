from ast import NodeTransformer


aluno = "Giselly Landim"

notas []

notas.append(float(input(f"Digite a primeira nota: ")))

notas.append(float(input(f"Digite a segunda nota: ")))

notas.append(float(input(f"Digite a terceira nota: ")))

media = sum(notas) / len(notas)



nota_minima_aprovacao = 7
nota_minima_rec = 6

if media >= nota_minima_aprovacao:
    status = "Aprovado"

elif media >= nota_minima_rec:
    nota_minima = min(notas) 
    nota_minima_indice = notas.index(nota_minima) 
    notas.pop(nota_minima_indice)
    media_recalculada = sum(notas) / len(notas)  

    if media >= nota_minima_aprovacao:
        status = f"Aprovado com {len(notas)}"
    else:
        status = "Recuperacao"


    status = "recuperacao"

else:
    status = "Reprovado"

media_arred = round(media, 2)

print(f"\nA media do aluno {aluno} é {media_arred} e este aluno tem o seguinte: {status}.")