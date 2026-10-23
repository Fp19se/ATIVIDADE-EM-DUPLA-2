import os
os.system('cls')


nome_do_produto = str(input('Qual produto deseja: '))
quantidade_comprada = int(input('Qual a quantidade deseja: '))
preco = float(input('Qual o preço do produto escolhido: '))

total = quantidade_comprada * preco

if quantidade_comprada <= 5:
    desconto = preco * 0.02

elif quantidade_comprada >= 6 and quantidade_comprada <= 10:
    desconto = preco * 0.03

else:
    desconto = preco * 0.05

valor_com_desconto = preco - desconto
total_a_pagar = valor_com_desconto

print()
print(f'O produto: {nome_do_produto}')
print(f'O total: {total}')
print(f'O desconto: {desconto}')
print(f'O total a pagar: {total_a_pagar}')

