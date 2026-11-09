def kruskal(vertices, aristas):
    padre = {vertice: vertice for vertice in vertices}
    rango = {vertice: 0 for vertice in vertices}

    def encontrar(x):
        if padre[x] != x:
            padre[x] = encontrar(padre[x])
        return padre[x]

    def unir(a, b):
        raiz_a = encontrar(a)
        raiz_b = encontrar(b)
        if raiz_a == raiz_b:
            return False
        if rango[raiz_a] < rango[raiz_b]:
            padre[raiz_a] = raiz_b
        elif rango[raiz_a] > rango[raiz_b]:
            padre[raiz_b] = raiz_a
        else:
            padre[raiz_b] = raiz_a
            rango[raiz_a] += 1
        return True

    aristas.sort(key=lambda x: x[2])
    arbol = []
    costo_total = 0
    for a, b, peso in aristas:
        if unir(a, b):
            arbol.append((a, b, peso))
            costo_total += peso
        if len(arbol) == len(vertices) - 1:
            break
    return arbol, costo_total

vertices = ['A', 'B', 'C', 'D']
aristas = [('A', 'B', 1), ('A', 'C', 4), ('B', 'C', 2), ('B', 'D', 5), ('C', 'D', 3)]
arbol, costo = kruskal(vertices, aristas)
print('ALGORITMO DE KRUSKAL')
print('Aristas seleccionadas:')
print('----------------------')
for arista in arbol:
    print(arista)
print('Costo total:', costo)
