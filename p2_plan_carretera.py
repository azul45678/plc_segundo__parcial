#https://replit.com/join/gnftezpzoo-azul-esmeraldae

def calculo_costo(distancia, rendimiento, gasolina, dias):
  costo_total_si = (distancia/rendimiento) * gasolina

  print("El costo total del viaje es de:  ", costo_total_si)


distancia = float(input("Ingresa la distancia en millas:  "))
rendimiento = float(input("Ingresa el rendimeinto en millas pro galón:  "))
dias = int(input("Ingresa la cantidd de dias que planea viajar:  "))
gasolina = float(input("Ingresa el costo por galón de gasolina:  "))
calculo_costo(distancia, rendimiento, gasolina, dias)

costo_total_si = (distancia/rendimiento) * gasolina
costo_total_si = costo_total_si * dias
print("El costo total del viaje es de:  ", costo_total_si)  
