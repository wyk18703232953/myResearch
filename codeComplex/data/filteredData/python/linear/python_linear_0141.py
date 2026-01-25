def main(n):
    # 生成确定性的输入数组 m，长度为 n
    # 使用简单算术构造，确保可规模化和可重复
    m = [(i * 2 + 3) % (n + 5) for i in range(n)]

    t = []
    for i in range(n):
        if i == 0:
            t.append(m[i] + 1)
        else:
            t.append(max(t[i - 1], m[i] + 1))
    s = t[n - 1] - m[n - 1] - 1
    for i in range(n - 2, -1, -1):
        if t[i] < t[i + 1] - 1:
            t[i] = t[i + 1] - 1
        s += t[i] - m[i] - 1
    print(s)


if __name__ == "__main__":
    main(10)