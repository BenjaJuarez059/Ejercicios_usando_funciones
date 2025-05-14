def calcular_gasto_promedio(total_gastado, numero_dias):
    return total_gastado / numero_dias

def calcular_balance(presupuesto, gasto_promedio):
    return presupuesto - gasto_promedio

# Función para pedir un número flotante al usuario
def pedir_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Error: Debes ingresar un número válido (puede tener decimales).")

# Función para pedir un número entero al usuario
def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")

# Programa principal
presupuesto = pedir_float("Ingresa el presupuesto total del viaje: ")
total_gastado = pedir_float("Ingresa el total gastado hasta ahora: ")
numero_dias = pedir_entero("Ingresa el número de días que llevas de viaje: ")

gasto_promedio = calcular_gasto_promedio(total_gastado, numero_dias)
balance_diario = calcular_balance(presupuesto / numero_dias, gasto_promedio)

print(f"\nGasto promedio diario: ${gasto_promedio:.2f}")
print(f"Balance diario (lo que te queda por día): ${balance_diario:.2f}")