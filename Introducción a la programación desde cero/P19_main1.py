from P18_F1C import *

dialogo = [
    {"Hola", gritando},
    {"Por favor, no chilles, me duele mucho la cabeza", None},
    {"Perdona, ¿quieres una aspirina?", voz_baja}]

for frase, modo in dialogo:
    if modo == None:
        print(frase)
    else:
        print(modo(frase))