import random

def main(n: int):
    # 生成测试数据
    # n: 数组规模
    # a: 随机整数数组
    # m: 查询次数，示例设为 n（也可根据需要调整）
    random.seed(0)
    a = [random.randint(0, 10**9) for _ in range(n)]
    m = n

    # 预生成 m 个随机区间 [l, r]，1-based，且 l <= r
    queries = []
    for _ in range(m):
        if n == 0:
            queries.append((1, 1))
            continue
        l = random.randint(1, n)
        r = random.randint(l, n)
        queries.append((l, r))

    # 逻辑与原始代码一致
    parity = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                parity ^= 1

    res = []
    for l, r in queries:
        s = r - l + 1
        parity ^= (s * (s - 1) // 2) % 2
        res.append("odd" if parity else "even")

    print("\n".join(res))


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)