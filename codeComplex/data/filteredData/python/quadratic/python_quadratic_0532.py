import random

def main(n):
    # 生成测试数据
    # 约束：n 为 a 的长度，且需要 n + m == len(t)
    # 这里令 m = max(1, n // 2)，并保证 t 中恰好有 m 个 1
    if n <= 0:
        return

    m = max(1, n // 2)

    # 为了符合原逻辑，t 的长度为 n + m，且其中有 m 个 1
    total_len = n + m

    # 随机生成 a，长度为 total_len，值递增以避免 a[j]-a[p[i]] 等差值过乱
    a = []
    cur = 0
    for _ in range(total_len):
        cur += random.randint(1, 10)
        a.append(cur)

    # 随机生成 t，长度为 total_len，且恰好有 m 个 1（其余为 0）
    t = [0] * total_len
    ones_positions = random.sample(range(total_len), m)
    for pos in ones_positions:
        t[pos] = 1

    # 原始逻辑
    ans = [0] * m
    p = []
    for i in range(n + m):
        if t[i] == 1:
            p.append(i)

    # 若生成数据有问题导致 p 数量不足，直接返回
    if len(p) < m:
        return

    ans[0] = p[0]
    for i in range(m):
        if i == m - 1:
            ans[i] += n + m - p[i] - 1
        else:
            for j in range(p[i] + 1, p[i + 1]):
                if a[j] - a[p[i]] <= a[p[i + 1]] - a[j]:
                    ans[i] += 1
                else:
                    ans[i + 1] += 1

    print(' '.join(map(str, ans)))


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)