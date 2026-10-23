import os
import time
os.system("cls")

while True:
    num1 = float(input("Digite o Primeiro Número: "))
    num2 = float(input("Digite o Segundo Número: "))
    operacao = input("Qual operação Desejada? : ")


    match operacao:
        case "+":
            resultado = num1 + num2
            break
        case "-":
            resultado = num1 - num2
        case "*":
            resultado = num1 * num2
        case "/":
            resultado = num1 / num2
        case _:
            print("Operação Inválida! Tente novamente.")
            input("Pressione qualquer tecla para Tentar novamente")
            time.sleep(1)
            os.system("Cls")

print(f"Primeiro Número: ", num1)
print(f"Segundo Número: ", num2)
print(f"Operação Escolhida: ", operacao)
print(f"Resultado: ", resultado)


