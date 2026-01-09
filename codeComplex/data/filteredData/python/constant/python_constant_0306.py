def main(n):
    # 原程序输入: k, n_input, s, p
    # 将 n 映射为:
    # k = n
    # n_input = 2*n
    # s = n//2 + 1 (确保非零)
    # p = max(1, n//3)
    k = n
    n_input = 2 * n
    s = n // 2 + 1
    p = n // 3 if n // 3 > 0 else 1

    x = (n_input + s - 1) // s
    x *= k
    result = (x + p - 1) // p
    # print(result)
    pass
if __name__ == "__main__":
    main(10)