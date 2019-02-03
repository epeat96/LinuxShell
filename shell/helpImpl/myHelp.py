#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def cp():
    print("Uso:")
    print("cp [ruta archivo a copiar] [ruta donde se va a copiar]")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def mv():
    print("Uso:")
    print("mv [ruta archivo a copiar] [ruta donde se va a mover]")
    print("OBS: \nPara renombrar un archivo se puede utilizar la funcion mover, colocando la misma ruta pero con nombres de archivo diferentes")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def cd():
	print("Uso:")
	print("cd [ruta directorio]")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def passwd():
	print("Uso:")
	print("passwd [nombre de usuario]")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def ls():
	print("Uso:")
	print("ls [directorio](opcional)")
	print("OBS: el directorio es opcional, en su defecto se lista el directorio actual")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def chown():
	print("Uso:")
	print("chown [ruta] [usuario] [grupo] [-r](opcional)")
	print("OBS: el parametro opcional -r sirve para cambiar el duenho de forma recursiva")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def chmod():
	print("Uso:")
	print("chmod [ruta] [octal 000 a 777] [-r](opcional)")
	print("OBS: el parametro opcional -r sirve para cambiar los permisos de forma recursiva")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def mkdir():
	print("Uso:")
	print("mkdir [ruta]")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def useradd():
	print("Uso:")
	print("useradd [usuario] [horario] [ip]")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def renombrar():
	print("Uso:")
	print("renombrar [ruta] [ruta ]")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
