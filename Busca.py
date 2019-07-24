# Busca todas las lineas iguales en ambos archivos y envia dos listas 
# a la siguiente funcion 

import Separa
import csv

def busca():
    list1,list2=Separa.separa()
    file_equals=[]
    file_equals1=[]
    for line in list1:
        for line1 in list2:
            if line[0]==line1[0] and line[1]==line1[1]:
                file_equals.append(line)
                file_equals1.append(line1)
                # ct=ct+1
    return file_equals,file_equals1

