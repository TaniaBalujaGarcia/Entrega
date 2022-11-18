# from f_retenciones import obtener_exencion, obtener_retencion
from P16_F_retenciones_2 import *

# Obtener datos de entrada
sueldo = float(input("Sueldo: ")) # El float es para poder operar con los datos de salida (decimales) de la pregunta
situacion = input("Situación (1/2/3): ")
num_hijos = int(input("Número de hijos: "))

# Obtener exención
exencion = obtener_exencion(situacion, num_hijos)
sueldo_a_retener = sueldo - exencion
porcentaje = obtener_retencion(sueldo_a_retener)

# Obtener retención
monto_anual = sueldo_a_retener * porcentaje / 100
monto_mensual = monto_anual / 12

# Mostrar resultados
print("Sueldo anual: \t", sueldo)
print("Situación: \t", situacion)
print("Base a retener: ", sueldo_a_retener)
print("Porcentaje: \t", porcentaje)
print("Total anual: \t", monto_anual)
print()
print("Retención mensual: ", monto_mensual)