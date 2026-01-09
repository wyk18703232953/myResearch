import sys


def main(n):
    N = n
    M = n  # 根据规模 n 生成一个 N×M 的方阵，这里简单取 M = n

    Ans = [None] * (N * M)
    for i in range(1, N * M + 1):
        if i % 2:
            a, b = divmod(i // 2, M)

        else:
            a, b = divmod(N * M - i // 2, M)
        Ans[i - 1] = (a + 1, b + 1)

    for a in Ans:
        sys.stdout.write('{} {}\n'.format(*a))


if __name__ == "__main__":
    # 示例：当 n = 3 时运行
    main(3)