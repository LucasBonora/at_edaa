import numpy as np


movimentos = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

def dentro_limite(x, y, n):
    return 0 <= x < n and 0 <= y < n

def tour_cavalo(x, y, tabuleiro, passo, n):
    if passo == n * n: 
        return True

    for dx, dy in movimentos:
        nx, ny = x + dx, y + dy
        if dentro_limite(nx, ny, n) and tabuleiro[nx][ny] == -1:
            tabuleiro[nx][ny] = passo
            if tour_cavalo(nx, ny, tabuleiro, passo + 1, n):
                return True
            tabuleiro[nx][ny] = -1  

    return False

def resolver_tour(n):
    tabuleiro = np.full((n, n), -1)  
    tabuleiro[0][0] = 0 
    
    if tour_cavalo(0, 0, tabuleiro, 1, n):
        print("Solução encontrada:")
        print(tabuleiro)
    else:
        print("Nenhuma solução encontrada.")

resolver_tour(8)
