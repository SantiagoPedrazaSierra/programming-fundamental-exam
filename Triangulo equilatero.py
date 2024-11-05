#Solicitar valor de lados a usuario 
lado=float(input("Ingrese valor de lado:"))

#Operacion para hallar area segun el lado 
area=1.732/4 * lado**2

#Mostrar resultado de area 
if area > 1000:
    print("DATOS NO VALIDOS")
else:
    print(area)
