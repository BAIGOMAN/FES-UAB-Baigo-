# Exercici 1: Funció de salutació
# Crea una funció saludar_a(nom, salutacio="Hola") que imprimeixi la salutació seguida del nom.
# Prova-la amb i sense el segon argument.
print("\nExercici 1:")
def saludar_a(nom,salutacio="Hola"):
    print(f"{salutacio} {nom}")

saludar_a("Mireia")
saludar_a("Mireia, Bon dia")

# Exercici 2: Parell o senar
# Crea una funció es_parell(numero) que retorni True si el número és parell i False si no ho és.

def es_parell(num):
    par = False
    if num % 2 == 0:
        par = True
    return par

print(f"{par}")