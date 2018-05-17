import sys
import lib_nooblinux
from decimal import Decimal, localcontext

def my_sub(list_a_1, list_b_1, base, decimal) :
    list_a = []
    list_b = []
    for m in range(0, len(list_a_1)) :
        list_a.append(list_a_1[m])
    for m in range(0, len(list_b_1)) :
        list_b.append(list_b_1[m])
    list_a_entero = []
    list_b_entero = []
    list_a_decimal = []
    list_b_decimal = []
    list_z_decimal = []
    list_aux = []
    #por defecto list_z es entera
    list_z = []
    flag_decimal  = 0
    #signo por defecto es positivo(0)
    signo = 0
    change = 0
    #indica si se ah cambiado a por b
    #se analizan los signos
    if list_a.count("-") == 1 or list_b.count("-") == 1 :
        if list_a.count("-") == 1 and list_b.count("-") == 1 :
                signo = 1
                list_a.pop(0)
                list_b.pop(0)
        elif list_a.count("-") == 1 and list_b.count("-") == 0 :
            list_a.pop(0)
            list_z = my_add(list_a,list_b,base,0)
            list_z.insert(0,"-")
            return list_z
        elif list_a.count("-") == 0 and list_b.count("-") == 1 :
            list_b.pop(0)
            list_z = my_add(list_a,list_b,base,0)
            return list_z
    #se analiza el caso de signos diferentes
    #se analiza si tienen parte decimal
    if list_a.count(".") == 1 or list_b.count(".") == 1:
        #se sumaran enteros
        flag_decimal = 1
        if list_a.count(".") == 1 :
            for i in range( 0 , list_a.index(".")) :
                list_a_entero.append(list_a[i])
            for i in range(list_a.index(".")+1, len(list_a)) :
                list_a_decimal.append(list_a[i])
        else :
                list_a_entero = list_a

        if list_b.count(".") == 1 :
            for i in range( 0 , list_b.index(".")) :
                list_b_entero.append(list_b[i])
            for i in range(list_b.index(".")+1, len(list_b)) :
                list_b_decimal.append(list_b[i])
        else :
                list_b_entero = list_b

        if len(list_a_decimal) > len(list_b_decimal) :
            for i in range( len(list_b_decimal) , len(list_a_decimal)) :
                list_b_decimal.append('0')
        else :
            for i in range( len(list_a_decimal) , len(list_b_decimal)) :
                list_a_decimal.append('0')
        if len(list_a_entero) > len(list_b_entero) :
            for i in range( len(list_b_entero) , len(list_a_entero)) :
                list_b_entero.insert(0,'0')
        else :
            for i in range( len(list_a_entero) , len(list_b_entero)) :
                list_a_entero.insert(0,'0')
#se calcula la substraccion de la parte decimal
        i = 0
        for i in range(0, len(list_a_entero)) :
            if int(list_a_entero[i]) - int(list_b_entero[i]) < 0 :
                list_temp = list_a_entero
                list_a_entero = list_b_entero
                list_b_entero = list_temp
                list_temp = list_a_decimal
                list_a_decimal = list_b_decimal
                list_b_decimal = list_temp
                change = 1
                break
            if int(list_a_entero[i]) - int(list_b_entero[i]) > 0 :
                break
        if i == len(list_a_entero) -1 :
            for j in range(0, len(list_a_decimal)) :
                if int(list_a_decimal[i]) - int(list_b_decimal[i]) < 0 :
                    list_temp = list_a_entero
                    list_a_entero = list_b_entero
                    list_b_entero = list_temp
                    list_temp = list_a_decimal
                    list_a_decimal = list_b_decimal
                    list_b_decimal = list_temp
                    change = 1
                    break
                if int(list_a_decimal[i]) - int(list_b_decimal[i]) > 0 :
                    break
        list_z_decimal = my_sub(list_a_decimal,list_b_decimal,base, 1)
    else :
        list_a_entero = list_a
        list_b_entero = list_b
        if decimal != 1 :
            if len(list_a_entero) > len(list_b_entero) :
                for i in range( len(list_b_entero) , len(list_a_entero)) :
                    list_b_entero.insert(0,'0')
            else :
                for i in range( len(list_a_entero) , len(list_b_entero)) :
                    list_a_entero.insert(0,'0')
            for i in range(0, len(list_a_entero)) :
                if int(list_a_entero[i]) - int(list_b_entero[i]) < 0 :
                    list_temp = list_a_entero
                    list_a_entero = list_b_entero
                    list_b_entero = list_temp
                    list_temp = list_a_decimal
                    list_a_decimal = list_b_decimal
                    list_b_decimal = list_temp
                    change = 1
                    break
                if int(list_a_entero[i]) - int(list_b_entero[i]) > 0 :
                    break

    borrow = 0
    i = 0
    j = 0
    #nos aseguramos que  a  es mayor siempre

        #si b en un caso e smyor hay que aginar el signo al ultimo
    #La lista  donde quedara el resultado debe ser de tamano 1 mas que la lista a
    if decimal == 0 :
        for k in range (0,len(list_a_entero)+1) :
            list_z.append(0)
    elif decimal == 1 :
        for k in range (0,len(list_a_entero)) :
            list_z.append(0)
    #se recorre desde la ultima posicion de b hasta el final de b
    for i in range( len(list_b_entero) -1, -1, -1) :
        borrow += (int(list_a_entero[i]) - int(list_b_entero[i]))
        #substraccion en una base dada
        if borrow < 0 :

            aux = borrow
            borrow  = borrow + base
            list_a_entero[ i - 1 ] = int(list_a_entero[ i - 1 ])-1
        if decimal == 0:
            list_z[i+1 ] += borrow
        elif decimal == 1:
            list_z[i] += borrow
        borrow *= 0
    borrow *=0
    #se comienza donde quedo i hasta el final de la lista a
    #se eliminan los 0 a la izquierda auiq me quedo+
    k = 0

    while list_z[k] == 0 and len(list_z) != 1 and decimal != 1 :
        list_z.pop(k)


    #eliminamos posibles numeros menores  a cero
    if len(list_z_decimal) != 0 :
        if list_z_decimal[0] < 0 :
            list_residuo = []
            list_residuo.append(abs(int(list_z_decimal[0])))
            list_z = my_sub(list_z, list_residuo,base,0)
            list_z_decimal.pop(0)
        list_z_decimal.insert(0,".")

    if list_z[0] < 0 and decimal != 1:
        list_z[0] = abs(list_z[0])
        list_z.insert(0,"-")

    if change == 1 :
        if list_z[0] == "-" :
            list_z.pop(0)
        else :
            list_z.insert(0,"-")

    list_z.extend(list_z_decimal)
    k = 0

    return list_z

#la suma acepta dos listas , la base en que se sumara y un valor por defecto 0 si se suman entero o 1 si la suma viene de decimales
def my_add( list_a_1, list_b_1, base, decimal) :
    #listas a usar
    list_a = []
    list_b = []
    for m in range(0, len(list_a_1)) :
        list_a.append(list_a_1[m])
    for m in range(0, len(list_b_1)) :
        list_b.append(list_b_1[m])
    list_a_entero = []
    list_b_entero = []
    list_a_decimal = []
    list_b_decimal = []
    list_z_decimal = []
    list_aux = []
    #por defecto list_z es entera
    list_z = []
    flag_decimal  = 0
    #signo por defecto es positivo(0)
    signo = 0
    #se analizan los signos

    if list_a.count('-') == 1 or list_b.count('-') == 1 :
        if list_a.count("-") == 1 and list_b.count("-") == 1 :
                signo = 1
                list_a.pop(0)
                list_b.pop(0)
        elif (list_a.count("-") == 1 and list_b.count("-") == 0) or (list_a.count("-") == 0 and list_b.count("-") == 1)  :
            if list_a.count("-") == 1 :
                list_a.pop(0)
                list_z = my_sub(list_b, list_a, base, 0)
                return list_z
            if list_b.count("-") == 1 :
                list_b.pop(0)
                return my_sub(list_a,list_b,base,0)

    #se analiza si tienen parte decimal
    if list_a.count(".") == 1 or list_b.count(".") == 1:
        #se sumaran enteros
        flag_decimal = 1
        if list_a.count(".") == 1 :
            for i in range( 0 , list_a.index(".")) :
                list_a_entero.append(list_a[i])
            for i in range(list_a.index(".")+1, len(list_a)) :
                list_a_decimal.append(list_a[i])
        else :
                list_a_entero = list_a
        if list_b.count(".") == 1 :
            for i in range( 0 , list_b.index(".")) :
                list_b_entero.append(list_b[i])
            for i in range(list_b.index(".")+1, len(list_b)) :
                list_b_decimal.append(list_b[i])
        else :
                list_b_entero = list_b
        if len(list_a_decimal) > len(list_b_decimal) :
            for i in range( len(list_b_decimal) , len(list_a_decimal)) :
                list_b_decimal.append('0')
        else :
            for i in range( len(list_a_decimal) , len(list_b_decimal)) :
                list_a_decimal.append('0')
        #se calcula la suma de la parte decimal
        list_z_decimal = my_add(list_a_decimal,list_b_decimal,base, 1)
    else :
        list_a_entero = list_a
        list_b_entero = list_b

    carry = 0
    i = 0
    j = 0

    #nos aseguramos que  a  es mayor siempre
    if len(list_a_entero) < len( list_b_entero) :
        list_temp = list_a_entero
        list_a_entero = list_b_entero
        list_b_entero = list_temp
    #La lista  donde quedara el resultado debe ser de tamano 1 mas que la lista a
    for k in range( (len(list_a_entero) + 1)) :
        list_z.append(0)
    #se recorre desde la ultima posicion de b hasta el final de b
    for i in range( len(list_b_entero) -1, -1, -1) :
        carry += (int(list_a_entero[i+ ( len(list_a_entero) - len( list_b_entero))]) + int(list_b_entero[i]))
        #suma en una base dada
        if carry >= base :
            aux = carry%base
            list_z[ (i -1) + ( len(list_a_entero) + 1 - len( list_b_entero))] += carry/base
            carry = aux
        list_z[i+ ( len(list_a_entero) + 1 - len( list_b_entero))] += carry
        carry *= 0
    carry *=0
    #se comienza donde quedo i hasta el final de la lista a
    if i  <= 0 :
        for j in range(i+ ( len(list_a_entero) - len( list_b_entero) -1), -1, -1) :
            carry += int(list_a_entero[j])
            list_z[j+1] += carry
            if list_z[j+1] >= base :
                list_z[j] += list_z[j+1]/base
                list_z[j+1] = list_z[j+1]%base
            carry *= 0
    #se eliminan los 0 a la izquierda
    k = 0
    while list_z[k] == 0 and len(list_z) != 1 and decimal != 1:
        list_z.pop(k)
    #eliminamos posibles numeros mayores a la base
    for i in range( len(list_z)-1, -1, -1) :
        if list_z[i] >= base :
            if i == 0 :
                list_z.insert(0, list_z[0]/base)
                list_z[1] = list_z[1]%base
            else :
                list_z[i-1] += list_z[i]/base
                list_z[i] = list_z[i]%base
    #se une la parte entera con la decimal
    if flag_decimal != 0 :
        if len(list_z_decimal) != len(list_a_decimal) :
            list_aux.append(list_z_decimal[0])
            list_z_decimal.pop(0)
            list_z = my_add(list_z, list_aux, base, 0)
        list_z.append(".")
        list_z.extend(list_z_decimal)
    if signo == 1 :
        list_z.insert(0,"-")
    return list_z
def naive(x, y, base):
    total = [0]
    mux = 0
    aux = 0
    if len(x) != 0 and len(y) != 0 :
        mux += int(x[0])*int(y[0])
    elif len(x) == 0 :
        mux =0
    elif len(y) == 0 :
        mux = 0
    total[0] += mux
    i = 0
    while total[0] >= base :
        aux = total[i]/base
        total[i] = total[i]%base
        total.insert(0,aux)

    return total

def kara(x, y, base,recursion):
    #analizo el signo
    signo = 0
    if x.count("-") == 1 and y.count("-") == 1 :
        signo = 0
        x.pop(0)
        y.pop(0)
    elif x.count("-") == 1 and y.count("-") == 0 :
        signo = 1
        x.pop(0)
    elif x.count("-") == 0 and y.count("-") == 1 :
        signo = 1
        y.pop(0)

    #analizo el decimal y guardo los exponentes
    exponente_x = 0
    exponente_y = 0
    if x.count(".") > 0 :
        exponente_x = len(x) - x.index(".")
        x.pop( x.index("."))
    else :
        if recursion == 0:
            exponente_x = 1
    if y.count(".") > 0 :
        exponente_y = len(y) -  y.index(".")
        y.pop( y.index("."))
    else :
        if recursion == 0:
            exponente_y = 1
# x  e y son listas
    xlow = []
    xhigh = []
    ylow = []
    yhigh = []
    total = [0]
    a = [0]
    b = [0]
    c = [0]
    d = [0]
    i = 0
    if len(x) <= 1 and len(y) <= 1 :  # Base
        return naive(x, y, base)
    else:
        n = max( len(x), len(y))
        mitad = int( n/2 )

        if len(x) > 0 :
            for i in range(len(x)-1, len(x) - 1 - mitad, -1) :
                if i >= 0 :
                    xlow.insert(0,x[i])
            for i in range( len(x)-1-mitad, -1, -1) :
                if i >= 0 :
                    xhigh.insert(0,x[i])
        if len(y) > 0 :
            for i in range(len(y) - 1, len(y) - 1 - mitad, -1) :
                if i >= 0 :
                    ylow.insert(0,y[i])
            for i in range( len(y)-1-mitad, -1, -1) :
                if i >= 0 :
                    yhigh.insert(0,y[i])

        a = kara( xhigh, yhigh, base,1)
        b = kara(my_add(xlow, xhigh, base, 0), my_add(ylow, yhigh,base,0),base,1)
        c = kara( xlow, ylow, base,1)
        d = my_sub( my_sub(b,a,base,0), c, base, 0 )

        total = my_add(  total, a, base, 0)
        exp = mitad*2
        for j in range( 0, exp) :
            total.append(0)
        total_d = [0]
        total_d = d
        exp = exp/2
        for j in range( 0, exp) :
            total_d.append(0)
        total = my_add(total, total_d, base, 0)
        total = my_add(total, c, base, 0)

        if signo == 1 :
            total.insert("-")
        exp_total = exponente_x + exponente_y
        if exp_total > 0 :
            k = exp_total - len(total)
            if k > 0 :
                for l in range(0,k):
                    total.insert(0,0)
            total.insert(len(total) - exp_total + 2,".")
            for i in range(0,total.index(".")):
                if total[0] == 0 and  total[1] != ".":
                    total.pop(0)
        return  total
def div( list_a1 , list_b1):

    division = 0
    list_a = lib_nooblinux.convert_binario(list_a1)
    list_b = lib_nooblinux.convert_binario(list_b1)

    num_x = lib_nooblinux.convertbinario_numero(list_a)
    num_y = lib_nooblinux.convertbinario_numero(list_b)
    with localcontext() as cont:
        cont.prec= 10000
        division = Decimal(float(num_x))/Decimal(float(num_y))
    #division = float(num_x)//float(num_y)
    list_division = lib_nooblinux.convertirnumero_list(division)
    return list_division

class Cola:
    def __init__(self):
        self.items=[]

    def encolar(self, x):
        self.items.append(x)

    def desencolar(self):
        try:
            return self.items.pop(0)
        except:
            raise valueErro("La cola esta  vacia")
    def es_vacia(self):
        return self.items == []

    def facto(self, list_a1):
        if list_a1 == [0] or list_a1 == ['0']:
            return [1]
        list_a = lib_nooblinux.convert_binario(list_a1)
        number = lib_nooblinux.convertbinario_numero(list_a)
        q = Cola()
        q.encolar(1)
        j = 0
        for i in range(1, number +1):
            j = 0

            for k in range(0,len( q.items )):
                q.items[k]*=i
            while j < len(q.items) :
                while q.items[j] >= 10 :
                    rest = q.items[j]
                    if rest/10 >= 1:
                        if j == len( q.items ) -1 :
                            q.encolar( rest/10 )
                        else:
                            q.items[j + 1] += rest/10
                    q.items[j] = rest%10
                j+=1
        q.items.reverse()
        return  q.items
def pw( number, potencia):
    if potencia == 0 :
        return [1]
    total = number
    for i in range(1,potencia):
        total = kara(total,number,10,0)

    return total
