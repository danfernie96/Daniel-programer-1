# Definir tarifas por minuto para diferentes regiones
T_EUU = 900
T_CANADA = 800
T_EUROPA = 950
T_RESTO_DEL_MUNDO = 1250

# Definir porcentaje de descuento
porcentaje_descuento = 0.2

# Pedir al usuario ingresar la duración de la llamada y la región
duracion = float(input("Ingrese la duración de la llamada en minutos: "))
region = input("Ingrese la región desde donde realiza la llamada (EEUU, CANADA, EUROPA o RESTO_DEL_MUNDO): ")

# Calcular el costo sin descuento
if region== "EEUU":
    costo_sin_descuento = duracion * T_EUU
elif region == "CANADA":
    costo_sin_descuento = duracion * T_CANADA
elif region== "EUROPA":
    costo_sin_descuento = duracion * T_EUROPA
else:
    costo_sin_descuento = duracion * T_RESTO_DEL_MUNDO

# Aplicar descuento si la duración es mayor a 15 minutos
if duracion > 15:
    descuento = costo_sin_descuento * porcentaje_descuento
    costo_con_descuento = costo_sin_descuento - descuento
    print(f"Su tarifa tiene un descuento del 20% y es: {costo_con_descuento}")
else:
    print(f"Su tarifa es: {costo_sin_descuento}")