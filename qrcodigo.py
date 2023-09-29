import qrcode

nombrearchivo=input("introduce el nombre para tu archivo")

textoQr =input("dime el texto o enlace para el codigo qr")

imagen =qrcode.make(textoQr)

fichero =open(nombrearchivo+".png","wb")

imagen.save(fichero)
fichero.close()
print("el codigo qr se a creado con exito")
print("el el archivo esta guardado en la carpeta del script")
