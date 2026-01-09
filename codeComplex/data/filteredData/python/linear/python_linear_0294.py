def main(n):
    # 生成确定性输入数据：长度为 n 的整数数组
    # 为避免负数索引问题，将值范围限制在 [-999999, 999999] 且排除 0
    # 使用简单算术构造保证可重复性
    a = []
    for i in range(n):
        val = (i * 123457) % 2000000 - 1000000
        if val == 0:
            val = 1
        a.append(val)

    c = 0
    po = [0] * 1000000
    ne = [0] * 1000000
    for i in range(n):
        if a[i] < 0 and ne[-a[i]] != 1:
            c += 1
            ne[-a[i]] = 1
        elif a[i] > 0 and po[a[i]] != 1:
            c += 1
            po[a[i]] = 1
    # print(c)
    pass
if __name__ == "__main__":
    main(10)