def main(n):
    # 确定性生成 k 和数组 a
    if n <= 0:
        return
    k = max(1, n // 3)  # 让 k 随 n 变化且 1 <= k <= n
    if k > n:
        k = n

    # 生成一个严格递增的数组 a，元素间差值有变化，便于体现算法逻辑
    # a[i] = i*i 保证单调递增且差值递增
    a = [i * i for i in range(n)]

    c = a[-1] - a[0]

    d = [a[i] - a[i - 1] for i in range(1, n)]
    d = sorted(d)[::-1]
    c -= sum(d[:k - 1])
    # print(c)
    pass
if __name__ == "__main__":
    main(10)