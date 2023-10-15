# https://replit.com/join/nbbyockbpt-azul-esmeraldae

#Escribe un programa que ayude a calcular los nutrientes totales en una receta. 
#El usuario debe ingresar los ingredientes y sus cantidades, asi como la información nutricional por cada 100 gramos de cada ingrediente.
#Luego, calcula los nutrientes totales en la recta considerando las cantidades proporcionadas por el usuario.

def calcular_nutrientes():
    num_ingredientes = int(input("Ingrese el número de ingredientes en la receta: "))
    nutrientes_totales = {"calorias": 0, "proteinas": 0, "grasas": 0, "carbohidratos": 0}

    ingredientes = [input("Nombre del ingrediente: ") for _ in range(num_ingredientes)]
    cantidades = [float(input("Cantidad del ingrediente (en gramos): ") ) for _ in range(num_ingredientes)]
    calorias = [float(input("Calorías por 100g del ingrediente: ")) for _ in range(num_ingredientes)]
    proteinas = [float(input("Proteínas por 100g del ingrediente: ")) for _ in range(num_ingredientes)]
    grasas = [float(input("Grasas por 100g del ingrediente: ")) for _ in range(num_ingredientes)]
    carbohidratos = [float(input("Carbohidratos por 100g del ingrediente: ")) for _ in range(num_ingredientes)]

    for i in range(num_ingredientes):
        cantidad = cantidades[i]
        nutrientes_totales["calorias"] += (calorias[i] / 100) * cantidad
        nutrientes_totales["proteinas"] += (proteinas[i] / 100) * cantidad
        nutrientes_totales["grasas"] += (grasas[i] / 100) * cantidad
        nutrientes_totales["carbohidratos"] += (carbohidratos[i] / 100) * cantidad

    print("Nutrientes totales en la receta:")
    for nutriente, valor in nutrientes_totales.items():
        print(f"{nutriente.capitalize()}: {valor:.2f} gramos")
        
if __name__ == "__main__":
    calcular_nutrientes()
