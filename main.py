#Pedir a usuario ingrese voltajes 
print("Ingrese 5 voltajes para obtener su promedio.")
print()

#Solicitar valor de cada voltaje 
voltaje_1=float(input("voltaje 1:"))
voltaje_2=float(input("voltaje 2:"))
voltaje_3=float(input("voltaje 3:"))
voltaje_4=float(input("voltaje 4:"))
voltaje_5=float(input("voltaje 5:"))

#Operacion de promedio de voltaje 
prom_voltaje=(voltaje_1+voltaje_2+voltaje_3+voltaje_4+voltaje_5) / 5

#Mostrar si el voltaje es alto o voltaje correcto segun su promedio
if prom_voltaje >220:
    print("ALTO VOLTAJE")
else:
    print("VOLTAJE CORRECTO")

   