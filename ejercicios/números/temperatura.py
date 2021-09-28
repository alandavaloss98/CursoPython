#Programa que pide un valor en grados centígrados y lo muestra en grados farenheit
#°C * 1.8 + 32 = °F
grados_centigrados = input("Introduce el valor en grados centigrados: ")
grados_centigrados = float(grados_centigrados)

grados_farenheit = ((grados_centigrados * 1.8) + 32)

print(f"El equivalente de {grados_centigrados}°C es: {grados_farenheit}°F")