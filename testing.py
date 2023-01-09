import random
numAleatorio = random.randint(100, 999)
print("Número aleatorio: ", numAleatorio)

unidad = int((str(numAleatorio))[2]);
decena = int((str(numAleatorio))[1]);
centena = int((str(numAleatorio))[0]);

print(unidad);
print(decena);
print(centena);