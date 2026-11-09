import heapq

def dijkstra(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    cola = [(0, inicio)]
    while cola:
        distancia, actual = heapq.heappop(cola)
        if distancia > distancias[actual]:
            continue
        for vecino, peso in grafo[actual]:
            nueva = distancia + peso
            if nueva < distancias[vecino]:
                distancias[vecino] = nueva
                heapq.heappush(cola, (nueva, vecino))
    return distancias

grafo = {'A': [('B', 4), ('C', 2)], 'B': [('D', 5)], 'C': [('B', 1), ('D', 8)], 'D': []}
resultado = dijkstra(grafo, 'A')
print('ALGORITMO DE DIJKSTRA')
print('Vertice inicial: A')
print('----------------------')
for nodo, distancia in resultado.items():
    print(f'Distancia hasta {nodo}: {distancia}')
