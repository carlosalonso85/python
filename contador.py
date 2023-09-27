contador =1
pares=0
impares=0
while contador <=50:
    print(contador)
    if contador %2==0:
        pares +=contador
    else: impares+=contador

    contador +=1
print(f"la suma e los pares es {pares}")
print(f"la suma de los imapres es  {impares}")