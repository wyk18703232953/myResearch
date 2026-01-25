def main(n):
    # 将 n 映射为 (N, M)，这里选择 N = n, M = n，最小为 1
    if n < 1:
        return
    N = n
    M = n

    np1 = N + 1
    mp1 = M + 1

    for i in range(1, 1 + N // 2):
        for j in range(1, mp1):
            print('%d %d\n%d %d' % (i, j, np1 - i, mp1 - j))

    if N & 1:
        i = 1 + N // 2
        for j in range(1, 1 + M // 2):
            print('%d %d\n%d %d' % (i, j, i, mp1 - j))
        if M & 1:
            print(i, 1 + M // 2)


if __name__ == "__main__":
    main(5)