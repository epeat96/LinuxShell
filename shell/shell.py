from cmd import Cmd
import os
import optparse
from helpImpl import myHelp
from commandsImpl import service
class MyPrompt(Cmd):
    def help_copiar(self):
        myHelp.copiar()
''' Funcion copiar
        Recibe como parametros las rutas de un archivo a copiar y la ruta donde este sera copiado
'''
    def do_copiar(self, inp):
        tokens = inp.split()
        if len(tokens)>2:
            print("No se reconocen los siguientes parametros:")
            for x in range(2, len(tokens)):
                print(tokens[x])
        else:
            copiar.copiar(tokens[0],tokens[1])
'''
    Funcion mover
        Recibe como paramtetros las rutas de un archivo a mover y la ruta donde este sera movido, tambien se puede usar
        para renombrar archivos
'''
    def do_mover(self, inp):
        tokens = inp.split()
        if len(tokens)>2:
            print("No se reconocen los siguientes parametros:")
            for x in range(2, len(tokens)):
                print(tokens[x])
        else:
            serice.copiar(tokens[0],tokens[1])
            os.remove(tokens[0])
#+++++++++++++++++++++++++++++++++++++++
    def do_hola(self, inp):
        print("holamundo")
#++++++++++++++++++++++++++++++++++++++
    def do_exit(self, inp):
        print("Bye")
        return True
#+++++++++++++++++++++++++++++++++++++++++++
    def do_add(self, inp):
        print("Adding '{}'".format(inp))

MyPrompt().cmdloop()
print("after")
