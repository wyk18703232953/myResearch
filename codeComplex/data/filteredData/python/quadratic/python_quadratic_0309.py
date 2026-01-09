def main(n):
    # 映射：n 为数组长度，k 为 n 的一半（至少为 1）
    length = max(1, n)
    k = max(1, length // 2)
    a = [(i * 7 - 3) % 1000 - 500 for i in range(length)]

    ans = -1 * 10**9 + 7
    for i in range(length):
        s = 0
        for j in range(i, length):
            s += a[j]
            if j - i + 1 >= k:
                ans = max(ans, s / (j - i + 1))
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)