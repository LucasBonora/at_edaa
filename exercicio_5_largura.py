from collections import deque

metro = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'E'],
    'E': ['B', 'D', 'F'],
    'F': ['C', 'E']
}
def bfs(metro, inicio):
    visitados = set() 
    fila = deque([inicio])  

    while fila:
        estacao = fila.popleft()  
        
        if estacao not in visitados:
            print(estacao, end=" ") 
            visitados.add(estacao)
            
            for vizinho in metro[estacao]:
                if vizinho not in visitados:
                    fila.append(vizinho)

print("\nBFS a partir de A:")
bfs(metro, 'A')


