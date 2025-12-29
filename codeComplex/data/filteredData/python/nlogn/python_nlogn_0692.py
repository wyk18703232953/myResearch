import random

def main(n):
    # 生成测试数据
    # n 为 b 的长度，m 随机生成（至少为 1）
    m = random.randint(1, max(1, 2 * n))
    b = [random.randint(1, 10**3) for _ in range(n)]
    g = [random.randint(1, 10**3) for _ in range(m)]

    mab = max(b)
    mig = min(g)
    if mab > mig:
        print(-1)
        return

    b = sorted(b, reverse=True)
    g = sorted(g)
    num = 0
    j = 0
    for i in range(n):
        k = 0
        l = 1
        while j < m and k < m - l and b[i] <= g[j]:
            if b[i] == g[j]:
                l = 0
            num += g[j]
            j += 1
            k += 1
        num += b[i] * (m - k)

    print(num)


if __name__ == "__main__":
    # 示例：调用 main，规模自定
    main(5)