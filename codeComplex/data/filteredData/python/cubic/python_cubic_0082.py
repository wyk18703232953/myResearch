from collections import deque
import random


def main(n: int):
    # n: number of rows; also use n as number of columns for testing
    m = n

    # Generate random number of initial points k (at least 1, at most n*m)
    k = random.randint(1, min(n * m, max(1, n // 2)))

    # Generate k distinct random cells as starting points
    all_cells = [(i, j) for i in range(n) for j in range(m)]
    random.shuffle(all_cells)
    starts = all_cells[:k]

    # Build grid and BFS queue
    a = [[0] * m for _ in range(n)]
    dq = deque()
    for x, y in starts:
        a[x][y] = 1
        dq.append((x, y))

    x, y = -1, -1
    while dq:
        x, y = dq.popleft()
        for tx, ty in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= tx < n and 0 <= ty < m and not a[tx][ty]:
                a[tx][ty] = 1
                dq.append((tx, ty))

    # Output last filled cell in 1-based coordinates
    print(f'{x + 1} {y + 1}')


if __name__ == "__main__":
    # example run with n=10
    main(10)