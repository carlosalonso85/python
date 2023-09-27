palabra =input("dime una palabra ")
palabrareves =palabra[::-1]
print(palabra)
print(palabrareves)
if(palabra==palabrareves):
    print("es palindromo")
else:
    print("no es palidromo")
    