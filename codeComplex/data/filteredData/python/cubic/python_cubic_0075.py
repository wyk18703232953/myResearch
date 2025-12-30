import random

def main(n):
    """
    n 为规模参数，用来生成 N, M, K 以及 K 对坐标的测试数据。
    可根据需要自行调整生成规则。
    """
    # 1. 根据 n 生成测试数据（这里给出一种示例规则）
    #    你可以根据实际需求修改 N, M, K 的生成方式
    N = max(1, n)        # 行数
    M = max(1, n)        # 列数
    # 至少 1 个点，最多不超过 N*M 且与 n 相关
    K = max(1, min(N * M, n // 2 + 1))

    # 随机生成 K 个点坐标 (1-based)
    inputs = []
    used = set()
    for _ in range(K):
        # 允许重复也没问题，如需要不重复则用 used 控制
        while True:
            x = random.randint(1, N)
            y = random.randint(1, M)
            if (x, y) not in used:
                used.add((x, y))
                break
        inputs.extend([x, y])

    # 2. 原逻辑（去掉文件读写，封装为 main(n) 的内部计算）
    map_max_dist = [[5000 for _ in range(M)] for _ in range(N)]

    p = 0
    while p <= K * 2 - 2:
        x, y = inputs[p] - 1, inputs[p + 1] - 1
        for r in range(N):
            for c in range(M):
                dist = abs(x - r) + abs(y - c)
                if dist < map_max_dist[r][c]:
                    map_max_dist[r][c] = dist
        p += 2

    max_val = 0
    max_index = (0, 0)
    for i in range(N):
        for j in range(M):
            if map_max_dist[i][j] > max_val:
                max_val = map_max_dist[i][j]
                max_index = (i, j)

    # 原程序输出到文件，这里直接打印
    print(f"{max_index[0] + 1} {max_index[1] + 1}")


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时按需修改或从外部调用 main(n)
    main(10)