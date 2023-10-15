# https://replit.com/join/vdqqadxlse-azul-esmeraldae

#Crea un programa que permita al usuario ingresar las notas de un grupo de estudiantes.
#Calcula el promedio de las notas, la nota más alta y la nota más baja. Además, miestra cuántos estudiantes aprobaron (notas mayores o iguales a 60) y cuántos reprobaron.

def calcular_estadisticas_notas(notas):
  promedio = sum (notas) / len (notas)

  nota_maxima = max(notas)
  nota_minima = min(notas)

  estudiantes_aprobados = sum(nota >= 60 for nota in notas)
  estudiantes_reprobados = len(notas) - estudiantes_aprobados

  print("Promedio de notas:", promedio)
  print("Nota más alta:", nota_maxima)
  print("Nota más baja:", nota_minima)
  print("Estudiantes aprobados:", estudiantes_aprobados)
  print("Estudiantes reprobados:", estudiantes_reprobados)

cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
notas_estudiantes = []
for i in range(cantidad_estudiantes):
  nota = float(input(f"Ingrese la nota del estudiante {i+1}: "))
  notas_estudiantes.append(nota)

calcular_estadisticas_notas(notas_estudiantes)
