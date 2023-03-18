"""
Marina Fresneda Manzano

"""

def esPrimo (numero):
    """
    Devuelve `True` si su argumento es primo, y `False` si no lo es
    
    >>> [numero for numero in range(2, 50) if esPrimo(numero)]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    for prueba in range(2,int(numero**0.5)+1):
        if numero % prueba == 0: return False
    
    return True


def primos(numero):
    """
    Devuelve una **tupla** con todos los números primos menores que su argumento
    
    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """
    return tuple([prueba for prueba in range(2, numero) if esPrimo(prueba)])


def descompon(numero):
    """
    Devuelve una **tupla** con la descomposición en factores primos de su argumento
    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """
    factores=[] 

    for factor in primos(numero):
        while numero%factor == 0:
            factores.append(factor)
            numero //= factor
    return tuple(factores)

def dicFact(numero1,numero2):
    """
    Devuelve el factor primo de un número con su correspondiente exponente. 
    La función tiene como argumento dos números.
    >>> dicFact(90,14)
    ({2: 1, 3: 2, 5: 1, 7: 0}, {2: 1, 3: 0, 5: 0, 7: 1})
    """
    factores1 = descompon(numero1)
    factores2 = descompon(numero2)

    factores = set(factores1 + factores2)  # conjunto, ya que son números únicos
    dicfact1 ={factor : 0 for factor in factores } 
    dicfact2 ={factor : 0 for factor in factores} 
    for factor in factores1 : dicfact1[factor] += 1
    for factor in factores2 : dicfact2[factor] += 1
  
    return dicfact1,dicfact2

def mcm(numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    La función tiene como argumento dos números.
    >>> mcm(90, 14)
    630
    """
    mcm = 1
    dicFact1, dicFact2 = dicFact(numero1, numero2)
    for factor in  dicFact1 | dicFact2:
        mcm *= factor ** max(dicFact1[factor],dicFact2[factor])
    return mcm

def mcd(numero1, numero2):
    """
    Devuelve el máximo común divisor de sus argumentos.
    La función tiene como argumento dos números.
    >>> mcd(924, 780)
    12
    """
    mcd = 1
    dicFact1, dicFact2 = dicFact(numero1, numero2)
    for factor in  dicFact1 | dicFact2:
        mcd *= factor ** min(dicFact1[factor],dicFact2[factor])
    return mcd


import doctest
doctest.testmod()

