def main(n):
    # 映射规模参数 n 到原程序的 n, a, b
    # 约束：满足 min(a, b) <= 1 且不触发 NO 的条件
    # 选择 a=1, b=0 始终满足条件，并保持结构变化与 n 线性相关
    orig_n = max(1, n)  # 保证至少为 1
    a = 1
    b = 0

    if min(a, b) > 1 or 1 < orig_n < 4 and max(a, b) == 1:
        print('NO')
        return
    print('YES')
    f = int(a == 1)
    g = [a, b][f]
    r = [[f] * orig_n for _ in range(orig_n)]
    for i in range(orig_n):
        r[i][i] = 0
    for i in range(orig_n - g):
        r[i][i + 1] ^= 1
        r[i + 1][i] ^= 1
    for x in r:
        print(*x, sep='')


if __name__ == "__main__":
    # 示例：以 n=5 运行
    main(5)