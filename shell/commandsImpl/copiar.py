def copiar(a,b):
    a=open(a,"r")
    b=open(b,"w")
    b.write(a.read())
    a.close()
    b.close()
