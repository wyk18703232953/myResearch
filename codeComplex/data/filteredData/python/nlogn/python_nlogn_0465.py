import random

def max_profit(n, k, l, d):
    a = []
    p, i = 0, -1
    d = d.copy()  # 避免修改外部列表
    while len(a) != k - 1:
        p += 1
        i += 1
        if l[i] in d:
            a.append(p)
            p = 0
            d.remove(l[i])
    a.append(n - sum(a))
    print(*a)


def main(n):
    # 规模 n：数组长度，同时原代码中 n 也是长度
    # 这里随机生成 l，并随机选择 k（1 <= k <= n）
    random.seed(0)
    l = [random.randint(1, 100) for _ in range(n)]
    k = random.randint(1, n)

    d = sorted(l, reverse=True)[:k]
    print(sum(d))
    max_profit(n, k, l, d)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可按需修改
    main(10)