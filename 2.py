def menu():
    print("selecciona la operaciom(1,2,3,4)")
    print("1.suma")
    print("2.resta")
    print("3.divide")
    print("4.multiplica")
    opcion =int(input())
    return opcion
def dameresultado(seleccion):
    num1 =int(input("primer numero"))
    num2 =int(input("segundo numero"))

    if(seleccion ==1):
        resultado = num1+num2

    elif(seleccion ==2):
        resultado =num1-num2
    elif(seleccion==3):
        resultado =num1/num2
    elif(seleccion==4):
        resultado =num1*num2
        try:
            resultado =num1/num2
        except:
            print("error al dividir")
            resultado=0
    else:
        print("selecione una opcion correcta")
    return  resultado

continua=True

while continua:
    seleccion = menu()
    resultado =dameresultado(seleccion)
    print(f"el resultado es {resultado}")
    print("quieres ontinuar(s/n")
    respuesta = input()
    if (respuesta =="s" or respuesta  =="S"):
        continua =True
    else:
        continua =False
        print("adios")


