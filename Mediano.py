#Funcion encargada de buscar los marcadores con el criterio
#MEDIANO de seleccion 
import Busca
import csv  
import math

def mediano():
    ct=0
    iguales1,iguales2=Busca.busca()
    with open('marcadores_seleccionados.txt','w') as f:
        for line in iguales1:
            for line1 in iguales2:
                if (float(line[2])-float(line1[2])<=1):
                    #SI
                    if (float(line[3])-float(line1[3])<=1) :
                        if(float(line[3])-float(line1[3])<=2):
                            linea=("1"+"\t"+str(line[2])+"\t"+str(line[3])+"\t"+str(line1[2])+"\t"+str(line1[3])+"\t"+"optimo"+"\n")
                            f.write(linea)
                           
                    #NO    
                    else:
                        linea=("1"+"\t"+str(line[2])+"\t"+str(line[3])+"\t"+str(line1[2])+"\t"+str(line1[3])+"\t"+"NO"+"\n")
                        f.write(linea)
                      
                if (float(line[2])-float(line1[2])>=1):
                    #SI                   
                    if(float(line1[3])-float(line[3])<=1):
                        if(float(line[3]-float(line1[3])>=2): 
                            linea=("1"+"\t"+str(line[2])+"\t"+str(line[3])+"\t"+str(line1[2])+"\t"+str(line1[3])+"\t"+"optimo"+"\n")
                            f.write(linea)
                    #NO    
                    else:
                        linea=("1"+"\t"+str(line[2])+"\t"+str(line[3])+"\t"+str(line1[2])+"\t"+str(line1[3])+"\t"+"NO"+"\n")
                        f.write(linea)
                        break

                                                
                                  

                    
    with open('marcadores_seleccionados.txt','r') as f:
        print("Se encontraron ",ct," marcadores")
        for line in f:
            print (line)
    
