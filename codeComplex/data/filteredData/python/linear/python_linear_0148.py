def main(n):
    # 确定性生成 n, k, lst
    # 保持原逻辑：前一行有 n 和 k，后一行为长度为 n 的数组
    if n <= 0:
        # print(0)
        pass
        return

    k = n + 3  # 任意与 n 相关的正整数，确保可规模化且确定
    lst = [(i * 2 + 3) % (k + 5) for i in range(n)]

    s = sum(lst)
    s2 = 0
    m = 0
    for i in range(n - 1):
        s2 += lst[i]
        s -= lst[i]
        v = (s2 % k) + (s % k)
        if v > m:
            m = v
    # print(m)
    pass
if __name__ == "__main__":
    main(10)