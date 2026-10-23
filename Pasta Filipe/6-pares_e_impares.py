import os
os.system('cls')

pares = 0
impares = 0
soma = 0
QUANTIDADE = 5

for i in range(QUANTIDADE):
    numero = int(input(f'Digite o {1+i}ª número: '))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    soma += numero

print(f'A quantidade de pares: {pares}')
print(f'A quantidade de impares: {impares}')
print(f'A soma: {soma}')