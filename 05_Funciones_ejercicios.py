# Exercici 1: Funció de salutació
# Crea una funció saludar_a(nom, salutacio="Hola") que imprimeixi la salutació seguida del nom.
# Prova-la amb i sense el segon argument.
print("\nExercici 1:")
def saludar_a(nom,salutacio="Hola"):
    print(f"{salutacio} {nom}")

saludar_a("Mireia")
saludar_a("Mireia, Bon dia")