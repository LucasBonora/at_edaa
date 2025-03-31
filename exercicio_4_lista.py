bairros = ["A", "B", "C", "D", "E", "F"]
num_bairros = len(bairros)

conexoes = {
    "A": [("B", 4), ("C", 2)],
    "B": [("A", 4), ("D", 5)],
    "C": [("A", 2), ("D", 8), ("E", 3)],
    "D": [("B", 5), ("C", 8), ("F", 6)],
    "E": [("C", 3), ("F", 1)],
    "F": [("D", 6), ("E", 1)]
}

lista_adj = {bairro: [] for bairro in bairros}


for bairro, vizinhos in conexoes.items():
    for vizinho, distancia in vizinhos:
        lista_adj[bairro].append((vizinho, distancia))

print("\nLista de Adjacência:")
for bairro, vizinhos in lista_adj.items():
    print(f"{bairro}: {vizinhos}")
