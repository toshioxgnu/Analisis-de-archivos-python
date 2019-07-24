#Funcion encargada de buscar los marcadores con el criterio
#ESTRICTO de seleccion 


import Busca
import csv

def estricto():
    ct=0
    iguales1,iguales2=Busca.busca()
    with open('marcadores_seleccionados.txt','w') as f:
        for line in iguales1:
            for line1 in iguales2:
                if int(line[2]) == int(line1[2]) or int(line[3])== int(line1[3]):
                    ct=ct+1
                    linea=("0"+"\t"+str(line[2])+"\t"+str(line[3])+"\t"+str(line1[2])+"\t"+str(line1[3])+"\t"+"optimo"+"\n")
            f.writelines(linea)                     
                    
    with open('marcadores_seleccionados.txt','r') as f:
        print("Se encontraron ",ct," marcadores")
        for line in f:
            print (line)
    
    
