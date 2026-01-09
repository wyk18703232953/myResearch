def main(n):
    # 生成测试数据：
    # 固定 q = n，查询编号 a 从 1 到 n，
    # 操作字符串 s 为长度随 n 变化的简单模式（例如交替 'L'、'R'、'U'）
    q = n
    queries = []
    ops = ['L', 'R', 'U']
    for i in range(q):
        a = (i % n) + 1  # 1 到 n 循环
        # 生成长度随 n 变化的操作串，避免过长
        length_s = max(1, min(20, n))  # 限制长度在 1~20 之间
        s = ''.join(ops[(i + j) % 3] for j in range(length_s))
        queries.append((a, s))

    # 原算法逻辑
    # 预处理树高度 l
    x = n + 1
    l = 0
    while x > 1:
        x //= 2
        l += 1

    results = []
    for a, s in queries:
        for j in s:
            lv = 1
            a1 = a
            # 计算节点所在层 lv（从 1 开始）
            while a1 % 2 == 0:
                a1 //= 2
                lv += 1
            x = 2 ** lv
            half = x // 2
            quarter = half // 2
            y = (a - half) // x + 1
            if j == 'U':
                if lv == l:
                    pass

                else:
                    if y % 2:
                        a = (2 * a + x) // 2

                    else:
                        a = (2 * a - x) // 2
            elif j == 'L':
                if lv == 1:
                    pass

                else:
                    z = 2 * (y - 1)
                    a = quarter + z * half
            else:  # 'R'
                if lv == 1:
                    pass

                else:
                    z = 2 * (y - 1)
                    a = quarter + (z + 1) * half
        results.append(a)

    # 输出结果
    for ans in results:
        # print(ans)
        pass
if __name__ == "__main__":
    # 示例调用，可自行修改 n
    main(10)