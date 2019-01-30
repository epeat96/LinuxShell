from cmd import Cmd
import os
import optparse
import shutil
from helpImpl import myHelp
from commandsImpl import service
class MyPrompt(Cmd):
    ruler='+'
    doc_header="Los siguientes comandos estan documentados, para verlos ejecute: help: <comando>"
    misc_header="Documentacion de ayuda miscelanea"
    undoc_header="Los siguientes comandos no estan documentados:"
    prompt="#"
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def help_cp(self):
        myHelp.copiar()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def help_mover(self):
        myHelp.mover()
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
    def do_rn(self, inp):
        tokens = inp.split()

MyPrompt().cmdloop()
print("after")
