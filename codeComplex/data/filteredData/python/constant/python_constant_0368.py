def main(n):
    # 确定性生成 a, b, c, n_input
    a = n
    b = n // 2
    c = n // 3
    n_input = 3 * n + 5

    a2 = a - c
    b2 = b - c
    if n_input - a2 - b2 - c >= 1 and a2 >= 0 and b2 >= 0:
        # print(n_input - a2 - b2 - c)
        pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    main(10)