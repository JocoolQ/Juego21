from random import sample

def creador_baraja():
    return sample([(x,y) for x in ['A',2,3,4,5,6,7,8,9,10,'J','Q','K'] for y in ['DIAMANTES','TREBOLES','PICAS','CORAZONES']], 52)    

def contar(mano):
    if(validar_as(mano) and contador(mano) <= 11):
        return contador(mano) + 10
    else:
        return contador(mano)

def contador(mano):
    if len(mano) == 0:
        return 0
    else:
        for carta in mano:
            if carta[0] in ['J','Q','K']:
                return contador(mano[1:]) + 10
            if carta[0] == 'A':
                return contador(mano[1:]) + 1
            else:
                return contador(mano[1:]) + carta[0]

def validar_as(mano):
    if mano == []:
        return False
    if mano[0][0] == 'A':
        return True
    return validar_as(mano[1:])


def juego_Casa(manoJ, manoC, mazo):
    print("La Casa tiene: " + str(manoC) + " (" + str(contar(manoC)) + " puntos)")
    
    if (contar(manoC) < contar(manoJ)):
        juego_Casa(manoJ, manoC + [mazo.pop()], mazo)
    
    elif (contar(manoC) >= contar(manoJ) and contar(manoC) <= 21):
        print("La Casa gana")

    else:
        print("¡Felicidades ha ganado!")

def repartir(manoJ, manoC, mazo):
    if (manoJ == [] and manoC == []):
        juego(manoJ + [mazo.pop()] + [mazo.pop()], manoC + [mazo.pop()] + [mazo.pop()], mazo)
    else:
        juego(manoJ + [mazo.pop()], manoC, mazo)

def juego(manoJ, manoC, mazo):
    if (manoJ != [] and manoC != []):
        print("Su mano: " + str(manoJ) + " (" + str(contar(manoJ)) + " puntos)")
        
        print("Casa: " + str(manoC[0]) + " ?")
      
    if (manoJ == [] and manoC == []):
        repartir(manoJ, manoC, mazo)
        
    elif contar(manoJ) > 21:
        print("Perdió, usted tiene: " + str(contar(manoJ)) + " puntos")
        
    elif (input("Desea continuar: (Digite N para no)") != 'N'):
        repartir(manoJ, manoC, mazo)

    elif contar(manoJ) <= 21:
        juego_Casa(manoJ, manoC, mazo)
        
juego([], [], creador_baraja())
