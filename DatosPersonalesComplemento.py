#Si el empleado es mayor de 55 años disfrutará de un bono de prepensión correspondiente al 5% de su sueldo básico.
#Si el empleado es casado y tiene hijos se le otorgará un paseo cada diciembre
#Si el sueldo básico está entre 1000000 y 1500000 tendrá una comisión del 2% sobre el valor del sueldo; Si el sueldo básico está entre 1500001 y 2000000 tendrá una comisión del 5% sobre el valor del sueldo; para todos los demás casos no habrá comisión.
#Si el empleado trabajó más de 20 días al mes y su sueldo es menor a 1000000 tendrá derecho a un bono de alimentación.



identificacion = input("Digite su identificacion: ")
nombres = input("Digite su Nombre: ")
apellido = input("Digite su Apellido: ")
direccion = input("Digite su Direccion: ")
telefono = input("Digite su Telefono: ")
edad = input("Digite su edad: ")
estadoCivil = input("Estado Civil:")
hijos= input("Numero de Hijos:")
estatura = input("Estatura en Centimetros:")
fechaContrato = input("fecha de contratación (Día/mes/año):")
sueldoBasico = float(input("Sueldo básico:"))
diasLabor = int(input("Días Laborados:"))

print("==============================")
print("****DatosRegistrados****")
print("==============================")

print("Identificacion:" + " " + identificacion)
print("Nombres:" + " " + nombres)
print("Apellidos:" + " " + apellido)
print("Drección:" + " " + direccion)
print("Telefono:" + " " + telefono)
print("Edad:" + " " + edad)
print("Estado Civil:" + " " + estadoCivil)
print("Hijos:" + " " + hijos)
print("Estatura:" + " " + estatura)
print("Fecha de Contrato:" + " " + fechaContrato)
print("Sueldo basico:" + " " + str(sueldoBasico))
print("Dias laborados ed:" + " " + str(diasLabor))
print("==============================")

# Bono de pre-pensión
if int(edad) > 55:
    bono_prepension = 0.05 * sueldoBasico
    print("Bono de pre-pensión: $" + str(bono_prepension))
else: print(" No Bono de pre-pensión")
# Paseo en diciembre
if estadoCivil.lower() == "casado" and int(hijos) > 0:
    print("Paseo en diciembre")
else: print("No Paseo Diciembre")
# Comisión
if 1000000 <= sueldoBasico <= 1500000:
    comision = 0.02 * sueldoBasico
    print("Comisión: $" + str(comision))
elif 1500001 <= sueldoBasico <= 2000000:
    comision = 0.05 * sueldoBasico
    print("Comisión: $" + str(comision))

else: print("No Comisión")

# Bono de alimentación
if diasLabor > 20 and sueldoBasico < 1000000:
    bono_alimentacion = 80000
    print("Bono de alimentación: $" + str(bono_alimentacion))
else: print("No Bono de alimentación")