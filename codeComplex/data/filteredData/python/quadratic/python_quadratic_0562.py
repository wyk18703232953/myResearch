import sys

def main(n):
    # 这里将原来的 N, M 都设为 n，根据规模 n 生成一个 n×n 的数据
    N = n
    M = n

    Ans = [(0, 0) for _ in range(N * M)]
    for i in range(1, N * M + 1):
        if i % 2:
            a, b = divmod(i // 2, M)

        else:
            a, b = divmod(N * M - i // 2, M)
        Ans[i - 1] = (a + 1, b + 1)
    for a in Ans:
        # sys.stdout.write('{} {}\n'.format(*a))
        pass


if __name__ == "__main__":
    # 示例：规模为 3 时调用
    main(3)