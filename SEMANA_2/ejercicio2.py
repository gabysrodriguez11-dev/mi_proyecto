def aprobado(notas):
    apr=[]
    cont=0
    for i in range(len(notas)):
        if cont %2!=0:
            print(i)
            if notas[i] >=3:
                apr.append(notas[i-1])
        cont +=1
    return apr

def main():
    lista= int(input("ingrese los estudiantes con su respectiva nota separandolos por espacio"))
    lista=lista.split( )
    notas=[]
    cont=0
    for i in lista:
        if cont %2 !=0:
            print(i)
            notas.append(i)