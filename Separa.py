# Esta funcion separa los archivos de texto en arreglos bidimensionales
# para que sea mas facil trabajar variables independientes


import csv
def separa():
    with open('uno_test.txt') as f, open('dos_test.txt','r') as f1:
        reader=csv.reader(f,delimiter='\t')
        reader2=csv.reader(f1,delimiter='\t')
        d=list(reader)
        d1=list(reader2)
        return d,d1
