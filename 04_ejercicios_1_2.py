nombre, ubicacion, numero_puerto, encendido = "router1", "servidores", 54301, True

print(f"Nombre: {nombre}, Ubicacion: {ubicacion}, Numero de puerto: {numero_puerto}, Esta encendido? {encendido}"), 

espacio_disponible = float(input("Quants GB de memoria disponible hi ha? Introdueix el numero: "))
consumido = float(input("Quants GB de memoria has consumit? Introdueix el numero: "))
espacio_restante =espacio_disponible-consumido
print("El espacio disponible (en GB) es: ", espacio_restante)
consumido = float(input("Quants GB de memoria has consumit ara? Introdueix el numero: "))
espacio_restante =espacio_disponible-consumido
print("El espacio disponible (en GB) es: ", espacio_restante)