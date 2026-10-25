"""""
#Ejercicio 1
print("\nExercici 1:")

num1 = 2
num2 = 27
es_igual = (num1 == num2)

if es_igual:
    print(f"Son iguales {num1 == num2}")
elif num1 > num2:
    print(f"el numero 1 es mayor que el numero 2, {num1 > num2}")
else:
    print(f"El numero 2 es mas grande que el numero 1, {num1 < num2}")

#Ejercicio 2
print("\nExercici 2:")

paraula_1 = "Hola"
paraula_2 = "hola"
es_igual = paraula_1 == paraula_2
print(es_igual)

"""
#Ejercicio 3
print("\nExercici 3:")

router_encès = True
connexio_activa = False
xarxa_disponible = router_encès and connexio_activa
print(xarxa_disponible)