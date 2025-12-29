import random

def main(n):
    # 生成测试数据
    # n: 列数
    # 随机生成 m 行，其中每行有 50% 概率是 k[0] == 1 的有效行
    random.seed(0)
    m = max(1, n)  # 简单设定：m 与 n 同规模
    cols = [random.randint(1, 10**6) for _ in range(n)]

    rows = []
    for _ in range(m):
        t = random.randint(0, 1)  # 模拟 k[0]，0 或 1
        x = random.randint(1, 10**6)
        if t == 1:
            rows.append(x)

    # 原逻辑开始
    ans = n + m
    cols.sort()
    rows.sort()
    cols.append(int(1e9))
    j = 0
    rem = 0

    for i in cols:
        while j < len(rows) and rows[j] < i:
            j += 1
        ans = min(ans, len(rows) - j + rem)
        rem += 1

    print(ans)


if __name__ == "__main__":
    # 示例调用
    main(10)