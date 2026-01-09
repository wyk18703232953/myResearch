def main(n):
    # 1. 生成测试数据：长度为 n 的数组 ar
    # 这里简单生成 ar[i] = i + 1，可按需要修改生成规则
    ar = [i + 1 for i in range(n)]

    # 2. 按原逻辑构建 li
    li = []
    for i in range(n):
        xx = []
        for j in range(n - i):
            xx.append(0)
        li.append(xx.copy())

    for i in range(n):
        for j in range(n - i):
            if i == 0:
                li[i][j] = ar[j]

            else:
                li[i][j] = li[i - 1][j] ^ li[i - 1][j + 1]

    for i in range(1, n):
        for j in range(n - i):
            li[i][j] = max(li[i][j], li[i - 1][j], li[i - 1][j + 1])

    # 3. 生成若干测试区间并输出查询结果
    # 这里生成所有 1 <= l <= r <= n 的查询
    for l in range(1, n + 1):
        for r in range(l, n + 1):
            # 与原程序一致的输出逻辑
            # print(li[r - l][l - 1])
            pass
if __name__ == "__main__":
    # 示例：用 n = 5 运行
    main(5)