import heapq

def prim(n, graph):
    mst = []  
    visited = [False] * n
    min_heap = [(0, 0, -1)]  
    total_cost = 0

    while min_heap:
        cost, u, prev = heapq.heappop(min_heap)
        if visited[u]:
            continue

        visited[u] = True
        if prev != -1:
            mst.append((prev, u, cost))
            total_cost += cost

        for v, weight in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (weight, v, u))

    return mst, total_cost

graph = {
    0: [(1, 4), (2, 3)],
    1: [(0, 4), (2, 1), (3, 2)],
    2: [(0, 3), (1, 1), (3, 4)],
    3: [(1, 2), (2, 4), (4, 2)],
    4: [(3, 2), (5, 6)],
    5: [(4, 6)]
}

n = len(graph)
mst, total_cost = prim(n, graph)
print("Árvore Geradora Mínima:", mst)
print("Custo Total:", total_cost)
