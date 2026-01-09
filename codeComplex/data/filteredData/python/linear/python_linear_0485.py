def main(n):
    # n 表示区间数量
    # 生成确定性区间：第 i 个区间为 [i, 2*i+1]
    l1 = l2 = -1
    r1 = r2 = 1 << 30
    il = ir = -1
    for i in range(n):
        l = i
        r = 2 * i + 1
        if l > l1:
            il, l1, l2 = i, l, l1
        elif l > l2:
            l2 = l
        if r < r1:
            ir, r1, r2 = i, r, r1
        elif r < r2:
            r2 = r
    # print(max(0, (r2 - l2, max(r1 - l2, r2 - l1))[il != ir]))
    pass
if __name__ == "__main__":
    main(10)