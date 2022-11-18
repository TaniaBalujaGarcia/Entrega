#p1 = "orejero"
#a = p1[::-1]
#print(a)

#f = "Dabale arroz a la zorra el abad"
#b = f[::-1]
#print(b)
#c = f.replace(" ", "")
#print(c)

def es_palíndromo(cadena):
    cadena = cadena.replace(" ","")
    cadena = cadena.lower
    
    return cadena == cadena[::-1]

def saca_vocales(cadena):
    resultado = ""
    for letra in cadena:
        if letra in "aeiouAEIOUáéíóúÁÉÍÓÚäëïöüÄËÏÖÜ":
            resultado += letra
            
    return resultado