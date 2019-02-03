import os
import shutil
import pwd
import subprocess as sub
import time
import getpass
def daemontools(inp):
	newpid=os.fork()
	if newpid==0:
		os.execl("/bin/python"," /home/daemons/daemon.py")
	else:
		print("auxiliomedesmayoxdxd")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def shenlong(cmd,inp):
	 try:
		 a = open("/var/log/lfsshell.log","a")
		 hora=time.strftime("%y-%m-%d %H:%M:%S")
		 a.write("[date:] "+hora+" [cmd:] "+cmd+" "+inp+" [user:] "+getpass.getuser()+"\n")
		 a.close()
	 except:
	 	print("Error")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def useradd(inp):

	try:
		if pwd.getpwnam(inp[0]) :
			print("El usuario: "+inp[0]+" ya existe")
			return 1
	except:
		pass

	try:
		sub.run("useradd" +" -c "+"\"hh/mm-hh/mm= "+inp[1]+" ip ="+inp[2]+"\" "+ inp[0],shell=True,executable="/bin/bash")
	except:
		print("si llega hasta aca no se que onda")
		return 1
	return 0
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def cd(tokens):
	try:
		os.chdir(tokens[0])
	except:
		print("Error: Ruta invalida")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def chown(tokens):
    #si la ruta es valida
    if os.path.exists(tokens[0]):
        #cambiar permisos al archivo o directorio raiz
        shutil.chown(tokens[0],tokens[1],tokens[2])
    else :
        #mensaje de error si la ruta es invalida
        print("Ruta invalida")
        return 1
    #se verifica si existe el 3er parametro y de ser asi se ve si es "-r"
    if len(tokens)==4 and tokens[3] =="-r":
            #Si ruta es valida
        if os.path.exists(tokens[0]) :
            #se cambian de forma recurisva los directorios y archivos de la carpeta raiz
            for root, dirs, files in os.walk(tokens[0]):
                for d in dirs:
                    shutil.chown(os.path.join(root, d),tokens[1],tokens[2])
                for f in files:
                    shutil.chown(os.path.join(root, f),tokens[1],tokens[2])
            return 0
        else :
            #mensaje si la ruta no es valida
            print("Ruta invalida")
            return 1
    elif len(tokens) == 4:
        #mensaje de error si el 3er parametro de chmod no es "-r"
        printf("No se reconoce el parametro: "+tokens[3])
    return 0
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def ls(tokens):
    if os.path.isdir(tokens[0]):
        b=os.listdir(tokens[0])
        for a in b:
            print(a,end=" ")
        return 0
    else :
        print("La ruta no es valida")
        return 1
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
    Recibe como paratetro una ruta y cambia de nombre el archivo/directorio
    OBS: si la ruta para renombrar ya existe rn sobreescribe el archivo, directorio
'''
def rn(tokens):
    try:
        os.rename(tokens[0],tokens[1])
    except IOError:
        print("La ruta no es valida")
        return 1
    return 0
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
    Recibe como parametro un string que contiene una ruta, un string representando un numero
    octal entre 000 y 777 y posiblemente un parametro que debe ser "-r" y retorna 0 si se pudo
    cambiar o 0 si hubo error
'''
def chmod(tokens):
    #intenta castear el string a un numero octal
    try :
        a=int(tokens[1],8)
    except :
        #mensaje de error si no se puede
        print("Por favor ingrese un numero en octal entre 000 y 777")
        return 1
    #si la ruta es valida
    if os.path.exists(tokens[0]):
        #cambiar permisos al archivo o directorio raiz
        os.chmod(tokens[0],a)
    else :
        #mensaje de error si la ruta es invalida
        print("Ruta invalida")
        return 1
    #se verifica si existe el 3er parametro y de ser asi se ve si es "-r"
    if len(tokens)==3 and tokens[2] =="-r":
        #se verifica que el numero en octal este en rango
        if 0o000 <= a <= 0o777 :
            #Si ruta es valida
            if os.path.exists(tokens[0]) :
                #se cambian de forma recurisva los directorios y archivos de la carpeta raiz
                for root, dirs, files in os.walk(tokens[0]):
                    for d in dirs:
                        os.chmod(os.path.join(root, d), a)
                    for f in files:
                        os.chmod(os.path.join(root, f), a)
                return 0
            else :
                #mensaje si la ruta no es valida
                print("Ruta invalida")
                return 1
        else:
            #mensaje de error si el numero no esta en rango, o lo que se paso no es un numero
            print("Por favor ingrese un numero en octal entre 000 y 777")
            return 1
    elif len(tokens) == 3:
        #mensaje de error si el 3er parametro de chmod no es "-r"
        printf("No se reconoce el parametro: "+tokens[2])
    return 0
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
    Funcion mkdir
        Crea el directorio o jerarquia de directorios cuyo path es pasado como parametro
'''
def mkdir(tokens):
    #Intenta crear la jerarquia o el directorio
    try:
        os.makedirs(tokens)
    #mensaje de error en caso de que no se pueda
    except IOError:
        print(tokens+" ya existe o no es una ruta valida")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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
