
# Ejercicio 1: Ordenamiento por burbuja
# Ordenar los precios de una tienda

precios = [250, 100, 450, 80, 300, 150, 500, 200]

print("Precios originales:")
print(precios)

# ==========================================
# INICIO DEL MÉTODO DE ORDENAMIENTO BURBUJA
# ==========================================

for i in range(len(precios) - 1):
    for j in range(len(precios) - 1 - i):

        if precios[j] > precios[j + 1]:
            precios[j], precios[j + 1] = (
                precios[j + 1], precios[j]
            )

# ==========================================
# FIN DEL MÉTODO DE ORDENAMIENTO BURBUJA
# ==========================================

print("\nPrecios ordenados de menor a mayor:")
print(precios)
