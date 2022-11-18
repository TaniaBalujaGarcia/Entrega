from P21_Cesar import cesar, cifrar, creaEncriptador

print(cesar("A", 1))
print(cesar("C", 3))
print(cesar("Z", 1))
print(cifrar("ZAR", 1))
print(cifrar("ABS", -1))

_encrypt = creaEncriptador(5)
_desencrypt = creaEncriptador(-5)
print(_encrypt("HOLA"), cifrar("HOLA", 5))
print(_desencrypt("MTPF"), cifrar("MTPF", -5))