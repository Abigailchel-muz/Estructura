# Intercalación de dos listas previamente ordenadas

def intercalar(a, b):
    resultado = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            resultado.append(a[i]); i += 1
        else:
            resultado.append(b[j]); j += 1
    resultado.extend(a[i:])
    resultado.extend(b[j:])
    return resultado

if __name__ == "__main__":
    grupo_a = [65, 72, 85, 91]
    grupo_b = [60, 78, 83, 95]
    print("Grupo A:", grupo_a)
    print("Grupo B:", grupo_b)
    print("Resultado:", intercalar(grupo_a, grupo_b))
