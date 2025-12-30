import random

def main(n: int):
    # 生成测试数据：n、s、a
    # s 为随机不重复整数，a 为正整数权重
    # 可根据需要调整数据生成策略
    s = random.sample(range(1, 10 ** 6), n)  # 随机且互不相同
    a = [random.randint(1, 10 ** 6) for _ in range(n)]

    t = 3 * 10 ** 9
    q = [0] * n

    for i in range(n - 1, -1, -1):
        u = 10 ** 8
        for j in range(i - 1, -1, -1):
            if s[i] > s[j]:
                u = min(u, a[j])
        q[i] = u

    for i in range(n):
        for j in range(i + 1, n):
            if s[i] < s[j]:
                t = min(t, a[i] + a[j] + q[i])

    ans = t if t <= sum(a) else -1
    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)