#Escribe un programa permita al usuario ingresar el precio de un producto y su categoría (A, B o C). Luego, aplica descuentos en función de la categoría y el número de unidades compradas. Por ejemplo: 
# Categoría A: 10% descuento
# Categoría B: 5% descuento
# Categoría C: 2% descuento

#Además, si el usuario compra más de 10 unidades, se aplica un descuento_adicional del 5%. Muestra el precio final después de todos los descuentos. 

# Solicitar el precio y la categoría al usuario
precio = float(input("Ingresar el precio del producto: "))
categoria = input("Ingrese la categoría del producto (A (10%, B(5%) o C(2%)): ")

if categoria == 'A':
    descuento = 0.10  
elif categoria == 'B':
    descuento = 0.05 
elif categoria == 'C':
    descuento = 0.02  
  
#Pedir la cantidad de unidades
unidades = int(input("Ingrese la cantidad de unidades compradas: "))

# aplica un descuento adicional del 5% si se compran más de 10 unidades 
if unidades > 10:
    descuento_adicional = 0.05 
else:
    descuento_adicional = 0


# Calcular el precio con descuentos
descuento_total = descuento + descuento_adicional
precio_final = precio * (1 - descuento_total)

# PRECIO FINAL 
print("El precio final es de {}.".format(precio_final))
