# cad = "Inglaterra"
# lcad = list(cad)
# lcad.remove("a")
# print(lcad)
# 
# a = "-".join(lcad)
# print(a)
# 
# b = ", ".join(lcad)
# print(b)
# 
# c = "".join(lcad)
# print(c)

def tacha(caracter, palabra):
    lpalabra = list(palabra)
    lpalabra.remove(caracter)
    return "".join(lpalabra)

def frecuencias(palabra):
    resultado = {}
    for letra in palabra:
        if letra in resultado:
            resultado[letra] += 1
        else:
            resultado[letra] = 1
    return resultado

def es_anagrama (p1, p2):
    for letra in p1:
        if letra in p2:
            p2 = tacha(letra, p2)
        else:
            return False
    return p2 == ""

def es_anagrama_by_dict(p1, p2):
    #return frecuencias(p1) == frecuencias(p2)
    fp1 = frecuencias(p1)
    fp2 = frecuencias(p2)
#     if fp1 == fp2:
#         return True
#     else:
#         return False 
    return fp1 == fp2