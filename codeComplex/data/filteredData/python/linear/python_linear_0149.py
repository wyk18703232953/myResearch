import random

def main(n: int):
    # 生成测试数据
    # p 取一个与 n 相关但不太小的值，避免退化，例如随机取 [1, 10*n] 内
    if n <= 0:
        return 0

    p = random.randint(1, max(1, 10 * n))
    # 生成 n 个非负整数，控制数值规模避免溢出
    a = [random.randint(0, 10**6) for _ in range(n)]

    # 原始逻辑
    k = sum(a)
    t = 0
    s = 0
    for i in range(0, n - 1):
        s += a[i]
        t = max(t, s % p + (k - s) % p)
    print(t)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)