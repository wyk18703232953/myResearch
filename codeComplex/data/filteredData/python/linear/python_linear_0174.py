import random

def main(n):
    # 生成测试数据
    # n: 数组规模
    # 随机生成 1 <= k <= n
    k = random.randint(1, n)
    # 随机生成 a[i] 在 [1, 10]，t[i] 在 {0, 1}
    a = [random.randint(1, 10) for _ in range(n)]
    t = [random.randint(0, 1) for _ in range(n)]

    p = [0] * (n + 1)
    now = 0
    for i in range(n):
        if t[i] == 1:
            now += a[i]
        p[i + 1] = p[i]
        if t[i] == 0:
            p[i + 1] += a[i]

    s = 0
    for i in range(n - k + 1):
        s = max(s, p[i + k] - p[i])

    ans = now + s
    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：调用 main(10)，可根据需要修改规模
    main(10)