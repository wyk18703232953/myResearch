def main(n):
    # 映射：n 为题目数量
    # 生成确定性参数
    least = n * (n // 2)
    most = n * (n + 1) // 2
    x = max(1, n // 3)
    # 生成确定性难度列表 c，长度为 n
    # 使用简单算术构造保证可扩展、确定性
    c = [(i * 2 + (i // 3)) % (2 * n + 3) + 1 for i in range(n)]

    ans = 0
    _max = lambda x, y: x if x > y else y
    _min = lambda x, y: x if x < y else y

    for mask in range(1 << n):
        mx = float("-inf")
        mn = float("inf")
        count = 0
        Sum = 0
        for i in range(n):
            if mask & (1 << i):
                count += 1
                Sum += c[i]
                mx = _max(mx, c[i])
                mn = _min(mn, c[i])
        if mx - mn >= x and Sum >= least and Sum <= most and count >= 2:
            ans += 1
    print(ans)


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 以做规模实验
    main(10)