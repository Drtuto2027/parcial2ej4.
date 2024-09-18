def verificar_valor(valor):
    if valor is None:
       print("El valor no está asignado (es None).")
    else:
       print(f"El valor es: {valor}")

# Prueba con None
verificar_valor(None)

# Prueba con otro valor
verificar_valor(10)
# pedir la edad del uauario

edad =int(input("ingrese su edad:"))

#verificar si es amyor de edad

es_mayor_de_edad_ = edad >=18

# moatrar el resultado

print(F"¿eres mayor de edad?:{es_mayor_de_edad}")