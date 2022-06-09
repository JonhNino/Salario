# Programa Para Calcular el Subisidio de transporte
# Autor: Jonh Niño
# Fecha 8/06/2022

#Entrada 
nombre=input("Nombre Empleado: ")
salario=float(input("Salario: "))

#Proceso
if salario <= 1000000:
    subsidio=120000
else:
    subsidio=120000

#Salida
print("Nombre empleado: ", nombre)
print("Salario: ","{:,.2f}".format(salario))
print("Subisidio de Transporte: ","{:,.2f}".format(subsidio))
    