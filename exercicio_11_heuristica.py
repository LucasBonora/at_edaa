import numpy as np

movimentos = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

def dentro_limite(x, y, n):
    return 0 <= x < n and 0 <= y < n

def contar_movimentos(x, y, tabuleiro, n):
    count = 0
    for dx, dy in movimentos:
        nx, ny = x + dx, y + dy
        if dentro_limite(nx, ny, n) and tabuleiro[nx][ny] == -1:
            count += 1
    return count

def warnsdorff_tour(x, y, tabuleiro, passo, n):
    if passo == n * n:
        return True

    movimentos_ordenados = sorted(
        [(dx, dy) for dx, dy in movimentos],
        key=lambda move: contar_movimentos(x + move[0], y + move[1], tabuleiro, n)
    )

    for dx, dy in movimentos_ordenados:
        nx, ny = x + dx, y + dy
        if dentro_limite(nx, ny, n) and tabuleiro[nx][ny] == -1:
            tabuleiro[nx][ny] = passo
            if warnsdorff_tour(nx, ny, tabuleiro, passo + 1, n):
                return True
            tabuleiro[nx][ny] = -1  
    return False

def resolver_tour_warnsdorff(n):
    tabuleiro = np.full((n, n), -1)
    tabuleiro[0][0] = 0

    if warnsdorff_tour(0, 0, tabuleiro, 1, n):
        print("Solução encontrada com Warnsdorff:")
        print(tabuleiro)
    else:
        print("Nenhuma solução encontrada.")

resolver_tour_warnsdorff(8)
