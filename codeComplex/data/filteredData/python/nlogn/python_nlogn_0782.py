import random

def main(n, seed=0):
    random.seed(seed)
    # 生成测试数据：严格递增的数组 a，长度为 n
    # 先生成随机差分，再前缀和得到 a
    max_step = 10
    diffs = [random.randint(1, max_step) for _ in range(n)]
    a = [0] * n
    a[0] = random.randint(0, 10)
    for i in range(1, n):
        a[i] = a[i-1] + diffs[i]

    # 随机生成 k，范围 [1, n]
    k = random.randint(1, n)

    # 原逻辑
    c = a[-1] - a[0]
    d = [a[i] - a[i - 1] for i in range(1, n)]
    d = sorted(d, reverse=True)
    c -= sum(d[:k - 1])

    print("n =", n)
    print("k =", k)
    print("a =", a)
    print("answer =", c)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)