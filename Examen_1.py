# Pregunta 1
def m(k):
    return (k%2) == 0

k1 = 1
P1 = m(k1)


# Pregunta 2
def f(ht):
    b = 0
    for elt in ht:
        b = elt + b
    return b

ht1 = [1, 2, 3, 4, 5]
P2 = f(ht1)


# Pregunta 3
def s(m, n):
    r = None
    if m <= n:
        r = m
    else:
        r = n
    return r

m1 = 2
n1 = 1
P3 = s(m1, n1)


# Pregunta 4
def interes_anual(cantidad, interes):
    return cantidad*(1+interes/100)

def retorno_inversion(cantidad, interes, anyos):
    r = []
    for anyo in range(anyos):
        cantidad = interes_anual(cantidad, interes)
        r.append(round(cantidad, 2))
        
    return r
P4 = retorno_inversion(10,4,3)


# Pregunta 5/6
def applyToEachString(stringFunction, *words):
    myList = []
    for word in words:
        # ¿Qué instrucción debe ir aquí?
        #myList = stringFunction(word) NOOOOO
        #myList.append(onlyVowels(word)) Llama la otra función
        myList.append(stringFunction(word)) # Parámetro
        #myList.append(stringFunction, word) NOOOO
    return tuple(myList)

def onlyVowels(word):
    vowels = 'aeiouáéíóúü'
    resp = ""
    for letter in word:
        if letter in vowels or letter in vowels:
            resp = resp + letter
            
    return resp

P6 = applyToEachString(str.upper, "Periódico", "navío", "computadora")


# Pregunta 7
def what_i_do(p1, p2):
    if p2 < len(p1):
        return p1
    
    gap = (p2 - len(p1))//2
    
    return " " * gap + p1

pa = "Dormir"
pb = 30
P7 = what_i_do(pa, pb)


# Pregunta 8
def second_scored(*lis):
    maximum = max(lis)
    preMax = min(lis)
    for nombre in lis:
        if (nombre < maximum and nombre > preMax):
            preMax = nombre
    return preMax

"""
EL COMENTARIO
"""

def another_second_scored(*lis):
    arr = list(set(lis))
    arr.sort()
    return arr[-2]

def other_second_scored(*lis):
    for n in lis:
        i = 2
        is_second = True
        while i <= n //2:
            if n % i == 0:
                is_second = False
            i += 1
            
        if is_second:
            return n
        
def the_second_scored(*lis):
    first = max(lis)
    lis = list(lis)
    lis.remove(first)
    while first == max(lis):
        lis.remove(first)
    return max(lis)

lis1 = "Saluchi"
lis2 = "Tania"
lis3 = "Alba"
P8 = second_scored(lis1, lis2, lis3)
P8a = another_second_scored(lis1, lis2, lis3)
#P8b = other_second_scored(lis1, lis2, lis3)
P8c = the_second_scored(lis1, lis2, lis3)


# Pregunta 9
def n(a):
    return (a % 2) == 0

def p(k):
    return not n(k)

k1 = 8
P9 = p(k1)


# Pregunta 10
def g(xxs):
    k = 1
    for elm in xxs:
        k = k*elm
    return k

xxs1 = [1, 2, 3, 4, 5]
P10 = g(xxs1)


# Pregunta 11
for x in ['Dar Vader', 'Luke Skywalker', 'Obi Wan', 'Leia Organa', 'R2-D2', 'C-3PO']:
    pass
    #P11 = print(x)


# Pregunta 12
#Bucle 1
for xa in range(0, 6):
    pass

    #P12a = print(xa)
#Bucle 2
index = 0
while index <= 6:
    pass
    index = index + 1
    
    #P12b = print(index)


# Pregunta 13
for x13 in range(0, 9):
    pass

    #P13 = print(x13)


# Pregunta 16
b = 42
def f1(b, k):
    return b + k

P16 = f1(0, 8)


# Pregunta 17
q = 51
def np(a):
    q = 42     # ¿Qué ocurre aquí?
    return q*a

P17 = np(1)


# Pregunta 18
z = -9
def ik(z):
    return z

P18 = ik(42)


# Preunta 23
fruits = {'banana', 'apple', 'orange', 'cherry'}
fruits.add('orange') # ¿Qué hará esta línea?

P23 = fruits


# Pregunta 24/25
def adder(n):
    return lambda x : x + n
fa = adder(2)

P25 = fa(2)


# Pregunta 26
def g(f):
    def k(*args):
        return 2*f(*args)
    return k


# Pregunta 27
# Jerarquía de clases para representar personajes de Star Wars
class StarWarsCharacter:
    def __init__(self, name):
        self.name = name
        
class Jedi (StarWarsCharacter):
    def __init__(self, name, midichlorians):
        super().__init__(name)
        self.midichlorians = midichlorians
        
#chewie = StarWarsCharacter('Chewbacca')
#m = chewie.midichlorians
anakin = Jedi('Anakin', 100000)


# Pregunta 30
characters = [Jedi('Anakin', 10000), Jedi('Yoda', 1000000), StarWarsCharacter('Chewie')]
sum = 0
for elt in characters:
    sum = sum + elt.midichlorians