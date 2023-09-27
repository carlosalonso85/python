def mayor(num1,num2):
    if num1<num2:
        return num2
    elif num1>num2:
        return num1
    else:
        return False
elmayor =mayor(4,4)
if(elmayor ==False):
        print("los numeros son iguales")

else:
    print(f"el mayor es el {elmayor}")
    