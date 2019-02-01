#!/usr/bin/env python
from cmd import Cmd
import os
import optparse
import shutil
from helpImpl import myHelp
from commandsImpl import service
import subprocess as sub
class MyPrompt(Cmd):
	ruler='+'
	doc_header="Los siguientes comandos estan documentados, para verlos ejecute: help <comando>"
	misc_header="Documentacion de ayuda miscelanea"
	undoc_header="Los siguientes comandos no estan documentados:"
	prompt="#: "
	intro="Para instrucciones ejecute: help"
	os.system("clear")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	def do_cd(self,inp):
		inp = inp.split()
		#si la cantidad de parametros es correcta
		if service.lenctrl(inp,1):
			service.cd(inp)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	def help_cp(self):
		myHelp.copiar()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	def help_mv(self):
		myHelp.mover()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	def do_passwd(self,inp):
		tokens = inp.split()
		#si la cantidad de parametros es correcta
		if service.lenctrl(tokens,1):
			os.system("passwd "+inp)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	def do_ls(self,inp):
		if inp == "":
			b=os.listdir(os.getcwd())
			for a in b:
				print(a,end=" ")
			print("")
		else:
			tokens = inp.split()
			if service.lenctrl(tokens,1):
				service.ls(tokens)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	def do_chown(self,inp):
		tokens = inp.split()
		if len(tokens)==4 :
			service.chown(tokens)
		elif service.lenctrl(tokens,3):
			service.chown(tokens)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	'''
		Funcion EOF
		Al llamar a esta funcion se deja de ejecutar la shell y retorna True
	'''
	def do_EOF(self,inp):
		print("\nAdios\n")
		return True
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	'''
	Funcion cp
	Recibe como parametros las rutas de un archivo a copiar y la ruta donde este sera copiado
	'''
	def do_cp(self, inp):
		tokens = inp.split()
		#si la cantidad de parametros es correcta
		if service.lenctrl(tokens,2):
			#se intenta copiar
			service.copiar(tokens[0],tokens[1])
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	'''
	Funcion mv
	Recibe como parametros las rutas de un archivo a mover y la ruta donde este sera movido, tambien se puede usar
	para renombrar archivos
	'''
	def do_mv(self, inp):
		tokens = inp.split()
		#si la cantidad de parametros es correcta
		if service.lenctrl(tokens,2):
			#si se pudo copiar
			if service.copiar(tokens[0],tokens[1]) == 0:
				shutil.rmtree(tokens[0])
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	'''
	Funcion renombrar
	Recibe com parametros la ruta de un archivo y el nombre con el cual este se quiere do_renombrar
	'''
	def do_renombrar(self, inp):
		tokens = inp.split()
		#si la cantidad de parametros es correcta
		if service.lenctrl(tokens,2):
			service.rn(tokens)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	'''
	Funcion chmod
	Recibe como parametros la ruta de un archivo, un numero en octal entre 000 y 777
	y un parametro que puede ser "-r" y cambia los permisos del archivo, directorio, o arbol
	de directorios dependiendo de si se paso el parametro -r o no
	'''
	def do_chmod(self,inp):
		tokens = inp.split()
		#si la cantidad de parametros es correcta
		if len(tokens)==3 :
			service.chmod(tokens)
		elif service.lenctrl(tokens,2):
			service.chmod(tokens)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	'''
	Funcion mkdir
	Recibe como parametro una ruta y crea un directorio
	'''
	def do_mkdir(self,inp):
		tokens = inp.split()
		if service.lenctrl(tokens,1):
			service.mkdir(tokens[0])
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	def do_salir(self,inp):
		print("Adios")
		return True;
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	def emptyline(self):
		pass
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	def default(self,inp):
		try:
			sub.run(inp,shell=True,executable="/bin/bash")
		except :
			print("No se conoce el comando: "+inp)
#loop principal de la shell
MyPrompt().cmdloop()
