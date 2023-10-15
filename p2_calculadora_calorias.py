https://replit.com/join/acidmqnvxj-azul-esmeraldae

#Haz un programa que calcule las calorías quemadas durante una actividad física. 
#Pide al usuario ingresar su peso en kg, la duración en minutos y el tipo de actividad (correr, nadar, andar en bicicleta, etc.). 
#Utiliza fórmulas específicas para cada actividad y muestra el total de calorías quemadas.

peso = float(input("Ingresa tu peso en kg: "))
duracion = int(input("Ingresa la duración de la actividad en minutos: "))
actividad = input("Ingresa el tipo de actividad como nadar, correr, etc. : ")


calorias_por_minuto = {
    "correr": 10.0,
    "nadar": 8.0,
    "andar en bicicleta": 6.3,
   
}


if actividad in calorias_por_minuto:
    calorias_quemadas = calorias_por_minuto[actividad] * duracion
    print(f"Calorías quemadas durante {duracion} minutos de {actividad}: {calorias_quemadas} kcal")
else:
    print("Actividad no encontrada en la base de datos. No se puede calcular las calorías quemadas.")

