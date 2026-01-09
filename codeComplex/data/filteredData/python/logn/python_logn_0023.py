def main(n):
    # 根据 n 生成确定性的 l 和 r，确保 l <= r 且有一定差异
    l = n
    r = n * 2 + (n // 2)
    if l > r:
        l, r = r, l

    for i in range(60, -1, -1):
        if ((l >> i) & 1) != ((r >> i) & 1):
            # print((1 << (i + 1)) - 1)
            pass
            return
    # print(0)
    pass
if __name__ == "__main__":
    main(10)