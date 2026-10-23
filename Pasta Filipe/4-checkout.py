import os
os.system('cls')

valor = float(input('Digite o valor do produto: '))
print('''
===FORMA DE PAGAMENTO===

(1) Pagamento à vista
(2) Pagamento à prazo
''')
pagamento = int(input('Qual a forma de pagamento? '))


desconto = valor * 0.10
valor_com_desconto = valor - desconto
match pagamento:
    case 1:
        avista = desconto
    case _:
        parcela = int(input('\ndigite a quantidade de parcelas que deseja pagar até 6 vezes: '))

conta = valor / parcela

match pagamento:
    case 1:
        print('Valor do produto', valor)
        print('Forma de pagamento: ', pagamento)
        print('Valor do desconto: ', desconto)
        print('total a pagar: ', valor_com_desconto )
    case _:
        print('Valor do produto', valor)
        print('Forma de pagamento: ', pagamento)
        print('Quantidade de parcelas: ', parcela)
        print('Valor por parcela: ', conta)
        print('Total á prazo: ', valor )
