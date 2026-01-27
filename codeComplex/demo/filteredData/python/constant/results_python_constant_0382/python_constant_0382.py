def main(n):
    # 生成确定性输入：a, b, c, n_input
    # 让 a, b, c 与 n 有线性关系，保证可规模化
    a = 2 * n
    b = 3 * n
    c = n // 2
    n_input = 5 * n

    a -= c
    b -= c
    if a >= 0 and b >= 0:
        if (a + b + c) < n_input:
            n_input -= (a + b + c)
            # print(n_input)
            pass

        else:
            # print(-1)
            pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    main(10)