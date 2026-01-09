from collections import deque

def main(n):
    # Interpret n as grid size; ensure at least 2x2 grid
    if n < 2:
        n = 2
    N = n
    M = n

    # Deterministically generate K and T based on n
    # Use K starting points along the main diagonal (or until we run out of cells)
    K = n
    T = []
    for i in range(1, K + 1):
        x = (i - 1) % N + 1
        y = (i - 1) % M + 1
        T.extend([x, y])

    graph = [[0] * (M + 1) for _ in range(N + 1)]
    queue = deque()
    for i in range(0, 2 * K - 1, 2):
        graph[T[i]][T[i + 1]] = 1
        queue.append((T[i], T[i + 1]))

    x, y = 0, 0
    while queue:
        x, y = queue.popleft()
        x_moves = [x - 1, x + 1, x, x]
        y_moves = [y, y, y - 1, y + 1]
        for i in range(len(x_moves)):
            if 0 < x_moves[i] <= N and 0 < y_moves[i] <= M:
                if graph[x_moves[i]][y_moves[i]] == 0:
                    x = x_moves[i]
                    y = y_moves[i]
                    graph[x_moves[i]][y_moves[i]] = 1
                    queue.append((x_moves[i], y_moves[i]))

    # print(f"{x} {y}")
    pass
if __name__ == "__main__":
    main(10)