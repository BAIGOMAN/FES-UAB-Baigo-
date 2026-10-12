#ejercicio 1

valor = float (input("Quants paquets ha rebut l'encaminador? Introdueix el numero: "))
print(round(valor))
print(int(1200) + int(valor))
#print( "1200" + str(int(valor))) esto era para concatenar los numeros no sumarlos. 

#ejercicio 2

num = int(input("Quina es la teva conexio en Mbps? Introdueix el numero: "))
num = float(num)/8 #La division tambien puede hacerse dentro del print
print("la velocitat equivalent en MB/s es:", num)
