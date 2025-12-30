import random

def main(n):
    # 生成测试数据
    # 权值数组 w，元素范围可自行调整
    w = [random.randint(1, 100) for _ in range(n)]
    # 查询次数 m，这里设为 n 次
    m = n
    # 随机生成 m 个区间 [l, r]，1 ≤ l ≤ r ≤ n
    queries = []
    for _ in range(m):
        l = random.randint(1, n)
        r = random.randint(l, n)
        queries.append((l, r))

    # 原始逻辑开始
    c = 0
    for i in range(n):
        for j in range(i + 1, n):
            if w[i] > w[j]:
                c += 1
    c %= 2  # 0 或 1

    for l, r in queries:
        x = r - l + 1
        if x != 1 and (x * (x - 1) // 2) % 2:
            c = not c
        if c:
            print("odd")
        else:
            print("even")


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)