
# Ejercicio 3: Ordenamiento por selección
# Ordenar los tiempos de una competencia

tiempos = [45, 32, 50, 28, 39, 35, 41]

print("Tiempos originales:")
print(tiempos)

# ============================================
# INICIO DEL MÉTODO DE ORDENAMIENTO SELECCIÓN
# ============================================

for i in range(len(tiempos) - 1):

    menor = i

    for j in range(i + 1, len(tiempos)):
        if tiempos[j] < tiempos[menor]:
            menor = j

    tiempos[i], tiempos[menor] = (
        tiempos[menor], tiempos[i]
    )

# ============================================
# FIN DEL MÉTODO DE ORDENAMIENTO SELECCIÓN
# ============================================

print("\nTiempos ordenados de menor a mayor:")
print(tiempos)

print("\nEl tiempo más rápido es:", tiempos[0])
