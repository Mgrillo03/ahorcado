import random
import os
import time
from threading import Thread


def clear_screan():
    ##Limpiar la consola
    os.system('clear')

def base(lista):
    if lista == [] :
        filas = []
        for i in range(40):
            for j in range(40):
                filas.append(' ')
            lista.append(filas)
            filas= []
        #filas = []
        auz1 = []
        for i in range(40):
            #filas.append('=')
            auz1.append('=')
        lista[0]= list(auz1)
        #lista[1] = filas
        lista[31] = auz1
        lista[31][15] = '@'
        lista[31][25] = ' '
        for i in range(31,40):
            lista[i][39] = '|'
            lista[i][38] = '|'
        for i in range(40):
            
            lista[i][0]='|'
            lista[i][1]='|'
        return lista
    else:
        return lista

def cuerda(lista):
    for i in range(1,14):
        lista[i][20]='|'
    return lista

def cara(lista):
    lista[14][18]='_'
    lista[14][19]='_'
    lista[14][20]='_'
    lista[14][21]='_'
    lista[14][22]='_'

    lista[16][16]='|'
    lista[17][16]='|'
    #lista[16][19]= 'X'
    #lista[16][22]= 'X'

    lista[16][24]='|'
    lista[17][24]='|'

    lista[18][17] = '\\'
    lista[18][23] = '/'
    
    lista[18][20] ='_'
    lista[18][21] ='_'
    lista[18][19] ='_'
    return lista

def cuerpo(lista):
    for i in range(19,29):
        lista[i][20] = '|'
    return lista

def brazo_izq(lista):
    lista[22][21]='\\'
    lista[23][23]='\\'
    return lista

def brazo_der(lista):
    lista[22][19]='/'
    lista[23][17]='/'
    return lista

def pierna_izq(lista):
    lista[29][21]='\\'
    lista[30][23]='\\'
    return lista

def pierna_der(lista):
    lista[29][19]='/'
    lista[30][17]='/'
    return lista

def borrado_cara(lista):
    lista[14][18]=' '
    lista[14][19]=' '
    lista[14][20]=' '
    lista[14][21]=' '
    lista[14][22]=' '

    lista[16][16]=' '
    lista[17][16]=' '
    #lista[16][19]= 'X'
    #lista[16][22]= 'X'

    lista[16][24]=' '
    lista[17][24]=' '

    lista[18][17] = ' '
    lista[18][23] = ' '
    
    lista[18][20] =' '
    lista[18][21] =' '
    lista[18][19] =' '

    #Borrado Brazos
    lista[22][21]=' '
    lista[23][23]=' '
    lista[22][19]=' '
    lista[23][17]=' '

    #Borrado Piernas
    lista[29][21]=' '
    lista[30][23]=' '
    lista[29][19]=' '
    lista[30][17]=' '


    return lista

def caida(lista):
    for i in range(15,25):
        lista[31][i] = ' '

    for i in range(19,29):
        lista[i][20] = ' '

    lista = borrado_cara(lista)
    lista[21][18]='_'
    lista[21][19]='_'
    lista[21][20]='_'
    lista[21][21]='_'
    lista[21][22]='_'

    lista[23][16]='|'
    lista[24][16]='|'
    lista[23][19]= 'X'
    lista[23][22]= 'X'

    lista[23][24]='|'
    lista[24][24]='|'

    lista[25][17] = '\\'
    lista[25][23] = '/'
    
    lista[25][20] ='_'
    lista[25][21] ='_'
    lista[25][19] ='_'

    for i in range(1,21):
        lista[i][20]='|'

    
    for i in range(26,36):
        lista[i][20] = '|'

    #Brazos y piernas
    lista[29][21]='\\'
    lista[30][23]='\\'
    lista[29][19]='/'
    lista[30][17]='/'

    lista[36][21]='\\'
    lista[37][23]='\\'
    lista[36][19]='/'
    lista[37][17]='/'
    
    return lista

def imprimir_lista(lista):
    #clear_screan()
    for i in lista:
        for j in i:
            print(j, end= "")
        print()

def dibujar(lista,n):

    if n == 0 :
        return base(lista) 
    elif n == 1:
        return cuerda(lista)
    elif n == 2:
        return cara(lista)
    elif n == 3:
        return cuerpo(lista)
    elif n == 4:
        return brazo_der(lista)
    elif n == 5:
        return brazo_izq(lista)
    elif n == 6: 
        return pierna_der(lista)
    elif n == 7:
        return pierna_izq(lista)
    elif n == 8:
        return caida(lista)
    
def space(n):
    print('\n'*n)

def select_random(words):
    #elegir una palabra random del archivo para jugar
    return random.choice(words)[:-1]

def read_file():
    #Leer los archivos y escribirlos en el la lista words
    words = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line)
    return words

def empty_spaces(word):
    #Guiones del largo de la palabra
    return '_ '*len(word)

def separate_line(n):
    pass
    ##for i in range(n):
    #    print("*****************************************************************")

def print_state(word_hide, letter_used, error, lista):
    clear_screan()
    print('LA PALABRA TIENE ',int(len(word_hide)/2),' LETRAS \n SI TE EQUIVOCAS 8 VECES PIERDES \n ¡¡¡SUERTEE!!!')
    space(2)
    lista = dibujar(lista, error)
    imprimir_lista(lista)
    space(2)
    print(word_hide)
    space(3)
    print('Te has equivocado: ',error,' veces, te quedan: ',8-error, 'oportunidades')
    if letter_used == []:
        print('Letras usadas : [ninguna hasta ahora]')
    else:
        print('Letras usadas: ', letter_used)
    space(2)

def print_error():
    clear_screan()
    space(2)
    separate_line(2)
    space(2)
    print("ERRORRRRRR \n LA LETRA NO ESTA EN LA PALABRA \n PONELE ONDA!!!!")
    time.sleep(2)

def print_success():
    clear_screan()
    space(2)
    separate_line(2)
    space(2)
    print("VAMOOOO WACHO ¡ASI SE HACE!")
    time.sleep(2)
    #input('oprime enter letra para continuar')

def win():
    clear_screan()
    separate_line(5)
    space(3)
    print("¡¡¡¡GANASTEEE!!!! \n ERES TU MENOOORRRRR \n TUTUTUTUTUTUTUTUTUTUTUTU")
    space(3)
    separate_line(5)
    time.sleep(3)
    #input()

def loose(word, lista):
    clear_screan()
    #separate_line(5)
    #space(3)
    print("¡¡¡¡BUUUUUUUUUUU!!!! \n ERES UN PERDEDOOOOOOORR \n PERDEEDOOOOOOOOOOOOOOR")
    print('LA PALABRA ERA ',word)
    lista = dibujar(lista, 8)
    imprimir_lista(lista)

    #space(3)
    #separate_line(5)
    #time.sleep(3)
    input()

def play_again():
    while True:
        clear_screan()
        separate_line(5)
        space(3)
        ans = input("¿QUERES JUGAR DE NUEVO? (y/n): ")
        space(3)
        separate_line(5)
        ans = ans.upper()
        if ans == 'Y':
            return True
        elif ans == 'N':
            return False
        else:
            print('INGRESA SOLO UNA DE LAS DOS OPCIONESS')
            
def good_bye():
    clear_screan()
    separate_line(5)
    space(3)
    print("                          CHAITO")
    space(3)
    separate_line(5)
    time.sleep(3)

def hello():
    while True:
        clear_screan()
        space(5)
        ans = input('Quieres Juagar al Ahorcado? (y/n) ')
        ans = ans.upper()
        if ans == 'Y' :
            return True
        elif ans == 'N':
            return False
        else:
            print('Te Pregunte SI o NO')
            time.sleep(2)

def read_input(word_hide, used_letter, error, lista):
    #Leer letra del usuario
    while True:
        print_state(word_hide,used_letter, error, lista)
        letter = input('Ingresa una letra  :')
        letter = letter.upper()
        if len(letter) == 1 and letter.isalpha() and not letter in used_letter:
            return letter
        else:
            print('Solo puedes ingresar una letra entre la A y la Z, intenta de nuevo')
            time.sleep(2)

def verify(guess, word):
    if guess in word:
        print_success()
        return True        
    else: 
        print_error()
        return False

def run():
    play = hello()

    while play : 
        #Crear lista de posibles palabras
        words = read_file()
        #seleccionar palabra random
        word = select_random(words)
        word = word.upper()
        #Crear palabra oculta
        word_hide = empty_spaces(word)
        #Lista de letras usadas    
        used_letter = []
        lista = []
        game = True
        error = 0
        good = 0
        gold = len(word)
        #Clico de juego
        while game:
            #leer intento
            guess = read_input(word_hide, used_letter, error, lista)
            #agregar a la lista de letras usadas
            used_letter.append(guess)
            #comprobar letra
            attempt = verify(guess, word)
            if attempt :
                for i in range(len(word)):
                    if word[i]   == guess: 
                        word_hide = word_hide[:i*2] + guess + word_hide[i*2+1:]
                    
                        good += 1
            else:
                error += 1
            if good >= gold :
                win()
                game = 0
                play = play_again()
            if error >= 8:
                play = loose(word, lista)
                game = 0
                play = play_again()


    
    #empezar juego
        #Mostrar palabra oculta (_ _ _ _ _)
        #Pedir letra (comprobar char alfabetico)
        #comprobar letra en la palabra   
        #   (NO) contar un error y pedir otra letra 
        #   (SI) mostrar en la palabra oculta y pedir otra letra
        #comprobar si gano o perdio
        #mostrar resultado
        #preguntar si quiere jugar otra partida o quiere salir

    '''print(word)
    print(len(word), len(word_hide))
    print(empty_spaces(word))'''
    good_bye()
    

if __name__ == '__main__':
    run()