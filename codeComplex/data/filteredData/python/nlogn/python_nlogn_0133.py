def main(n):
    # 映射含义：
    # n: 数组 a 的长度
    # 构造确定性的 m, k, a
    # 保证 m、k 与 n 有一定规模关系，便于观察复杂度

    # m 随 n 线性增长
    m = 5 * n + 10
    # k 稍小于 m，确保算法需要若干步
    k = 2 * n + 3

    # 构造长度为 n 的数组 a，元素为确定性递减序列
    # 保证有足够多的大数和小数的混合
    # 例如：a[i] = (n - i) % 7 + 1，确保都为正数
    a = [((n - i) % 7) + 1 for i in range(n)]

    # 核心算法逻辑保持不变
    a.sort(reverse=True)
    no = 0
    while k < m and no < n:
        k += a[no] - 1
        no += 1
    if k < m:
        # print(-1)
        pass

    else:
        # print(no)
        pass
if __name__ == "__main__":
    main(10)