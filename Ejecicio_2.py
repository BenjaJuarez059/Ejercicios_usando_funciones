def calcular_objetivo_ml(peso_kg, nivel_actividad):
    base = peso_kg * 35  # Base en ml por kg
    if nivel_actividad == "bajo":
        return base * 0.9  # -10%
    elif nivel_actividad == "alto":
        return base * 1.1  # +10%
    else:  # medio o cualquier otro valor se considera medio
        return base  # 0%

def estado_hidratacion(consumo_ml, objetivo_ml):
    porcentaje = (consumo_ml / objetivo_ml) * 100
    diferencia = abs(porcentaje - 100)

    if porcentaje == 100:
        return "Has alcanzado tu objetivo."
    elif porcentaje < 100:
        return f"Te falta un {diferencia:.1f}% para llegar."
    else:
        return f"Has excedido tu objetivo en {diferencia:.1f}%."

# Función auxiliar para pedir números con validación
def pedir_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Por favor, ingresa un número positivo.")
            else:
                return valor
        except ValueError:
            print("Error: Ingresa un número válido.")

# Función auxiliar para pedir nivel de actividad
def pedir_nivel_actividad():
    while True:
        nivel = input("Ingresa tu nivel de actividad (bajo, medio o alto): ").strip().lower()
        if nivel in ["bajo", "medio", "alto"]:
            return nivel
        else:
            print("Nivel no válido. Por favor escribe 'bajo', 'medio' o 'alto'.")

# Programa principal
peso = pedir_float("Ingresa tu peso en kg: ")
nivel = pedir_nivel_actividad()
consumo = pedir_float("Ingresa la cantidad de agua que has consumido hoy (en ml): ")

objetivo = calcular_objetivo_ml(peso, nivel)
mensaje = estado_hidratacion(consumo, objetivo)

print(f"\nTu objetivo diario de agua es: {objetivo:.0f} ml")
print(mensaje)