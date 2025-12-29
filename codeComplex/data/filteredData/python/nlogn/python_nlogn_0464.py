import random

def max_profit(n, k, l, d):
    a = []
    s, p, i = 0, 0, -1
    while len(a) != k - 1:
        p += 1
        i += 1
        if l[i] in d:
            s += l[i]
            a.append(p)
            p = 0
            d.remove(l[i])
    print(s + d[0])
    a.append(n - sum(x for x in a))
    print(*a)


def main(n):
    # 生成测试数据：
    # k 在 [1, n] 内（保证 k 不超过 n）
    k = random.randint(1, n)

    # l 为长度为 n 的正整数数组，这里生成 [1, 100] 区间随机数
    l = [random.randint(1, 100) for _ in range(n)]

    # 构造 d：为 l 中最大的 k 个元素
    m = l[:]
    m.sort(reverse=True)
    d = m[:k]

    max_profit(n, k, l, d)


if __name__ == "__main__":
    # 示例：调用 main(10)，可按需修改 n 测试规模
    main(10)