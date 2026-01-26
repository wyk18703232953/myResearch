def main(n):
    # n 表示数组 a 的长度，值域固定为 [1, 10]，c 固定为 5
    # 所有数据由 n 确定性生成
    if n <= 0:
        # print(0)
        pass
        return

    c = 5
    max_val = 10  # a[i] 取值范围 [1, max_val]

    # 构造确定性数组 a：a[i] = (i % max_val) + 1
    a = [(i % max_val) + 1 for i in range(n)]

    # 原始逻辑开始
    f = [0] * 500001
    l = [[0] for _ in range(500001)]

    m = 0
    for i in range(n):
        v = a[i]
        l[v].append(f[v] - m)
        if v == c:
            m += 1
        f[v] += 1
        l[v].append(f[v] - m)

    ma = 0
    for arr in l:
        mi = 0
        for val in arr:
            if val < mi:
                mi = val
            diff = val - mi
            if diff > ma:
                ma = diff

    # print(m + ma)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的大小进行实验
    main(10)