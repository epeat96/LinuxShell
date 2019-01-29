from cmd import Cmd
import os
import optparse
import shutil
from helpImpl import myHelp
from commandsImpl import service
class MyPrompt(Cmd):
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def help_copiar(self):
        myHelp.copiar()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    '''
    Funcion copiar
    Recibe como parametros las rutas de un archivo a copiar y la ruta donde este sera copiado
    '''
    def do_copiar(self, inp):
        tokens = inp.split()
        #si la cantidad de parametros es correcta
        if service.lenctrl(tokens,2):
            #se intenta copiar
            service.copiar(tokens[0],tokens[1])
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    '''
    Funcion mover
    Recibe como parametros las rutas de un archivo a mover y la ruta donde este sera movido, tambien se puede usar
    para renombrar archivos
    '''
    def do_mover(self, inp):
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

MyPrompt().cmdloop()
print("after")
