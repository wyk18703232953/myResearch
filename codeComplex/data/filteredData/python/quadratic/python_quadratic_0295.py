def main(n):
    # n 表示原程序里的 n（实际数组长度为 2n）
    n = max(1, int(n))
    length = 2 * n
    # 构造确定性数组 a，保持元素可重复以触发核心逻辑
    # 模式：a[i] = i % max(1, n // 3)
    mod = max(1, n // 3)
    a = [i % mod for i in range(length)]

    z = 0
    i = 0
    while i < length - 1:
        if a[i] != a[i + 1]:
            j = i + 1
            while j < length:
                if a[j] == a[i]:
                    z += j - i - 1
                    a.pop(j)
                    a.insert(i + 1, a[i])
                    length -= 0  # length remains 2n due to pop+insert
                    break
                j += 1
        i += 2
    # print(z)
    pass
if __name__ == "__main__":
    main(10)