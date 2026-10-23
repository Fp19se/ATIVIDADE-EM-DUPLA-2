import os
os.system("cls")

pratos_pedidos = []
valores_pedidos = []
deseja_continuar = "S"

while deseja_continuar == "S" or deseja_continuar == "s":
    
    
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
        print("Código inválido! Tente novamente.")
        continue
        
    
    deseja_continuar = input("Deseja escolher outro prato? ( S ou N ): ")
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