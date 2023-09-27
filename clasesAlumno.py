class Alumno():
    def __init__(self,nombre,nota):
        self.nombre =nombre
        self.nota=nota
    def mostrar(self):
        print(f"nombre : {self.nombre}")
        print(f" nota {self.nota}")
    def valoracion(self):
        if self.nota <5:
            print(f"{self.nota} has suspendido")
        else:
            print(f"{self.nota} has aprobado")



if __name__ =="__main__":
    alumno1 =Alumno("GROW",8)
    alumno2=Alumno("PADME",10)
    alumno3 =Alumno("kim",3)
    alumno1.mostrar()
    alumno1.valoracion()
    alumno2.mostrar()
    alumno2.valoracion()
    alumno3.mostrar()
    alumno3.valoracion()