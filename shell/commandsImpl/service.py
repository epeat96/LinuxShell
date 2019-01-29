import os
def copiar(a,b):
    if os.path.isfile(a) :
        a=open(a,"r")
    else :
        print("El archivo "+a+" no existe o no es un archivo")

    if os.path.isfile(b) :
        print("El archivo "+b+" ya existe o no es un archivo")
    else :
        b=open(b,"w")
        b.write(a.read())
        a.close()
        b.close()
