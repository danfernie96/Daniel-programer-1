nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))
nota4 = float(input("Ingrese la nota 4: "))

# Calcular el promedio
promedio = (nota1 + nota2 + nota3 + nota4) / 4

# Clasificar el rendimiento del estudiante
if 4 <= promedio <= 5:
    rendimiento = "Excelente"
elif 3 <= promedio < 4:
    rendimiento = "Bien"
else:
    rendimiento = "Necesita mejorar"

# Mostrar el resultado
print(f"El rendimiento del estudiante es: {rendimiento}")

# aplicacion de descuento

if rendimiento = "Excelente":
    print(f"su tarifa tiene descuento de 20%")
