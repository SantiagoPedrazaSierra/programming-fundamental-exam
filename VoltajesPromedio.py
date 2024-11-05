#Solicitar a usuario voltajes 
voltaje_1=float(input("Voltaje 1: "))
voltaje_2=float(input("Voltaje 2: "))
voltaje_3=float(input("Voltaje 3: "))

#Operacion promedio 
promedio=(voltaje_1+voltaje_2+voltaje_3) / 3

#Comprobar valor de voltajes si es mayor o menor a 115
if promedio< 115:
    print("VOLTAJE CORRECTO")

elif promedio > 115 and promedio < 220:
    print("ALTO VOLTAJE")

elif promedio > 220:
        print("PELIGRO")