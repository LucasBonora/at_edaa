import random
matriz_exemplo = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]


def calcular_distancia_rota(rota, matriz_distancia):
    return sum(matriz_distancia[rota[i]][rota[i+1]] for i in range(len(rota)-1)) + matriz_distancia[rota[-1]][rota[0]]

def gerar_populacao(n, tamanho):
    return [random.sample(range(n), n) for _ in range(tamanho)]

def crossover(pai1, pai2):
    corte = random.randint(1, len(pai1)-2)
    filho = pai1[:corte] + [c for c in pai2 if c not in pai1[:corte]]
    return filho

def mutacao(rota):
    i, j = random.sample(range(len(rota)), 2)
    rota[i], rota[j] = rota[j], rota[i]

def algoritmo_genetico(matriz_distancia, geracoes=100, tamanho_pop=50):
    populacao = gerar_populacao(len(matriz_distancia), tamanho_pop)

    for _ in range(geracoes):
        populacao = sorted(populacao, key=lambda r: calcular_distancia_rota(r, matriz_distancia))
        nova_pop = populacao[:10]  
        while len(nova_pop) < tamanho_pop:
            pai1, pai2 = random.sample(populacao[:20], 2)
            filho = crossover(pai1, pai2)
            if random.random() < 0.1:  
                mutacao(filho)
            nova_pop.append(filho)
        populacao = nova_pop

    melhor_rota = min(populacao, key=lambda r: calcular_distancia_rota(r, matriz_distancia))
    return melhor_rota, calcular_distancia_rota(melhor_rota, matriz_distancia)

rota, distancia = algoritmo_genetico(matriz_exemplo)
print(f"Melhor rota genética: {rota} com distância {distancia}")
