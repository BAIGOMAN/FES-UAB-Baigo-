#Ejercicio 1

num1 = input("Dime un numero para poder compararlo con otro: ")
num2 = input("Dime un segundo numero para poder compararlo: ")

if(num1 > num2):
    print("El primer numero es mas grande que el segundo")
elif(num1 < num2): 
    print("El segundo numero es mas grande que el primero")
elif num1 == num2:
    print("Son iguales")

#Ejercicio 2
print("\nExercici 2:")

num1 = float(input("Dime el primer numero con el que operar: "))
num2 = float(input("Dime un segundo numero con el que hacer la operacion: "))
operacion = input("Dime que operacion quieres hacer con los numeros: (+, -, *, /): ").strip()

if operacion == "/" and num2 == 0:
 print("La operacion no se puede hacer, no se puede dividir entre 0")
elif operacion =="/":
    resultado = num1 / num2
    print(f"El resultado es: {resultado}")
elif operacion == "+":
    resultado = num1 + num2
    print(f"El resultado es: {resultado}")
elif operacion == "-":
    resultado = num1 - num2
    print(f"El resultado es: {resultado}")
elif operacion == "*":
    resultado = num1 * num2
    print(f"El resultado es: {resultado}")

#Ejercicio 3
print("\nExercici 3:")

año = int(input("Dime un añua para ves si es bisiesto o no: "))

if año % 4 == 0 and año %100 != 0 or año %400 == 0:
    print(f"El año {año} es bisiesto")
else:
    print(f"El año {año} no es bisiesto")


#Ejercicio 4
print("\nExercici 4:")

edad = int(input("Dime una edad y te la clasifico: "))

if edad < 0:
    print("La edad no puede ser tan pequeña")
elif edad > 0 and edad <= 2:
    print("Es un nadó")
elif edad > 3 and edad <= 12:
    print("es un infant")
elif edad > 13 and edad <= 17:
    print("es un adolescente")
elif edad > 18 and edad <= 64:
    print("Es un adulto")
else:
    print("es una persona grande")

"""
para comentar todo entre estas comillas
"""
