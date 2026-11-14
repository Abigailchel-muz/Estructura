
# Ejercicio 2: Ordenamiento por inserción
# Ordenar las calificaciones de alumnos

calificaciones = [8, 5, 10, 7, 6, 9, 4]

print("Calificaciones originales:")
print(calificaciones)

# ============================================
# INICIO DEL MÉTODO DE ORDENAMIENTO INSERCIÓN
# ============================================

for i in range(1, len(calificaciones)):

    actual = calificaciones[i]
    j = i - 1

    while j >= 0 and calificaciones[j] > actual:
        calificaciones[j + 1] = calificaciones[j]
        j -= 1

    calificaciones[j + 1] = actual

# ============================================
# FIN DEL MÉTODO DE ORDENAMIENTO INSERCIÓN
# ============================================

print("\nCalificaciones ordenadas:")
print(calificaciones)
