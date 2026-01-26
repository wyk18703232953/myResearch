def main(n):
    # 生成确定性输入：n, m, a, b
    # 为了可规模化，将主输入规模映射为 n，本题原本只有一个 n
    # 其余参数用 n 的简单确定函数构造
    if n <= 0:
        n_val = 1

    else:
        n_val = n

    m = n_val % 10 + 1   # 1 到 10 之间
    a = n_val + 1
    b = n_val + 2

    if n_val % m != 0:
        mn = n_val // m * m
        mx = n_val // m * m + m
        # print(min((n_val - mn) * b, (mx - n_val) * a))
        pass

    else:
        # print(0)
        pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(1000)