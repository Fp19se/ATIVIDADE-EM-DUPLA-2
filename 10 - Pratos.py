import os
os.system("cls")

pratos_pedidos = []
valores_pedidos = []
opcao_menu = 0

while opcao_menu != 4:
    os.system("cls")

    print("\n=== SISTEMA DE PEDIDOS ===")
    print("1 - Adicionar prato")
    print("2 - Remover prato")
    print("3 - Ver conta parcial")
    print("4 - Finalizar pedido")
    print("==========================")

    opcao_menu = int(input("Escolha uma opção: "))

    if opcao_menu == 1:
        os.system("cls")
        print("\n--- CARDÁPIO ---")
        print("1 - Picanha       - R$ 25.00")
        print("2 - Lasanha       - R$ 20.00")
        print("3 - Strogonoff    - R$ 18.00")
        print("4 - Bife Acebolado - R$ 15.00")
        print("5 - Pão com ovo   - R$ 5.00")
        print("----------------")

        codigo = int(input("Digite o código do prato desejado: "))

        if codigo == 1:
            pratos_pedidos.append("Picanha")
            valores_pedidos.append(25.00)
            print("Picanha adicionada!")
        elif codigo == 2:
            pratos_pedidos.append("Lasanha")
            valores_pedidos.append(20.00)
            print("Lasanha adicionada!")
        elif codigo == 3:
            pratos_pedidos.append("Strogonoff")
            valores_pedidos.append(18.00)
            print("Strogonoff adicionado!")
        elif codigo == 4:
            pratos_pedidos.append("Bife Acebolado")
            valores_pedidos.append(15.00)
            print("Bife Acebolado adicionado!")
        elif codigo == 5:
            pratos_pedidos.append("Pão com ovo")
            valores_pedidos.append(5.00)
            print("Pão com ovo adicionado!")
        else:
            print("Código inválido!")

        input("\nPressione ENTER para voltar ao menu...")

    elif opcao_menu == 2:
        os.system("cls")
        quantidade_itens = len(pratos_pedidos)

        if quantidade_itens == 0:
            print("\nNão há itens na conta para remover!")
        else:
            print("\n--- ITENS NA CONTA ---")
            for i in range(quantidade_itens):
                print(
                    i + 1,
                    "-",
                    pratos_pedidos[i],
                    "- R$",
                    valores_pedidos[i],
                )
            print("----------------------")

            item_remover = int(
                input("Digite o número do item que deseja remover: ")
            )

            if item_remover >= 1 and item_remover <= quantidade_itens:
                posicao = item_remover - 1

                prato_removido = pratos_pedidos.pop(posicao)
                valor_removido = valores_pedidos.pop(posicao)

                print("\n", prato_removido, "foi removido da conta!")
            else:
                print("Número de item inválido!")

        input("\nPressione ENTER para voltar ao menu...")


    elif opcao_menu == 3:
        os.system("cls")
        print("\n--- RESUMO PARCIAL ---")
        quantidade_itens = len(pratos_pedidos)
        total_parcial = 0.0

        for i in range(quantidade_itens):
            print(pratos_pedidos[i], "- R$", valores_pedidos[i])
            total_parcial = total_parcial + valores_pedidos[i]

        print("----------------------")
        print("TOTAL PARCIAL: R$", total_parcial)

        input("\nPressione ENTER para voltar ao menu...")



os.system("cls")
print("\n=== CONTA FINAL ===")

total_conta = 0.0
quantidade_itens = len(pratos_pedidos)

for i in range(quantidade_itens):
    nome_prato = pratos_pedidos[i]
    valor_prato = valores_pedidos[i]

    print(nome_prato, "- R$", valor_prato)
    total_conta = total_conta + valor_prato

print("-------------------")
print("TOTAL A PAGAR: R$", total_conta)