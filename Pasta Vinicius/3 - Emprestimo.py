import os
os.system("cls")

renda = float(input("Digite sua renda mensal: R$ "))
valor_total = float(input("Digite o valor do emprestimo: R$ "))
parcelas = int(input("Digite a quantidade de parcelas: "))

prestacao = valor_total / parcelas
max_emprestimo = renda * 10
max_prestacao = renda * 0.3

if valor_total <= max_emprestimo and prestacao <= max_prestacao:
    print("Emprestimo APROVADO!")
else:
    print("Emprestimo NEGADO!")