import random

def main(n):
    # 生成测试数据：随机生成满足 0 <= l[i], r[i] <= n 的数据
    l = [random.randint(0, n) for _ in range(n)]
    r = [random.randint(0, n) for _ in range(n)]

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
        print(" ".join(str(x) for x in a))
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：可修改 n 以测试不同规模
    main(5)