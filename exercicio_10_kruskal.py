class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n  
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u]) 
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])  
    ds = DisjointSet(n)
    mst = []
    total_cost = 0

    for u, v, weight in edges:
        if ds.find(u) != ds.find(v): 
            ds.union(u, v)
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost

edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1), (1, 3, 2), (2, 3, 4), (3, 4, 2), (4, 5, 6)]
n = 6  

mst, total_cost = kruskal(n, edges)
print("Árvore Geradora Mínima:", mst)
print("Custo Total:", total_cost)
