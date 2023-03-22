#Un maestro necesita un sistema para capturar las
#calificaciones de 5 parciales de sus alumnos, después
#recapturarlas necesita que se despliegue el promedio,
#cuando ya no quiera capturar más alumnos, necesita que
#se despliegue el promedio general de todos los alumnos
#capturados. Preguntar si desea ejecutar de nuevo el
#programa con el ciclo while.


# inicializar variables
total_alumnos = 0
total_calificaciones = 0

# ciclo while para ejecutar el programa varias veces
while True:
    # capturar las calificaciones de 5 parciales de un alumno
    calificaciones = []
    for i in range(5):
        calificacion = float(input(f"Ingrese la calificación del parcial {i+1}: "))
        calificaciones.append(calificacion)
    
    # calcular el promedio del alumno
    promedio_alumno = sum(calificaciones) / len(calificaciones)
    print(f"El promedio del alumno es: {promedio_alumno}")
    
    # agregar el promedio del alumno al promedio general
    total_alumnos += 1
    total_calificaciones += promedio_alumno
    
    # preguntar si desea capturar más alumnos
    respuesta = input("¿Desea capturar las calificaciones de otro alumno? (s/n): ")
    if respuesta.lower() != "s":
        break

# calcular el promedio general
promedio_general = total_calificaciones / total_alumnos
print(f"El promedio general de todos los alumnos capturados es: {promedio_general}")