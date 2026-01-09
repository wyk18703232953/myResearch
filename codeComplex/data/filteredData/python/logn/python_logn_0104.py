def main(n):
    # 将 n 映射为一对整数 (l, r)，保证 l <= r，且规模随 n 线性增长
    l = n
    r = 2 * n

    lxr = l ^ r
    msb = 0
    while lxr:
        msb += 1
        lxr >>= 1
    m = 0
    t = 1
    while msb:
        m += t
        t <<= 1
        msb -= 1
    # print(m)
    pass
if __name__ == "__main__":
    main(10)