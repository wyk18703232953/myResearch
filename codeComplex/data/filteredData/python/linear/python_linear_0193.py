import random

def main(n):
    # 生成测试数据
    # 约束猜测自原程序：时间 t 不超过 1000（因 f = [0]*1001）
    # 为保证有意义，令：
    #   1 <= n
    #   1 <= t <= 1000
    #   1 <= a, b, c <= 10
    t = random.randint(1, 1000)
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)

    # 生成 n 个时间点，每个在 [1, t] 内
    l = [random.randint(1, t) for _ in range(n)]

    # 原逻辑
    f = [0] * 1001
    for i in l:
        f[i] += 1

    tmp = 0
    for i in range(1, t):
        tmp += (t - i) * f[i]

    tmp = n * a + tmp * c - tmp * b
    ans = max(n * a, tmp)

    print(ans)


if __name__ == "__main__":
    # 示例：规模 n=10
    main(10)