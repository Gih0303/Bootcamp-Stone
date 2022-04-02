aluno = "Giselly Landim"
nota_1 = float(input(f"Digite a primeira nota: "))
nota_2 = float(input(f"Digite a segunda nota: "))
nota_3 = float(input(f"Digite a terceira nota: "))
media = (nota_1 + nota_2 + nota_3) / 3
media_arred = round(media, 2)

print(f"\nA media do aluno {aluno} é {media_arred}.")

# Simplificando
aluno = "Giselly Landim"
notas = [10, 8, 6]
media = sum(notas) / len(notas)

media_arred = round(media, 2)
print(f"\nA media do aluno {aluno} é {media_arred}.")


