def main(n):
    # 映射：n 为数组长度 m，同时设 n_person = n // 2（保证有一定规模）
    m = n
    if m <= 0:
        return

    # 构造确定性数组 a，元素值在 [1,101] 区间内循环
    a = [(i % 101) + 1 for i in range(m)]
    n_person = max(1, n // 2)

    dic = {}
    for i in range(m):
        if a[i] in dic:
            dic[a[i]] += 1
        else:
            dic[a[i]] = 1

    for i in range(1, 102):
        r = 0
        for j in dic:
            r += dic[j] // i
        if r < n_person:
            print(i - 1)
            break


if __name__ == "__main__":
    main(1000)