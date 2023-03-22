# Definir la función para cada operación
def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

# Pedir al usuario que introduzca los números y la operación deseada
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
operacion = input("Introduce la operación que quieres realizar (+, -, *, /): ")

# Realizar la operación correspondiente y mostrar el resultado
if operacion == "+":
    print(num1, "+", num2, "=", suma(num1, num2))

elif operacion == "-":
    print(num1, "-", num2, "=", resta(num1, num2))

elif operacion == "*":
    print(num1, "*", num2, "=", multiplicacion(num1, num2))

elif operacion == "/":
    print(num1, "/", num2, "=", division(num1, num2))

else:
    print("Operación no válida")
