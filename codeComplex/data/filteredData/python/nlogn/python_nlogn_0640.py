import random

def main(n):
    # 生成测试数据
    # n: 垂直线数量
    # m: 水平线“候选”数量（含非 a==1 的情况）
    # 这里令 m 与 n 同规模，可根据需要调整
    m = n

    # 垂直线位置：随机递增生成
    vert = []
    cur = 0
    for _ in range(n):
        cur += random.randint(1, 10)
        vert.append(cur)

    # 水平线数据 (a, b, c)
    horiz_raw = []
    for _ in range(m):
        a = random.choice([1, 2, 3])  # a=1 的才会加入有效列表
        b = random.randint(0, 10 * n)
        c = random.randint(0, 10)     # c 实际在原算法中未使用
        horiz_raw.append((a, b, c))

    # 原始逻辑开始
    horiz = []
    for a, b, c in horiz_raw:
        if a == 1:
            horiz.append(b)

    vert.sort()
    vert.append(1000000000)
    vert.append(2000000000)
    horiz.sort()

    oof = [0] * (n + 2)
    b_idx = 0
    for h in horiz:
        while True:
            if h < vert[b_idx]:
                oof[b_idx] += 1
                break
            else:
                b_idx += 1

    mini = 1000000
    bad = len(horiz)
    for i in range(n + 1):
        bad -= oof[i]
        if bad + i < mini:
            mini = bad + i

    print(mini)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)