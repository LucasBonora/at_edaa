import numpy as np

bairros = ["A", "B", "C", "D", "E", "F"]
num_bairros = len(bairros)

matriz_adj = np.full((num_bairros, num_bairros), np.inf)

conexoes = {
    "A": [("B", 4), ("C", 2)],
    "B": [("A", 4), ("D", 5)],
    "C": [("A", 2), ("D", 8), ("E", 3)],
    "D": [("B", 5), ("C", 8), ("F", 6)],
    "E": [("C", 3), ("F", 1)],
    "F": [("D", 6), ("E", 1)]
}

for bairro, vizinhos in conexoes.items():
    i = bairros.index(bairro)
    for vizinho, distancia in vizinhos:
        j = bairros.index(vizinho)
        matriz_adj[i][j] = distancia
        matriz_adj[j][i] = distancia  

print("Matriz de Adjacência:")
print(matriz_adj)
