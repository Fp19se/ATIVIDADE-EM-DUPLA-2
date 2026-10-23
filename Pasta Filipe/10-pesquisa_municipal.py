import os

contador_famillias = 0
quantidade_geral_filhos = 0
soma_salario = 0
maior_salario = 0
menor_salario = 9999

while True:
    os.system('cls')
    print('''
=== MENU ===
1 - Adicionar família
2 - Sair e exibir resultados
''')
    opcao = int(input('Digite a opção desejada: '))

    match opcao:
        case 1:
            print('=== CADASTRO ===')
            salario = float(input('Digite o salário: R$ '))
            numero_de_filhos = float(input('Digite a quantidade de filhos: '))

            contador_famillias += 1
            soma_salario += salario
            quantidade_geral_filhos += numero_de_filhos

            maior_salario = max(salario, maior_salario)
            menor_salario = min(salario, menor_salario)


            print('\nFamília adicionada com sucesso!')
            input('Pressione uma tecla para continuar...')
        case 2:
            break
        case _:
            print('\nOpção inválida! \n')
            input('Pressione uma tecla para continuar...')


if contador_famillias == 0:
    print('\nNenhuma família cadastrada. \n')
    input('Pressione uma tecla para continuar...')
else:
    media_salario = soma_salario / contador_famillias
    media_numero_filhos = quantidade_geral_filhos / contador_famillias
   
    print('\n=== RESULTADOS DA PESQUISA ===')
    print(f'Total de famílias que responderam a pesquisa: {contador_famillias}')
    print(f'Média de salário da população: R$ {media_salario}')
    print(f'Média de número de filhos: {media_numero_filhos}')
    print(f'Maior salário: {maior_salario}')
    print(f'Menor salário: {menor_salario}')

    input('\nPressione uma tecla para continuar...')