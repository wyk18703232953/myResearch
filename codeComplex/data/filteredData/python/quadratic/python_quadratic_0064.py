import random

def main(n):
    # 生成规模为 n 的测试数据
    # 数组 a：生成 n 个随机整数
    a = [random.randint(0, 10**9) for _ in range(n)]
    # 查询数量 q：这里设为 n（也可根据需要调整）
    q = n
    # 生成 q 个随机区间 [l, r]（1-based）
    queries = []
    for _ in range(q):
        l = random.randint(1, n)
        r = random.randint(l, n)
        queries.append((l, r))

    # 原逻辑开始
    s = 0
    for i in range(n):
        for j in range(i):
            s ^= a[j] > a[i]

    for l, r in queries:
        s ^= (r - l + 1) * (r - l) // 2 % 2
        print(['even', 'odd'][s])


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)