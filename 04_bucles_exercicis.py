""""
#Ejercicio 1
print("\nExercici 1:")

contador =10

while contador > 0:
    print(contador)
    contador-=1

#Ejercicio 2
print("\nExercici 2:")

contador = 1
suma_parells = 0
while contador <= 20:
    if contador % 2 == 0:
        suma_parells += contador
    contador +=1
print(f"La suma de los pares es: {suma_parells}")

#Ejercicio 3
print("\nExercici 3:")

num = int(input("Introduce un numero entero positivo para calcular su factorial: "))
factorial = 1
while num > 0:
    factorial = num*factorial
    num -= 1
print(f"El factorial es: {factorial}")

#Exercici 4: Validació de contrasenya

contrasenya = str(input("Introduce una contrasenña: "))

while len(contrasenya) < 8:
    print("La contrasenya ha de tenir almenys 8 caracters.")
    contrasenya = str(input("Introduce una contrasenya: "))
print("Contraseá valida.")

# Exercici 5: Taula de multiplicar

num = int(input("Introduce un numero entero positivo para calcular su tabla de multiplicar: "))
contador = 0

while contador <10:
    contador += 1
    multiplicacion = contador * num
    print(f"{contador} * {num} = {multiplicacion}")

"""
# Exercici 6: Números primers fins a N

num = int(input("Introduce un numero positivo: "))
contador = 1

while contador <= num:
    
    if num % contador == 0:
        print(f"{contador}")
    contador += 1