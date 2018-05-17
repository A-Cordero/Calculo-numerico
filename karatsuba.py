import lib_nooblinux
import operaciones
import sys
raiz_2 = [1,".",4,1,4,2,1,3,5,6,2,3,7,3]
def main():
    cola = operaciones.Cola()
    n = 6
    #calculando pi
    pi_iterado = []
    pi = [0]
    for k in range(0,n):
        pi_iterado = operaciones.div(operaciones.kara((cola.facto(operaciones.kara( [4], lib_nooblinux.convertirnumero_list(k),10,0))),operaciones.my_add([1,1,0,3],operaciones.kara([2,6,3,9,0],lib_nooblinux.convertirnumero_list(k),10,0),10,0),10,0),operaciones.kara(operaciones.pw(cola.facto(lib_nooblinux.convertirnumero_list(k)),4),operaciones.pw([3,9,6],4*k),10,0))
        pi = operaciones.my_add(pi,pi_iterado,10,0)
    pi = operaciones.kara( pi, operaciones.kara([2],raiz_2,10,0),10,0)
    pi = operaciones.div( pi , [9,8,0,1])

    pi = operaciones.div( [1],pi)

    lib_nooblinux.print_milista(pi)

    """    x = 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
    y = 10**14000
    list_x = lib_nooblinux.convertirnumero_list(x)
    list_y = lib_nooblinux.convertirnumero_list(y)
    list_z = operaciones.kara(list_x,list_y,10)
    lib_nooblinux.print_milista(list_z)
    """
    #numero = lib_nooblinux.convertirnumero_list([])
    #print numero
    #list_1 = lib_nooblinux.leer_milista()
#    list_2 = lib_nooblinux.leer_milista()
    #print list_1
#    print list_2
    #list_add = operaciones.pw(list_1,10)
    #list_add = cola.facto(list_1)
    #list_sub = operaciones.my_sub(list_1, list_2, 10, 0)
    #lib_nooblinux.print_milista(list_sub)
    #print list_1
    #print list_2
    #print list_add
    """binario = lib_nooblinux.convertirnumero_list(0.25)
    print "binario: ",
    #lib_nooblinux.print_milista()
    print binario
    print " numero: ",
    #numero = lib_nooblinux.convertbinario_nu(0.25)
    #print numero
    division = operaciones.div(lib_nooblinux.convert_binario(list_1),lib_nooblinux.convert_binario(list_2))
    print division
    print lib_nooblinux.convertbinario_numero(division)"""
main()
