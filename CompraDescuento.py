# Pedir al usuario el total de la compra
total_compra = float(input("Introduce el total de la compra: "))

# Calcular el descuento del 15%
descuento = total_compra * 0.15

# Calcular el precio final después del descuento
precio_final = total_compra - descuento

# Mostrar el precio final al usuario
print("El precio final de la compra con el descuento del 15% es:", precio_final)

