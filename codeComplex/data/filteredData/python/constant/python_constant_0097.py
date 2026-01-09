def solve(a, b):
    m = max(a, b)
    n = min(a, b)
    if n == 0:
        return 0
    if m == n:
        return 1
    elif m % n == 0:
        return m // n
    k = m // n
    return k + solve(n, m - n * k)


def main(n):
    # n 表示测试用例数量
    res = []
    for i in range(1, n + 1):
        a = i
        b = 2 * i + 1
        res.append(solve(a, b))
    for v in res:
        # print(v)
        pass
if __name__ == "__main__":
    main(10)