import random

def main(n):
    # 生成测试数据
    # 约束：1 <= k <= n
    k = random.randint(1, n)
    a = [random.randint(0, 100) for _ in range(n)]
    t = [random.randint(0, 1) for _ in range(n)]

    ans = 0
    m = 0

    # 原逻辑开始
    for i in range(n):
        if t[i]:
            ans += a[i]
            a[i] = 0

    cf = [0] * (n + 1)
    for i in range(1, n + 1):
        cf[i] = cf[i - 1] + a[i - 1]

    for i in range(n - k + 1):
        m = max(m, cf[i + k] - cf[i])

    print(ans + m)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)