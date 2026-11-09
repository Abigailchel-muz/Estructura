def warshall(matriz):
    n = len(matriz)
    alcance = [fila[:] for fila in matriz]
    for i in range(n):
        alcance[i][i] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                alcance[i][j] = int(alcance[i][j] or (alcance[i][k] and alcance[k][j]))
    return alcance

grafo = [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
resultado = warshall(grafo)
print('ALGORITMO DE WARSHALL')
print('Matriz de alcanzabilidad:')
print('------------------------')
for fila in resultado:
    print(fila)
