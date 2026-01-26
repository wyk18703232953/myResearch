def main(n):
    # 映射 n 为区间 [l, r]，保证 l <= r 且规模随 n 增大
    # 构造方式完全确定性
    if n < 1:
        n = 1
    l = n
    r = 2 * n + 7

    for i in range(63, -1, -1):
        mx, mn = r, l
        if (1 << i) & l and (1 << i) & r:
            mx = (1 << i) - 1
            mx = r ^ (1 << i) | mx
        elif ((1 << i) & l) == 0 and ((1 << i) & r) == 0:
            mn = (1 << i) - 1
            mn = (l & mn) ^ (l | (1 << i))
        if mx >= l and mx <= r and mn >= l and mn <= r:
            r, l = mx, mn
    # print(l ^ r)
    pass
if __name__ == "__main__":
    main(10)