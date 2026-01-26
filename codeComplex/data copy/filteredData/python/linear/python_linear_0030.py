def main(n):
    # 数据生成：将 n 映射为字符串长度
    # 构造一个由 'H' 和 'T' 组成的确定性字符串
    if n <= 0:
        s = "HT"

    else:
        chars = []
        for i in range(n):
            # 偶数位放 'H'，奇数位放 'T'
            if i % 2 == 0:
                chars.append('H')

            else:
                chars.append('T')
        s = "".join(chars)

    # 原程序的 a 未真正参与逻辑，只作为初始上界
    # 这里将 a 设为 n，且保证至少为 1
    a = max(1, n)

    d = s.count('H')
    p = []
    for i in range(len(s)):
        if i + d > len(s):
            n_over = d + i - len(s)
            m = d - n_over
            h = s[:m] + s[-n_over:]
            k = h.count("T")
            p.append(k)

        else:
            h = s[i:d + i]
            k = h.count("T")
            p.append(k)
    mi = a
    for i in range(len(p)):
        if p[i] < mi:
            mi = p[i]
    if s.count("H") == 1 or s.count("T") == 0:
        # print(0)
        pass

    else:
        # print(mi)
        pass
if __name__ == "__main__":
    main(10)