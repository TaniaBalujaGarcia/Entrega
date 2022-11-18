# # Pedir números
# n1 = input("Número 1: ")
# n2 = input("Número 2: ")
# 
# # Convertir cadenas de entrada en números
# n1 = float(n1)
# n2 = float(n2)
# 
# # Realizar operaciones (suma, resta, producto y división)
# suma = n1 + n2
# resta = n1 - n2
# producto = n1*n2
# division = n1/n2
# 
# # Imprimir salida
# print("La suma es", suma, ", la resta es", resta, ", el producto es", producto, "y la división es", division)

## La manera más completa de hacer el ejercicio es la siguiente
class Calculadora:
    # Creación de métodos
    # self hace referencia a un determinado objeto
    # init significa inicializar
    
    def __init__(self, n1, n2):
        # Asignar atributos
        self.suma = (n1 + n2)
        self.resta = (n1 - n2)
        self.mult = (n1 * n2)
        self.div = (n1 / n2)
        
ope = int(input("Ingrese la operación deseada: \n Para la suma 1\n Para la resta 2\n Para la multiplicación 3\n Para la división 4\n"))

# Impresión del resultado
while ope > 0 and ope <= 4:
    num1 = float(input("Ingrese el primer valor: "))
    num2 = float(input("Ingrese el segundo valor: "))
    # Creación del objeto para acceder al método
    operacion = Calculadora(num1, num2)
    if ope == 1:
        print("La suma de", num1, "+", num2, "es:", operacion.suma, "\n")
    elif ope == 2:
        print("La resta de", num1, "-", num2, "es:", operacion.resta, "\n")
    elif ope == 3:
        print("La multiplicación de", num1, "*", num2, "es:", operacion.mult, "\n")
    elif ope == 4:
        print("La división de", num1, "/", num2, "es:", operacion.div, "\n")
        
    opcion = input("Desea realizar otra operaion? S/N: ")
    opcion = opcion.upper()
    if (opcion == "S"):
        ope = int(input("Ingrese la operación deseada: \n Para la suma 1\n Para la resta 2\n Para la multiplicación 3\n Para la división 4\n"))
    else:
        ope = int(input("Para salir de la aplicación presione un número diferente a las opciones de las operaciones: "))
print("Usted ha salido de la aplicación")