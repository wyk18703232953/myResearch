import random

def main(n: int):
    # 生成测试数据：
    # 在合理范围内随机生成 m, k, l
    # 保证 m >= 1，k,l >= 0
    m = random.randint(1, max(1, n))       # 1 ≤ m ≤ n
    k = random.randint(0, n)               # 0 ≤ k ≤ n
    l = random.randint(0, n)               # 0 ≤ l ≤ n

    # 原逻辑
    if k + l > n:
        ans = -1
    else:
        x = (k + l) // m + (1 if (k + l) % m != 0 else 0)
        if x * m > n:
            ans = -1
        else:
            ans = x

    # 输出：先输出生成的参数，再输出结果，方便检查
    print(n, m, k, l, ans)


if __name__ == "__main__":
    # 可以在这里指定规模 n 的测试，例如 n = 100
    main(100)