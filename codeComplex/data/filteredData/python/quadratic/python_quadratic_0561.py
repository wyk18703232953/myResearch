def main(n):
    # 映射规则：N = n，M = n（可按需要调整为其他映射）
    N = max(1, n)
    M = max(1, n)

    total = N * M
    Ans = [None] * total

    for i in range(1, total + 1):
        if i % 2:
            a, b = divmod(i // 2, M)

        else:
            a, b = divmod(N * M - i // 2, M)
        Ans[i - 1] = ' '.join((str(a + 1), str(b + 1)))

    for a in Ans:
        # print(a)
        pass
if __name__ == "__main__":
    main(5)