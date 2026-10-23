import os
import time
os.system ("cls")

print("= Tabuada =")

print(f"\n- Multiplicação -")
numero = int(input(f"\nDigite um número: "))
for i in range(1, 11):
    print (f"{numero} * {i} = {numero * i} ")
    time.sleep(1)
print("_ Fim _")