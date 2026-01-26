def main(n):
    # 映射：n -> N, M，使得 N*M 大致为 n 的规模
    if n <= 0:
        return
    N = n
    M = n

    total = N * M
    Ans = [(0, 0) for _ in range(total)]
    for i in range(1, total + 1):
        if i % 2:
            a, b = divmod(i // 2, M)

        else:
            a, b = divmod(total - i // 2, M)
        Ans[i - 1] = ' '.join((str(a + 1), str(b + 1)))

    out_lines = '\n'.join(Ans)
    # print(out_lines)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的规模
    main(5)