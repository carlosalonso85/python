from tkinter import *
from tkinter import messagebox
from basedatos import *

ANCHO=560
ALTO=540
POSX=400
POSY=400
anchoAlto=str(ANCHO)+"x"+str(ALTO)
posicionx ="+"+ str(POSX)
posiciony="+"+str(POSY)

colorventana="blue"
colorFondo="blue"
colorLetrq="white"



def mostrarMensaje(titulo,mensaje):

    messagebox.showinfo(titulo,mensaje)

def limpiarDatos():
    nombre.set("")
    apellidos.set("")
    telefono.set("")
    email.set("")
    ID.set("")
    text.delete(1.0,END)

def guardar():
    crearTabla()
    if((nombre.get()=="")or (apellidos.get()=="")):
        mostrarMensaje("error","debe de rellenar los datos")
    else:
        datos=nombre.get(),apellidos.get(),telefono.get(),email.get()
        mostrarMensaje("guardar","contacto guardado")
        insertar(datos)
        limpiarDatos()

def actualizar():
    crearTabla()
    if((ID.get()=="")or (ID.get()==0)or(nombre.get()=="")):
        mostrarMensaje("error","debes de rellenar los datos")
    else:
        try:
            modificar(ID.get(),nombre.get(),apellidos.get(),telefono.get(),email.get())
            mostrarMensaje("modificar","contacto modificado")
            limpiarDatos()
            mostrar()
        except:
            mostrarMensaje("error","identificador no encontrado")


def eliminar():
    if(ID.get()=="")or (ID.get()==0):
        mostrarMensaje("error","debes insertar un identificador")
    else:
        try:
            borrar(ID.get())
            mostrarMensaje("borrar","contacto borrado")
            limpiarDatos()
            mostrar()
        except:
            mostrarMensaje("error","identificador no encontrado")

def mostrar():
    listado=consultar()
    text.delete(1.0,END)
    text.insert(INSERT,"ID\tnombre\tapellido\ttelefono\temail\n")
    for elemento in listado:
        id=elemento[0]
        nombre=elemento[1]
        apellidos=elemento[2]
        telefono=elemento[3]
        email=elemento[4]
        text.insert(INSERT,id)
        text.insert(INSERT,"\t")
        text.insert(INSERT,nombre)
        text.insert(INSERT,"\t")
        text.insert(INSERT,apellidos)
        text.insert(INSERT,"\t")
        text.insert(INSERT,telefono)
        text.insert(INSERT,"\t")
        text.insert(INSERT,email)
        text.insert(INSERT,"\n")









ventana=Tk()
ventana.config(bg=colorventana)
ventana.geometry(anchoAlto+posicionx+posiciony)
ventana.title("agenda")
frame=Frame()
frame.config(width=ANCHO,height=ALTO)
frame.config(bg=colorventana)
frame.pack()

ID=IntVar()
nombre =StringVar()
apellidos=StringVar()
telefono=StringVar()
email= StringVar()

etiquetaID=Label(frame,text="ID:").place(x=50,y=50)
cajaID=Entry(frame,textvariable=ID).place(x=130,y=50)
etiquetaNombre=Label(frame,text="nombre: ").place(x=50,y=90)
cajaNombre =Entry(frame,textvariable=nombre).place(x=130,y=90)

etiquetaApellidos=Label(frame,text="apellido: ").place(x=50,y=130)
cajaApellido =Entry(frame,textvariable=apellidos).place(x=130,y=130)

etiquetaTelefono=Label(frame,text="telefono: ").place(x=50,y=170)
cajaTelefono =Entry(frame,textvariable=telefono).place(x=130,y=170)

etiquetaEmail=Label(frame,text="email: ").place(x=50,y=210)
cajaEmail =Entry(frame,textvariable=email).place(x=130,y=210)
text=Text(frame)
text.place(x=50,y=240,width=500,height=200)
botonAñadir=Button(frame,text="Añadir",command=guardar).place(x=150,y=500)
botonBorrar=Button(frame,text="borrar",command=eliminar).place(x=200,y=500)
botonConsultar=Button(frame,text="consultar",command=mostrar).place(x=250,y=500)
botonModificar=Button(frame,text="Actualizar",command=actualizar).place(x=320,y=500)


ventana.mainloop()