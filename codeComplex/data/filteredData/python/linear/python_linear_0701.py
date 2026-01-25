def main(n):
    # 生成确定性参数 n_in, v 基于规模 n
    if n <= 0:
        print(0)
        return

    n_in = n
    v = n * (n + 1) // 4  # 一个随 n 增长的确定性容量

    x = 0
    c = 0
    for i in range(1, n_in):
        if x < n_in - i:
            add = min((n_in - i), v - x)
            c += i * add
            x += add
        x -= 1

    print(c)


if __name__ == "__main__":
    # 示例：使用 n = 10 作为规模
    main(10)