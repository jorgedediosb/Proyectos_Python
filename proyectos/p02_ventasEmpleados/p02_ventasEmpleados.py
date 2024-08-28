# Programa que calcula el 13% de las ventas de los empleados.

nombre = input("Nombre de empleado: ")
#al guardarse como string debemos transformar a int
ventas = int(input("¿Cuantas ventas has hecho hoy? "))
#comisión del 13% usando round para redondear a 2 decimales
comisiones = round((ventas * 13)/ 100, 2)
print(f"{nombre}, hoy recibes {comisiones} euros por tus ventas.")