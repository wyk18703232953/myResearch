def main(n: int):
    import random

    # 生成测试数据
    # 规模参数 n：数组长度
    # 这里设置 m 和 k 为与 n 同规模的随机值，可按需求修改
    m = max(1, min(n, 10))            # m 至少为 1，且不超过 10 或 n
    k = random.randint(-10, 10)       # k 在一个小范围内随机
    a = [0] + [random.randint(-10, 10) for _ in range(n)]  # 1-based

    # 以下为原逻辑
    p = [0] * (n + 1)
    for i in range(1, n + 1):
        p[i] = p[i - 1] + a[i]

    INF = 10 ** 16
    s = [INF for _ in range(m)]
    s[0] = k
    ans = 0
    for i in range(1, n + 1):
        ans = max(ans, p[i] - min(s))
        idx = i % m
        s[idx] = min(s[idx], p[i])
        s[idx] += k

    print(ans)


if __name__ == "__main__":
    # 示例调用，规模可自行调整
    main(10)