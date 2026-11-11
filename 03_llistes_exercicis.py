
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
print("Llista a:", llista_a)
print("Llista b:", llista_b) 


#Ejercicio 3
print("\nExercici 3:")

lista = [1,2,3,4,5,6,7,8,9,10]
del lista[2:4]
print(lista)

#Ejercicio 4
print("\nExercici 4:")

lista =[5, 2, 8, 1, 9, 4, 2]
lista.sort()
num_2 = lista.count(2)
hay_el_7 = 7 in lista
print(f"Llista ordenada: {lista}")
print(f"Número de vegades que apareix el 2: {num_2}")
print(f"Hi ha un 7 a la llista: {hay_el_7}")

#Ejercicio 5
print("\nExercici 5:")

lista = [1,2,3]
copia_1 = lista[:]
copia_2 = lista.copy()
referencia = lista
lista [0] = 10
print(f"Lista original: {lista}")
print(f"Copia 1: {copia_1}")
print(f"Copia 2: {copia_2}")
print(f"Referencia: {referencia}")

#Ejercicio 6
print("\nExercici 6:")

lista = ["Poma", "pera", "PLÀTAN", "taronja"]
lista.sort(key=str.lower)
print(lista)
