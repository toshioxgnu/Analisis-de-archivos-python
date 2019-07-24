#Funcion encargada de buscar los marcadores con el criterio
#RELAJADO de seleccion 
import Busca
import csv  
import math

def relajado():
    ct=0
    dif=0
    print("Etra")
    iguales1,iguales2=Busca.busca()
    with open('marcadores_seleccionados.txt','w') as f:
        for line in iguales1:
            ct=ct+1
            for line1 in iguales2:
                linea=("2"+"\t"+str(line[2])+"\t"+str(line[3])+"\t"+str(line1[2])+"\t"+str(line1[3])+"\t"+"optimo"+"\n")
                if (int(line[2])-int(line1[2])<=2):
                    if int(line[3])-int(line1[3])<=2:
                        linea=("2"+"\t"+str(line[2])+"\t"+str(line[3])+"\t"+str(line1[2])+"\t"+str(line1[3])+"\t"+"optimo"+"\n")
                        f.write(linea)
                        break       
                    else:
                        linea=("2"+"\t"+str(line[2])+"\t"+str(line[3])+"\t"+str(line1[2])+"\t"+str(line1[3])+"\t"+"NO"+"\n")
                        f.write(linea)
                    break    
                if (int(line[2])-int(line1[2])>=2):
                    linea=("2"+"\t"+str(line[2])+"\t"+str(line[3])+"\t"+str(line1[2])+"\t"+str(line1[3])+"\t"+"optimo"+"\n")
                    if int(line1[3])-int(line[3])<=2:
                        linea=("2"+"\t"+str(line[2])+"\t"+str(line[3])+"\t"+str(line1[2])+"\t"+str(line1[3])+"\t"+"optimo"+"\n")
                        f.write(linea)
                        break    
                else:
                    linea=("2"+"\t"+str(line[2])+"\t"+str(line[3])+"\t"+str(line1[2])+"\t"+str(line1[3])+"\t"+"NO"+"\n")
                    f.write(linea)
                    break    
                                  

                    
    with open('marcadores_seleccionados.txt','r') as f:
        print("Se encontraron ",ct," marcadores")
        for line in f:
            print (line)
    
