def main(n):
    # 通过 n 确定性地构造输入：
    # n = 原始输入的 n（行数）
    # k 与每一行的 (x, y) 都由简单算术生成，保证可重复
    if n <= 0:
        # 若规模为 0，构造一个最小可运行场景
        n = 1

    # 构造 k：让它随 n 线性增长，保证确定性
    k = n * (n // 2 + 1)

    a = []
    b = []
    d = []
    c = 0

    # 构造 n 行 (x, y)，保持 x >= y 且都有一定差值
    for i in range(n):
        # 简单确定性模式：x 比 y 大一个与 i 相关的值
        y = i % 7 + 1
        x = y + (i // 3 + 1)
        t = x - y
        a.append(x)
        b.append(y)
        d.append(t)

    s = sum(a)
    d.sort()
    d = d[::-1]
    if sum(b) > k:
        # print(-1)
        pass

    else:
        while s > k and c < len(d):
            s = s - d[c]
            c = c + 1
        # print(c)
        pass
if __name__ == "__main__":
    # 示例：可根据需要修改 n 的规模
    main(10)