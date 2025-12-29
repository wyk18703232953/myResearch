def main(n):
    # 生成前 n 个素数
    y = []
    num = 2
    while len(y) < n:
        is_prime = True
        for x in range(2, int(num ** 0.5) + 1):
            if num % x == 0:
                is_prime = False
                break
        if is_prime:
            y.append(num)
        num += 1

    # 计算相邻素数和
    h = []
    for i in range(len(y) - 1):
        h.append(y[i] + y[i + 1])

    # 参数化：根据 n 生成 a, b
    # 这里设定：
    # a 为最后一个素数与前一个素数的和再加 1（与原逻辑接近）
    # b 为需要的满足条件的个数，取 n // 3（可按需要调整策略）
    if len(y) >= 2:
        a = y[-2] + y[-1] + 1
    else:
        a = 3
    b = max(1, n // 3)

    # 将和全部加 1
    for i in range(len(h)):
        h[i] = h[i] + 1

    # 筛选出仍然是素数的数
    g = []
    for val in h:
        is_prime = True
        for x in range(2, int(val ** 0.5) + 1):
            if val % x == 0:
                is_prime = False
                break
        if is_prime:
            g.append(val)

    # 统计在 [2, a] 区间内的数量
    j = 0
    for val in g:
        if 2 <= val <= a:
            j += 1

    # 按原逻辑输出
    if j >= b:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：调用 main，n 为规模
    main(10)