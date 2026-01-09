def main(n):
    # 生成确定性输入：a, b, c, n_input
    a = n
    b = 2 * n
    c = n // 2
    n_input = n + 5

    p = a + b - c
    if p <= n_input - 1 and a - c >= 0 and b - c >= 0:
        result = n_input - p

    else:
        result = -1

    # print(result)
    pass
if __name__ == "__main__":
    main(10)