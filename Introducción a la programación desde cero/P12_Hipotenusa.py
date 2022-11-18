import math

def hipotenusa(c1, c2 = -1): # c1 y c2 son variables locales
    print("c1: ", c1, "c2: ", c2)
    #if c2 == -1:
    #    h = math.sqrt(c1*c1 + c1*c1)
    #else:
    #    h = math.sqrt(c1*c1 + c2*c2)
    h = math.sqrt(c1*c1 + c2*c2)
    
    return h

def hcartabon(l):
    return hipotenusa(l, l)

cateto1 = 3 # Variable global
cateto2 = 4 # Variable global

_hcartabon = hcartabon(cateto1)
_hipotenusa = hipotenusa(cateto1, cateto2)