import random

def main(n):
    # 生成测试数据
    # n: V 的规模
    # m: 按某种策略生成，至少保证 m >= n 以产生足够的区间
    m = max(1, n * 2)

    # 生成 V：n 个随机整数，范围 [1, 1e6]
    V = [random.randint(1, 10**6) for _ in range(n)]

    # 生成区间 (x1, x2, y)
    # 仅当 x1 == 1 时，x2 会被用到，因此随机部分区间的 x1 设为 1
    intervals = []
    for _ in range(m):
        x1 = random.choice([1, 2])  # 一部分为 1，一部分为其他
        x2 = random.randint(1, 10**6)
        y = random.randint(1, 10**6)
        intervals.append((x1, x2, y))

    # ---- 原始逻辑开始 ----
    V.sort()
    V.append(10 ** 9)
    n_local = n + 1  # 对应原代码中的 n += 1

    X2 = []
    for (x1, x2, y) in intervals:
        if x1 == 1:
            X2.append(x2)
    X2.sort()

    k = len(X2)
    i = 0
    j = 0
    ans = 10 ** 9 + 7
    c = 0

    while i < n_local:
        while j < k:
            if X2[j] < V[i]:
                c += 1
                j += 1
            else:
                break
        ans = min(ans, k - c + i)
        i += 1

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)