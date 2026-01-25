def main(n):
    # 映射规则：给定 n，构造 (N, a, b)
    # 为了有不同规模的矩阵，让 N = max(2, n)
    # a, b 的构造保持确定性：
    # - 如果 n <= 3，构造 (N, 1, 1) 覆盖原代码中特判的情况
    # - 否则在 {1, 2} 之间做简单的算术分配
    if n <= 0:
        return
    N = max(2, n)
    if n <= 3:
        a, b = 1, 1
    else:
        # 确定性构造：n 的奇偶和模 3 控制 a, b
        if n % 2 == 0:
            a = 1
        else:
            a = 2
        if n % 3 == 0:
            b = 1
        else:
            b = 2

    if min(a, b) > 1 or ((N, a, b) in ((2, 1, 1), (3, 1, 1))):
        print("NO")
        return

    res = [[0] * N for _ in range(N)]
    for i in range(0, N - max(a, b)):
        res[i][i + 1] = 1
        res[i + 1][i] = 1
    if a == 1:
        res = [[e ^ 1 for e in l] for l in res]

    print("YES")
    for i in range(N):
        res[i][i] = 0
        print(*res[i], sep='')


if __name__ == "__main__":
    # 示例：用几种不同规模调用 main
    for size in [1, 2, 3, 4, 5, 10]:
        main(size)