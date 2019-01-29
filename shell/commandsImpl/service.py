import os
import shutil
'''
    Funcion lenctrl
        Esta funcion recibe como parametro una lista con los parametros parseados recibidos a travez del prompt
        de la shell , la cantidad de parametros que son validos y retorna true si la cantidad de parametros es valida
        o false si la cantidad no es valida
'''
def lenctrl(tokens,cantidad):
    # Si se introdujeron mas de <cantidad> parametros
    if len(tokens)>cantidad:
        print("Se introdujeron mas parametros de los aceptados")
        return False
    #Si se introdujeron menos de <cantidad> parametros
    elif len(tokens)<cantidad:
        print("Muy pocos parametros ingresados")
        return False
    return True
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
    Funcion copiar
        Recibe como parametros un archivo y una ruta o un directorio y una ruta y copia el arvhico/directorios
        a en la ruta b
'''
def copiar(a,b):
    #Si a existe y si b no existe
    if os.path.exists(a) and not os.path.exists(b):
        #copiar directorio recursivamente o el archivo
        if os.path.isfile(a): # Si a es un archivo
            #se intenta abrir a en modo lectura
            try:
                a=open(a,"r")
            #Mensaje de error en caso de que a no sea un archivo, no exista o la ruta sea invalida
            except IOError:
                print("El archivo o directorio: "+"\""+a+"\""+" no existe")
                return 1
            if os.path.isfile(b):
                #Mensaje de error en caso de que b no sea un archivo, no exista o la ruta sea invalida
                print("El archivo o directorio: "+"\""+b+"\""+" ya existe o la ruta no es valida")
                return 1
            else :
                #se intenta abrir b en modo escritura
                try:
                    b=open(b,"w")
                except IOError:
                    #Mensaje de error en caso de que b no sea un archivo, no exista o la ruta sea invalida
                    print("El archivo o directorio: "+"\""+b+"\""+" ya existe o la ruta no es valida")
                    return 1
                b.write(a.read())
                return 0
        #si a es un directorio
        elif os.path.isdir(a):
            #se intenta copiar el arbol de directorios
            try:
                shutil.copytree(a, b)
            #Mensaje de error en caso de que no se pueda
            except IOError:
                print("El archivo o directorio: "+"\""+b+"\""+" ya existe o la ruta no es valida")
                return 1
        #mensaje de error si a no es un directorio
        else:
            print("El archivo o directorio: "+"\""+a+"\""+" no existe")
            return 1
        return 0
    else:
        #Mensajes de error
        #Caso 1 El parametro a no existe (archivo o directorio a copiar)
        if not os.path.exists(a):
            print("El archivo o directorio: "+"\""+a+"\""+" no existe")
            return 1
        #Caso 2 El parametro b ya existe (ruta donde se debe copiar el archivo o directorio)
        elif os.path.exists(b):
            print("El archivo o directorio: "+"\""+b+"\""+" ya existe")
            return 1
