import heapq  

grafo = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('D', 5)],
    'C': [('A', 2), ('D', 8), ('E', 3)],
    'D': [('B', 5), ('C', 8), ('F', 6)],
    'E': [('C', 3), ('F', 1)],
    'F': [('D', 6), ('E', 1)]
}
def dijkstra(grafo, inicio, destino):
   
    fila = [(0, inicio)]
   
    distancias = {no: float('inf') for no in grafo}
    distancias[inicio] = 0
   
    predecessores = {}

    while fila:
        distancia_atual, no_atual = heapq.heappop(fila)  

        
        if no_atual == destino:
            break

        for vizinho, peso in grafo[no_atual]:
            nova_distancia = distancia_atual + peso

            
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                heapq.heappush(fila, (nova_distancia, vizinho))
                predecessores[vizinho] = no_atual

    caminho = []
    no = destino
    while no in predecessores:
        caminho.append(no)
        no = predecessores[no]
    caminho.append(inicio)
    caminho.reverse()

    return caminho, distancias[destino]

rota, custo = dijkstra(grafo, 'A', 'F')

print(f"Rota mais curta: {' -> '.join(rota)}")
print(f"Distância total: {custo} km")
