""""
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

#parte 2 de ejercicios de listas

#Ejercicio 1
print("\nExercici 1:")

lista = [1,2,3,4,5]
lista.append(6) 
lista.insert(2,10)
lista[0] = 0
print(lista)

#Ejercicio 2
print("\nExercici 2:")

llista_a = [1, 2, 3]
llista_b = [4, 5, 6, 1, 2]
llista_a.extend(llista_b)
llista_a.remove(1)
element_eliminat = llista_a.pop(3)
print(element_eliminat)
llista_b.clear()

"""
#Ejercicio 2
print("\nExercici 2:")

lista = [1,2,3,4,5,6,7,8,9,10]
del lista[2:4]
print(lista)