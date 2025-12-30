import random

def main(n):
    # 规模参数 n 用来生成测试数据
    # 生成 n 个男孩技能值, m 个女孩技能值 (这里设定 m = n 或 n+1 随机)
    m = random.randint(n, n + 5)  # m 至少为 n，稍微大一点
    # 技能值范围可自行调整
    b = [random.randint(1, 100) for _ in range(n)]
    g = [random.randint(1, 100) for _ in range(m)]

    # 原始逻辑开始
    if max(b) > min(g):
        print(-1)
        return

    total = m * sum(b)
    b.sort()
    g.sort()
    # 为了不破坏原始 b/g 内容，复制一份进行操作
    boys = b[:]
    girls = g[:]

    while len(girls) > 0:
        current = 0
        count = 1
        if len(boys) > 0:
            current = boys.pop()
        while len(girls) > 0 and girls[-1] > current and count < m:
            total += girls[-1] - current
            girls.pop()
            count += 1
        while len(girls) > 0 and girls[-1] == current:
            girls.pop()

    print(total)


if __name__ == "__main__":
    # 示例：运行 main(5)
    main(5)