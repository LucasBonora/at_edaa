from itertools import permutations

def calcular_distancia(caminho, matriz_distancia):
    distancia_total = 0
    for i in range(len(caminho) - 1):
        distancia_total += matriz_distancia[caminho[i]][caminho[i + 1]]
    distancia_total += matriz_distancia[caminho[-1]][caminho[0]]  
    return distancia_total

def tsp_forca_bruta(matriz_distancia):
    cidades = list(range(len(matriz_distancia)))
    melhor_rota = None
    menor_distancia = float('inf')

    for perm in permutations(cidades[1:]):  
        rota = [0] + list(perm)
        dist = calcular_distancia(rota, matriz_distancia)
        if dist < menor_distancia:
            menor_distancia = dist
            melhor_rota = rota

    return melhor_rota, menor_distancia

matriz_exemplo = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

rota, distancia = tsp_forca_bruta(matriz_exemplo)
print(f"Melhor Rota: {rota} com distância {distancia}")
