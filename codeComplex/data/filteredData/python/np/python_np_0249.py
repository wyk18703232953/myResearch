import random

def solve(a, b, c, d, e, f):
    n = 1
    n2 = a * b + c * d + e * f
    while n * n < n2:
        n += 1
    if n * n > n2:
        return "-1"

    l = sorted([
        [max(a, b), min(a, b), 'A'],
        [max(c, d), min(c, d), 'B'],
        [max(e, f), min(e, f), 'C']
    ])

    if l[2][0] != n:
        return "-1"

    v = str(n) + '\n' + (l[2][2] * n + '\n') * l[2][1]

    if l[0][0] == n and l[1][0] == n:
        for i in range(2):
            v += (l[i][2] * n + '\n') * l[i][1]
    else:
        s = n - l[2][1]
        if s not in l[0] or s not in l[1]:
            return "-1"
        if s != l[0][0]:
            l[0][0], l[0][1] = l[0][1], l[0][0]
        if s != l[1][0]:
            l[1][0], l[1][1] = l[1][1], l[1][0]
        v += (l[0][2] * l[0][1] + l[1][2] * l[1][1] + '\n') * s

    return v

def generate_test_data(n):
    # 尝试构造满足 a*b + c*d + e*f == n^2 的数据
    # 简单策略：随机切分 n^2 成三块，然后为每块找一个因子分解
    S = n * n
    parts = [0, 0, 0]
    # 保证三部分和为 S 且为正
    x = random.randint(1, S - 2)
    y = random.randint(1, S - 1 - x)
    z = S - x - y
    parts = [x, y, z]

    def rand_fact(k):
        # 找到 k 的一个随机因子分解 (p, q)
        divs = []
        d = 1
        while d * d <= k:
            if k % d == 0:
                divs.append((d, k // d))
                if d * d != k:
                    divs.append((k // d, d))
            d += 1
        return random.choice(divs)

    (a, b) = rand_fact(parts[0])
    (c, d_) = rand_fact(parts[1])
    (e, f) = rand_fact(parts[2])
    return a, b, c, d_, e, f

def main(n):
    a, b, c, d, e, f = generate_test_data(n)
    res = solve(a, b, c, d, e, f)
    print(res)

if __name__ == "__main__":
    # 示例：调用 main(4)，实际评测时由外部调用 main(n)
    main(4)