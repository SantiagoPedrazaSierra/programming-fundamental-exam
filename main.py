#PRIMER EJERCICIO

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


#SEGUNDO EJERCICIO

#Solicitar valor de lados a usuario 
lado=float(input("Ingrese valor de lado:"))

#Operacion para hallar area segun el lado 
area=1.732/4 * lado**2

#Mostrar resultado de area 
if area > 1000:
    print("DATOS NO VALIDOS")
else:
    print(area)


#TERCEER EJERCICIO

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


#CUARTO EJERCICIO

#Solicitar metros
metros=float(input("Metros:"))

#Operacion para pasar de metros a kilometros 
kilometros= metros/1000

#Mostrar distancia en kilometros 
print(f"{round(metros)}m = {round(kilometros)}km.")