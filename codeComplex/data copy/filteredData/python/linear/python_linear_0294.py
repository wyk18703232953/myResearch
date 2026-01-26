def main(n):
    # 生成确定性输入：长度为 n 的整数数组 a
    # 数值分布在 [-499999, 499999]，跳过 0
    a = [((i % 999999) - 499999) or 1 for i in range(n)]

    c = 0
    po = [0] * 1000000
    ne = [0] * 1000000
    for i in range(n):
        if a[i] < 0 and ne[a[i]] != 1:
            c += 1
            ne[a[i]] = 1
        elif a[i] > 0 and po[a[i]] != 1:
            c += 1
            po[a[i]] = 1
    # print(c)
    pass
if __name__ == "__main__":
    main(100000)