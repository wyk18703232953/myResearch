import random

def main(n):
    # 生成测试数据：k 和长度为 n 的数组 a
    # 这里生成 k ∈ [1, 20]，a[i] ∈ [0, 2^k - 1]
    if n <= 0:
        print(0)
        return

    k = random.randint(1, 20)
    upper = (1 << k) - 1
    a = [random.randint(0, upper) for _ in range(n)]

    d = dict()
    d[0] = 1
    x = 0

    for val in a:
        x ^= val
        v = min(x, (1 << k) - x - 1)
        if v not in d:
            d[v] = 0
        d[v] += 1

    ans = 0
    for _, v in d.items():
        c1 = v // 2
        c2 = v - c1
        ans += c1 * (c1 - 1) // 2 + c2 * (c2 - 1) // 2

    print(n * (n - 1) // 2 + n - ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)