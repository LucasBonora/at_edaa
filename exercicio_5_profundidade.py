from collections import deque

metro = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'E'],
    'E': ['B', 'D', 'F'],
    'F': ['C', 'E']
}

def dfs(metro, inicio):
    visitados = set()  
    pilha = [inicio]   

    while pilha:
        estacao = pilha.pop()  
        
        if estacao not in visitados:
            print(estacao, end=" ") 
            visitados.add(estacao)
            
           
            for vizinho in reversed(metro[estacao]):
                if vizinho not in visitados:
                    pilha.append(vizinho)

print("DFS a partir de A:")
dfs(metro, 'A')

