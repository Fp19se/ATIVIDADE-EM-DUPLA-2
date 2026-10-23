import os
os.system("cls")

soma = 0
qtd_notas = 3
for i in range(qtd_notas):
    while True:
        nota = float(input(f"Digite a {i+1}° nota entre 0 e 10: "))
        if nota < 0 or nota > 10:
            print("Nota inválida, Tente novamente!")
            os.system("cls")
        else:
            soma = soma + nota
            break
            print()

media = soma / qtd_notas
if media >= 7:
    print("Aprovado com a Média: ", media)
elif media >= 5 and nota  <= 6.9:
    print("Recuperação.")
else:
    print("Reprovado com Média", media)

print(" = Fim! = ")