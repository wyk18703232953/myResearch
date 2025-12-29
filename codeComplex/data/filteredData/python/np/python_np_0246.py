import random


def main(n: int):
    # 生成参数 m, k
    # 限制：m <= n，k <= n^2
    if n <= 0:
        return
    m = random.randint(1, n)
    max_k = n * n
    # 适当限制 k 避免过大
    k = random.randint(0, max_k)

    # 生成 a 数组（浮点数）
    # 例如在 [0, 100) 范围内
    a = [random.uniform(0, 100) for _ in range(n)]

    # 初始化 add 矩阵
    add = [[0.0] * n for _ in range(n + 1)]

    # 随机生成 k 条三元组 (xi, yi, ci)
    # xi, yi 从 1..n，ci 为随机整数
    for _ in range(k):
        xi = random.randint(1, n)
        yi = random.randint(1, n)
        ci = random.randint(-50, 50)
        add[xi - 1][yi - 1] = float(ci)

    minf = float('-inf')
    dp = [[minf] * (1 << n) for _ in range(n + 1)]
    dp[n][0] = 0.0

    for bitset in range(1 << n):
        if bin(bitset).count('1') >= m:
            continue
        for i in range(n + 1):
            if dp[i][bitset] == minf:
                continue
            base = dp[i][bitset]
            for j in range(n):
                if (bitset >> j) & 1:
                    continue
                nb = bitset | (1 << j)
                val = base + a[j] + add[i][j]
                if val > dp[j][nb]:
                    dp[j][nb] = val

    ans = int(max(max(row) for row in dp) + 1e-7)
    print(ans)


if __name__ == '__main__':
    # 示例：n 可在此处指定，或在外部调用 main(n)
    main(5)