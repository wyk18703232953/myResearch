def main(n):
    # n 表示数组长度
    if n <= 0:
        return

    # 确定性生成 l, r
    # 让 l 有一定起伏, r 与 l 有不同模式, 保持确定性
    l = [(i * 2 + (i // 2)) % (n + 3) for i in range(n)]
    r = [((i * 3) ^ (i // 3)) % (n + 5) for i in range(n)]

    a = [0 for _ in range(n)]
    m = []
    m_ = []
    for i in range(n):
        m.append(l[i] + r[i])
        m_.append(l[i] + r[i])
    m.sort()
    ma = m[-1] + 1

    for i in range(n):
        a[i] = ma - m_[i]

    l_ = []
    r_ = []
    for i in range(n):
        c = 0
        d = 0
        for j in range(i + 1):
            if a[j] > a[i]:
                c += 1
        for j in range(i, n):
            if a[j] > a[i]:
                d += 1
        l_.append(c)
        r_.append(d)
    res = True
    for i in range(n):
        if l[i] != l_[i] or r[i] != r_[i]:
            res = False
            break
    if res:
        print("YES")
        for i in range(n):
            a[i] = str(a[i])
        print(" ".join(a))
    else:
        print("NO")


if __name__ == "__main__":
    main(10)