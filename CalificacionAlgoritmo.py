#Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. Dicha calificación se compone de tres exámenes parciales.

# Pedir al usuario sus notas en los tres exámenes parciales
nota1 = float(input("Introduce tu nota en el primer examen parcial: "))
nota2 = float(input("Introduce tu nota en el segundo examen parcial: "))
nota3 = float(input("Introduce tu nota en el tercer examen parcial: "))

# Calcular el promedio de las tres notas
promedio = (nota1 + nota2 + nota3) / 3

# Mostrar la calificación final al usuario
print("Tu calificación final en la materia de Algoritmos es:", promedio)