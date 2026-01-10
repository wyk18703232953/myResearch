def main(n):
    a = []
    # 生成确定性区间数据：
    # 第 i 个区间为 [i, i + (i % max(1, n//3)) + 1]
    # 并保证有一定概率产生包含关系用于覆盖原逻辑
    if n <= 0:
        print("-1 -1")
        return

    base = max(1, n // 3)
    for i in range(n):
        l = i
        r = i + (i % base) + 1
        # 为了增加被完全包含的区间，周期性地缩小一些区间
        if i >= 2 and i % 5 == 0:
            l = i - 2
        a.append([l, r, i + 1])

    a.sort(key=lambda x: (x[0], -x[1]))
    r = 0
    iid = 0
    f = 1
    for i in range(n):
        if r >= a[i][1]:
            f = 0
            print(a[i][2], a[iid][2])
            break
        else:
            r = a[i][1]
            iid = i
    if f:
        print("-1 -1")


if __name__ == "__main__":
    main(10)