def main(n):
    # 映射：将 n 拆成 l, r，保证 l <= r 且有一定差异度
    l = n
    r = 2 * n if n > 0 else 0  # 确保 r >= l
    z = l ^ r
    c = 0
    if z == 0:
        # print(0)
        pass
        return
    while z:
        c += 1
        z >>= 1
    x = '1' * c
    # print(int(x, 2))
    pass
if __name__ == "__main__":
    main(10)