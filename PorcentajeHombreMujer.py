#Un maestro desea saber qué porcentaje de hombres y que
#porcentaje de mujeres hay en un grupo de estudiantes.


# Pedir al usuario el número total de estudiantes y el número de hombres
num_estudiantes = int(input("Introduce el número total de estudiantes en el grupo: "))
num_hombres = int(input("Introduce el número de hombres en el grupo: "))

# Calcular el porcentaje de hombres y mujeres
porcentaje_hombres = (num_hombres / num_estudiantes) * 100
porcentaje_mujeres = 100 - porcentaje_hombres

# Mostrar los porcentajes de hombres y mujeres al usuario
print("El porcentaje de hombres en el grupo es:", porcentaje_hombres, "%")
print("El porcentaje de mujeres en el grupo es:", porcentaje_mujeres, "%")
