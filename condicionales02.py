EJERCICIO N°2

#Escribe un programa que reciba un número del usuario e imprima "HUrra!!" si es mayor a -10 y menor a 10. ambos incluidos. 

numero = float(input("Por favor, ingresa un número: "))

if -10 <= numero <= 10:
    print("¡Hurra!!")
else:
    print("El número no está en el rango de -10 a 10.")

