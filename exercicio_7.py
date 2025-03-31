import numpy as np

INF = float('inf')  


grafo = [
    [0, 3, INF, 7, INF, 8],
    [3, 0, 2, INF, 5, INF],
    [INF, 2, 0, 1, 4, INF],
    [7, INF, 1, 0, 3, 6],
    [INF, 5, 4, 3, 0, 2],
    [8, INF, INF, 6, 2, 0]
]

def floyd_warshall(grafo):
    n = len(grafo)
    dist = np.array(grafo)  


    for k in range(n):
        for i in range(n):
            for j in range(n):
                
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


menores_tempos = floyd_warshall(grafo)


print("Matriz de menores tempos entre os bairros:")
print(menores_tempos)
