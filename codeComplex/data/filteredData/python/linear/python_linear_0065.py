def solve(n, p, s):
    p.append((0, 0))
    p.sort()
    t = 0
    while p:
        x = p.pop()
        s, t = x[0], max(x[1], t + abs(s - x[0]))
    return t


def generate_input(n):
    # 对于规模 n，生成：
    # s: 初始位置，可随 n 线性增长
    # p: n 个 (position, time) 对，位置单调递增，时间做简单算术构造
    s = n // 2
    p = [(i, (i * (i + 1)) // 2) for i in range(1, n + 1)]
    return n, p, s


def main(n):
    n_val, p, s = generate_input(n)
    result = solve(n_val, p, s)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)