
#Ejercicio 1
print("\nExercici 1:")

missatge = ["C", "o", "d", "i", " ", "s", "e", "c", "r", "e", "t"]
missatge_nou = missatge[5:]
print(missatge_nou)

#Ejercicio 2
print("\nExercici 2:")

nombres = [10, 20, 30, 40, 50]
nombres [0], nombres[-1] = nombres [-1], nombres[0] 
print(nombres)

#Ejercicio 3
print("\nExercici 3:")

pa_de_dalt = ["pa de dalt"]
ingredients = ["pernil", "formatge", "tomàquet"]
pa_de_sota = ["pa de sota"]
entrepa = pa_de_dalt + ingredients + pa_de_sota 
print(entrepa)

#Ejercicio 4
print("\nExercici 4:")

llista = [1, 2, 3]
llista += llista
print(llista)

#Ejercicio 5
print("\nExercici 5:")

llista = [10, 20, 30, 40, 50]
num_central = len(llista) // 2
print(llista [num_central])

#Ejercicio 6
print("\nExercici 6:")

llista = [1, 2, 3, 4, 5, 6]
mitad = len(llista) // 2
llista_nova = llista[:mitad][::-1] + llista[mitad:]
print(llista_nova)