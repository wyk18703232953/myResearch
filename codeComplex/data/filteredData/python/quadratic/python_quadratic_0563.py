import sys

def main(n):
    # 将 n 映射为 N 和 M，使得 N*M 与 n 同阶，这里取 N = n, M = n
    if n <= 0:
        return
    N = n
    M = n

    total = N * M
    Ans = [None] * total
    for i in range(1, total + 1):
        if i % 2:
            a, b = divmod(i // 2, M)
        else:
            a, b = divmod(N * M - i // 2, M)
        Ans[i - 1] = (a + 1, b + 1)
    for a in Ans:
        sys.stdout.write('{} {}\n'.format(*a))


if __name__ == "__main__":
    main(5)