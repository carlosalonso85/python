from random import randint as azar

numero=azar(1,100)
usuario =int(input("adividina el numero que he pensado"))
continua=True
intentos =0
while (continua):
    if usuario<numero:
        print("el numero que he pensado es mayor")
        intentos =intentos+1
        usuario=int(input("adivida el numero"))
    elif usuario>numero:
        print("el numero que he pensado es menor")
        intentos =intentos+1
        usuario =int(input("adividina el numero"))
    else:
        print("bien lo adivinastes")
        print("el numero de intentos es "+str(intentos))
        print("quieres continuar(s/n)")
        if(input()=="s"or input()=="S"):
            contiua =True
            intentos =0
            piensanumero =azar(1,100)
            usuario =int(input("adivina el numero"))
else:
    contiua=False
print("fin dle juego")
