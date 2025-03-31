matriz_exemplo = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def tsp_vizinho_mais_proximo(matriz_distancia):
    n = len(matriz_distancia)
    visitado = [False] * n
    rota = [0]  
    visitado[0] = True
    distancia_total = 0

    for _ in range(n - 1):
        atual = rota[-1]
        proxima_cidade = min(
            [(cidade, matriz_distancia[atual][cidade]) for cidade in range(n) if not visitado[cidade]],
            key=lambda x: x[1]
        )[0]
        rota.append(proxima_cidade)
        visitado[proxima_cidade] = True
        distancia_total += matriz_distancia[atual][proxima_cidade]

    distancia_total += matriz_distancia[rota[-1]][0] 
    return rota, distancia_total

rota, distancia = tsp_vizinho_mais_proximo(matriz_exemplo)
print(f"Melhor Rota Aproximada: {rota} com distância {distancia}")
