from collections import deque
import random

def main(n):
    # 1. 根据规模 n 生成 N, M
    # 这里简单设定：N = n, M = n
    N = n
    M = n

    # 2. 生成若干起始点 K 和列表 T（长度为 2K）
    # 设定 K 与 n 有关，例如 K = max(1, n // 2)
    K = max(1, n // 2)

    # 随机生成 K 个起始坐标 (x, y)，范围在 [1, N] x [1, M]
    # T = [x1, y1, x2, y2, ...]
    T = []
    for _ in range(K):
        x = random.randint(1, N)
        y = random.randint(1, M)
        T.extend([x, y])

    # 3. 原逻辑封装（不再读写文件）
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

    # 4. 输出结果（直接打印）
    print(f"{x} {y}")


if __name__ == "__main__":
    # 示例调用，可按需修改 n
    main(10)