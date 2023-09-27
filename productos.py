peso1=1.50
peso2=3.5
peso3=2.5

cantidad1=int(input("cuantas unidades quieres"))
cantidad2=int(input("cuantas unidades quieres"))
cantidad3=int(input("cuantas unidades quieres"))

peso_env1=cantidad1*peso1
peso_env2=cantidad2*peso2
peso_env3=cantidad3*peso3

peso_total =peso_env1+peso_env2+peso_env3
print(f"del producto 1 envia un peso de {round(peso_env1)} kg")
print(f"del producto 2 envia un peso de {round(peso_env2)} kg")
print(f"del producto 3 envia un peso de {round(peso_env3)} kg")


print(f"el peso enviado total es de  {round(peso_total,2)} kg")



