import sys
import math
#se lee solo un caracter sin echo
def getChar():
    # figure out which function to use once, and store it in _func
    if "_func" not in getChar.__dict__:
        try:
            # for Windows-based systems
            import msvcrt # If successful, we are on Windows
            getChar._func=msvcrt.getch

        except ImportError:
            # for POSIX-based systems (with termios & tty support)
            import tty, sys, termios # raises ImportError if unsupported

            def _ttyRead():
                fd = sys.stdin.fileno()
                oldSettings = termios.tcgetattr(fd)

                try:
                    tty.setcbreak(fd)
                    answer = sys.stdin.read(1)
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, oldSettings)

                return answer

            getChar._func=_ttyRead

    return getChar._func()
def convertirnumero_list(numero) :

    mi_lista = []
    for x in str(numero) :
        mi_lista.append(x)
    if mi_lista.count("E") == 1:
        for i in range(0,3) :
            mi_lista.pop(len(mi_lista)-2)
    return mi_lista
#funcion que lee caracter por caracter y regresa una lista con estos
def leer_milista() :
    self = []
    answer = "x"
    while answer != "\n" :
        answer = getChar()
        if answer != "\n" :
            sys.stdout.write(answer)
            self.append( answer )
    print

    if self.count(".") > 0 :
        if self.count('0') == len(self) - 1:
            self = [0,0]
    else :
        if self.count('0') == len(self):
            self = [0,0]
    return self

#funcion que imprime una lista como string
def print_milista( list1 ) :
    list_aux = []
    for i in list1:
        string = str(i)
        list_aux.append(string)
    print "".join(list_aux)

def convert_binario(list2) :
    list_original = []
    binario_entero = []
    binario_decimal = []
    binario_flag = 0
    contador = 0
    signo = 0
    #verifico si es decimal
    if list2.count(".") == 1 :
        binario_flag = list2.index(".")
    else :
        binario_flag = len(list2)
    #verifico si es negativo
    if list2[0] == "-" :
        list2[0] = 0
        signo = 1
    #convierto a entero la lista
    for i in list2 :
        if i == "." :
            list_original.append(i)
        else :
            entero = int(i)
            list_original.append(entero)


    while  list_original.count(0) != len(list_original) and contador < 100:
            contador += 1

            for i in range( 0, binario_flag) :
                if i == binario_flag -1 :
                    if len(binario_entero) != 0:
                        if list_original[0:binario_flag ] != [0] :
                            binario_entero.append(list_original[i]%2)
                    else :
                            binario_entero.append(list_original[i]%2)

                    list_original[i] /=2
                else :
                    list_original[i+1] += (list_original[i]%2)*10
                    list_original[i] = list_original[i]/2

            if list2.count(".") == 1 :
                for i in range( binario_flag + 1, len(list_original)) :
                    list_original[i] *= 2
                for i in range( binario_flag + 1, len(list_original)) :
                    if i == binario_flag + 1 :
                         binario_decimal.append(list_original[i]/10)
                         list_original[i] %= 10
                    else :
                        list_original[i - 1] +=  list_original[i]/10
                        list_original[i] %=10
                    list_original[binario_flag] = 0
    #antes de escribir el binario agregamos el signo
    if list2[0] == 0 and signo == 1:
        binario_entero.append("-")
    binario_entero.reverse()
    k = 0
    while binario_entero[k] == 0 and len(binario_entero) != 1 :
        binario_entero.pop(k)

    if list2.count(".") == 1 :
        binario_entero.append(".")
        binario_entero.extend(binario_decimal)

    return binario_entero

def convertbinario_numero(list_x) :
    list_binario = []
    for m in range( 0, len(list_x)) :
        list_binario.append(list_x[m])
    numero_entero = 0
    numero_decimal = 0
    signo = 0
    if list_binario.count("-") > 0 :
        signo = 1
        list_binario.pop(0)
    if list_binario.count(".") > 0 :
        for i in range( list_binario.index(".") + 1, len(list_binario)) :
            numero_decimal += list_binario[i] * 2**( (-1)*(i -list_binario.index(".") ))
        for i in range( list_binario.index(".") - 1, -1,-1 ) :
            numero_entero += (int)(list_binario[i] * 2**( list_binario.index(".") - 1 - i))
    else :
        for i in range( len(list_binario)- 1, -1,-1 ) :
            numero_entero += (int)(list_binario[i]) * 2**( len(list_binario)- 1 - i)
    numero_entero += numero_decimal
    if signo == 1 :
        numero_entero*=(-1)
    return numero_entero
