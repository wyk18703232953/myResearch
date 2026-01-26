def main(n):
    # 生成确定性输入结构：
    # 让 n 同时决定 k, n_input, s, p
    # 确保 s != 0, p != 0
    if n <= 0:
        n = 1
    k = n
    n_input = n * 2
    s = (n % 5) + 1
    p = (n % 7) + 1

    a = n_input // s
    if n_input % s != 0:
        a += 1
    q = k * a
    m = q // p
    if q % p != 0:
        m += 1
    # print(m)
    pass
    return m


if __name__ == "__main__":
    main(10)