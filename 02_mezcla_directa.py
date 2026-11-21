# Mezcla directa: fusiona bloques de tamaño 1, 2, 4, ...

def fusionar(a, b):
    resultado = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            resultado.append(a[i]); i += 1
        else:
            resultado.append(b[j]); j += 1
    return resultado + a[i:] + b[j:]

def mezcla_directa(datos):
    datos = datos.copy()
    ancho = 1
    while ancho < len(datos):
        for inicio in range(0, len(datos), 2 * ancho):
            medio = min(inicio + ancho, len(datos))
            fin = min(inicio + 2 * ancho, len(datos))
            datos[inicio:fin] = fusionar(datos[inicio:medio], datos[medio:fin])
        print(f"Pasada con bloques de {ancho}:", datos)
        ancho *= 2
    return datos

if __name__ == "__main__":
    precios = [249, 89, 450, 120, 75, 310, 199]
    print("Original:", precios)
    print("Ordenado:", mezcla_directa(precios))
