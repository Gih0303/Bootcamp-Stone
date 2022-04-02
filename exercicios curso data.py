# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na sua instrução de impressão.

frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir."
count = 0
for letra in frase:
    if letra == "r":
        count += 1
print("A letra r aparece %s vezes na frase." %(count))  














