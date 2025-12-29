import random

def solve(n, m, x, t):
    r = [0] * n
    d = [0] * m
    ans = [0] * m
    cr = 0
    cd = 0
    for i in range(n + m):
        if t[i]:
            d[cd] = x[i]
            cd += 1
        else:
            r[cr] = x[i]
            cr += 1
    cn = 0
    for i in range(m - 1):
        mid = (d[i] + d[i + 1]) // 2
        while cn < n and r[cn] <= mid:
            cn += 1
            ans[i] += 1
    ans[-1] += n - sum(ans)
    return ' '.join(str(i) for i in ans)


def main(n):
    # 生成测试数据：
    # n: 类型为0的元素个数
    # 随机生成 m，满足 1 <= m <= max(1, n)
    m = random.randint(1, max(1, n))

    # 一共需要 n + m 个位置
    total = n + m

    # 构造 t，使得其中恰好有 n 个 0 和 m 个 1
    t = [0] * n + [1] * m
    random.shuffle(t)

    # 生成严格递增的 x（原题通常是有序坐标/时间等）
    # 为简单起见，生成一个随机递增序列
    x = []
    cur = 0
    for _ in range(total):
        cur += random.randint(1, 10)
        x.append(cur)

    result = solve(n, m, x, t)
    print("n:", n)
    print("m:", m)
    print("x:", x)
    print("t:", t)
    print("answer:", result)


# 示例调用
if __name__ == "__main__":
    main(5)