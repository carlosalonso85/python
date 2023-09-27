import time

for contador in range(10,-1,-1):
    if contador !=0:

        print(f"\r{contador}",end=" ")
        time.sleep(1)
    else:
        print(f"\r{contador}",end=" ")
        print("fin de la cuenta atras")