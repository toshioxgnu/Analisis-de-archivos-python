import Estricto
import Mediano
import Relajado
 


def main():
    N=int(input("Ingrese parametro de ordenado : "))
    if N==0:
        Estricto.estricto()
    if  N==1:
        Mediano.mediano()
    if N==2:
        Relajado.relajado()

main()
