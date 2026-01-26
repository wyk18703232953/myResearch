def main(n):
    # n 表示序列长度
    t = max(1, n)

    # 构造一个先递增再递减的“山峰”序列，峰值为 t-1，保证有明确的最大值
    if t == 1:
        g = [0]

    else:
        peak = t // 2
        g = list(range(peak + 1)) + list(range(peak - 1, -1, -1))
        g = g[:t]

    k = max(g)
    flag = True
    i = 0
    while g[i] != k:
        if i != 0 and g[i] < g[i - 1]:
            # print("NO")
            pass
            return
        i += 1
    i += 1
    while i < t and g[i] != k:
        if i != 0 and g[i] > g[i - 1]:
            # print("NO")
            pass
            return
        i += 1
    # print("YES")
    pass
if __name__ == "__main__":
    main(10)