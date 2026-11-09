def floyd(matriz):
    n = len(matriz)
    distancias = [fila[:] for fila in matriz]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                nueva = distancias[i][k] + distancias[k][j]
                if nueva < distancias[i][j]:
                    distancias[i][j] = nueva
    return distancias

INF = float('inf')
grafo = [[0, 3, 10], [INF, 0, 2], [INF, INF, 0]]
resultado = floyd(grafo)
print('ALGORITMO DE FLOYD')
print('Matriz de distancias minimas:')
print('----------------------------')
for fila in resultado:
    print(fila)
