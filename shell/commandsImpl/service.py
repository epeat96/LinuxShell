import os

def copiar(a,b):
    if os.path.isfile(a) :
        a=open(a,"r")
    else :
        print("\""+a+"\""+" no existe o no es un archivo")

    if os.path.isfile(b) :
        print("\""+b+"\""+" ya existe o no es un archivo")
    else :
        if os.path.isdir(b) :
            print(b+" ya existe o no es un archivo")
        else :
            b=open(b,"w")
            b.write(a.read())
            a.close()
            b.close()
