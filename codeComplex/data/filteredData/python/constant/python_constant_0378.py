def main(n):
    # 原程序输入结构：a b c n
    # 这里将输入规模参数映射为原程序中的 n_input
    n_input = n

    # 确定性生成 a, b, c
    a = n_input // 2
    b = n_input // 3 + 1
    c = min(a, b) // 2

    t = a + b - c
    if a >= n_input or b >= n_input or c > a or c > b or t >= n_input:
        # print(-1)
        pass

    else:
        # print(n_input - t)
        pass
if __name__ == "__main__":
    main(10)