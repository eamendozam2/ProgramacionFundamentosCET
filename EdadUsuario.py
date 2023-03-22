# pedir la edad del usuario
import datetime
edad = int(input("¿Cuál es tu edad? "))
anio_actual = datetime.date.today().year
a = anio_actual - edad
# ciclo for para imprimir los años que ha cumplido
for i in range(1, edad+1):
    print(f"Año {a+i}: Cumplí {i} años")