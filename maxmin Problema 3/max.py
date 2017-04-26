'''
EL SIGUIENTE PROGRAMA DA LA FACILIDAD DE MEDIR O COMPARAR A DOS NÚMEROS ENTRES SI, DONDE DEPENDIENDO DE
FUNCIONES UTILIZABLES SE PODRA REALIZAR DIVERSAS OPERACIONES Y LA MISMA SE GUARDARAN EN LA CANTIDAD DE LAS VECES QUE SE UTILIZEN
'''
maxCalled = 0
minCalled = 0


def max_val(a, b):
    '''
     FUNCION QUE REFLEJA EL MAYOR DE LOS NUMEROS COMPARADOS

    :return: Regresa el valor mas grande de los 2
     :rtype: int

     :type a: int
     :param a: Primer numero a comparar

      :type b: int
      :param b: Segundo numero a comparar



     '''
    global maxCalled
    maxCalled = maxCalled + 1

    if (a > b):
        return a
    elif (b > a):
        return b
    else:
        return a


def min_val(a, b):
    '''
    FUNCION QUE REFLEJA EL MENOR DE LOS VALORES COMPARADOS

    :return: Regresa el valor mas pequeño de los 2
    :rtype: int

    :param b: Segundo numero a comparar
    :type b: int

    :param a: Primer numero a comparar
    :type a: int





    '''
    global minCalled
    minCalled = minCalled + 1

    if (a < b):
        return a
    elif (b < a):
        return b
    else:
        return a


def print_usage(init_msg, max_val=True, min_val=True):
    '''
    FUNCION QUE INDICA LA CANTIDAD DE VECES QUE FUERON UTILIZADAS LAS FUNCIONES ANTES LLAMADAS

    :param init_msg: EL PRIMER ELEMENTO QUE SE IMPRIMIRÁ
    :type init_msg: str

    :param max_val: INDICA SI SE VA A IMPRIMIR EL USO DE LA SIGUIENTE FUNCION max_val
    :type max_val: bool

    :param min_val: INDICA SI SE VA A IMPRIMIR EL USO DE LA SIGUIENTE FUNCION min_val
    :type min_val: bool

    '''
    global maxCalled, minCalled
    print
    init_msg
    if max_val:
        print('functin max_val was called', maxCalled, ' times')
    if min_val:
        print('function min_val was called', minCalled, ' times')


if __name__ == '__main__':
    print('Calling function max_val')
    max_val(1, 4)
    max_val(2, b=1)
    max_val(b=4, a=3)

    print('Calling function min_val')
    min_val(1, 4)
    min_val(2, 4)
    min_val(4, b=9)

    print_usage('The usage of functions min_val and max_val')