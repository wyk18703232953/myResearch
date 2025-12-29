def main(n):
    # 生成测试数据：n 对 (x, y)，以及总容量 m
    # 这里给出一个简单的随机-like 构造，便于测试逻辑：
    #  - x 在 [1, 10*n] 内递增生成
    #  - y 在 [0, x] 内通过简单规则生成
    #  - m 设为总 x 的一半左右，保证有可压缩空间
    a = []
    cur = 0
    sm = 0
    for i in range(1, n + 1):
        x = i * 3 + 1          # 模拟原始 x
        y = x // 2             # 模拟原始 y，保证 y <= x
        a.append([x, y])
        cur += x
        sm += y
    # 设置 m：比总 x 略小，使得需要若干压缩
    m = cur - (cur // 3)

    # 以下为原程序逻辑，仅去掉 input 并封装为函数

    if sm > m:
        print(-1)
        return

    cnt = 0
    # 按照减少量 (x-y) 从大到小排序 => key 为 -(x - y)
    a.sort(key=lambda x: -x[0] + x[1])

    i = 0
    while cur > m and i < n:
        cur -= a[i][0] - a[i][1]
        cnt += 1
        i += 1

    print(cnt)


if __name__ == "__main__":
    # 示例：规模为 5
    main(5)