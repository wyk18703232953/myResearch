def main(n):
    # 映射规则：
    # 原始输入: n, a, b
    # 这里将:
    #   n_input = n
    #   a = max(1, n % 5)
    #   b = max(1, (n // 2) % 5)
    # 这样 (n, a, b) 完全由 n 决定，且可变化又确定。
    n_input = max(1, n)
    a = max(1, n_input % 5)
    b = max(1, (n_input // 2) % 5)

    n = n_input
    if min(a, b) > 1 or 1 < n < 4 and max(a, b) == 1:
        print('NO')
        return
    print('YES')
    f = int(a == 1)
    g = [a, b][f]
    r = [[f] * n for _ in range(n)]
    for i in range(n):
        r[i][i] = 0
    for i in range(n - g):
        r[i][i + 1] ^= 1
        r[i + 1][i] ^= 1
    for x in r:
        print(*x, sep='')


if __name__ == "__main__":
    # 示例：使用 n = 10 进行一次确定性实验
    main(10)