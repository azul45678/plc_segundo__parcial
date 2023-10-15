#https://replit.com/join/aijkjvrzvz-azul-esmeraldae

print("1. Millas a Kilómetros")
print("2. Litros a Galones")
print("3. Grados Fahrenhit a celsius")

opciones = int(input("Ingrese la opción de conversión que desea utilizar: "))

if opciones == 1:
    print("Millas a Kilómetros")
    entrada = float(input("Ingrese la cantidad en Millas: "))
    resultado = (entrada * 1.60934)
    print("El resultado de la conversión es:", int(resultado))
  
elif opciones == 2:
    print("Litros a Galones")
    entrada = float(input("Ingrese la cantidad en Litros: "))
    resultado = (entrada * 0.264172, 2)
    print("El resultado de la conversión es:", int(resultado))
      
elif opcion == 3:
    print("Grados Fahrenheit a Celsius")
    entrada = float(input("Ingrese la cantidad en Grados Fahrenheit: "))
    resultado = round((entrada - 32) * 5/9, 2)
    print("El resultado de la conversión es:", int(resultado))

else:
    print("Opción no válida")
