from random import sample

def contar(lista):
    if(len(lista)<=0):
        return 0
    if(contador(lista)>11):
        return contador(lista)
    else:
        for i in lista:
            if i[0] == 'J' or  i[0] == 'K' or  i[0] == 'Q':
                return 10+contar(lista[1:])
            elif i[0] == 'A':            
                return contador(lista)+10
            else:
                return i[0]+contar(lista[1:])

def contador(lista):
    if(len(lista)==0):
        return 0
    else:
        for i in lista:
            if(i[0]=='J' or i[0]=='Q' or i[0]=='K'):
                return contador(lista[1:])+10
            if(i[0]=='A'):
                return contador(lista[1:])+1
            else:
                return contador(lista[1:])+i[0]

def creadorbaraja():
    return sample([(x,y)for x in ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']for y in ['DIAMANTES','TREBOLES','PICAS','CORAZONES']], 52)    

def juego(listaJ, listaC, lista):
    print(listaJ)
    if(len(listaJ)==0 and len(listaC)==0):
        repartirIni(listaJ, listaC, lista)
        return "Fin del Juego"
    elif(input("Desa continuar: (Digite N para no)")!='N'):
        print("Casa "+str(listaC[0])+" ?")
        if(contar(listaJ)<=21):
            return repartirIni(listaJ,listaC,lista)
        else:
            return print("Perdio usted tiene: "+str(contar(listaJ)))
    elif(contar(listaJ)>21):
        return print("Perdio usted tiene: "+str(contar(listaJ)))
    elif(contar(listaJ)<=21):
        print("Tiene: "+str(contar(listaJ)))
        return juegoCasa(listaJ,listaC,lista)
        
def juegoCasa(listaJ,listaC,lista):
    print("La Casa tiene"+str(listaC))
    if(contar(listaC)<contar(listaJ)):
        return repartirIni2(listaJ,listaC,lista)
    elif(contar(listaC)>=contar(listaJ) and contar(listaC)<=21):
        return print("La Casa Gana")
    else:
        return print("Felicidades Ganaste, ¡Exitos!")


def repartirIni(listaJ, listaC, lista):
    if (len(lista)==52):
        return juego(listaJ+[lista[0]]+[lista[1]],listaC+[lista[2]]+[lista[3]],lista[4:])
    else:
        return juego(listaJ+[lista[0]],listaC,lista[1:])

def repartirIni2(listaJ, listaC, lista):
    return juegoCasa(listaJ,listaC+[lista[0]],lista[1:])

juego([],[],creadorbaraja())
