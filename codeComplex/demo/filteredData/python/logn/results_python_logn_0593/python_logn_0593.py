def main(n):
    # 生成测试数据：n 为规模，自行构造 k
    # 这里示例设定 k 为从 0 到 n*(n+1)//2 中点附近的某个值
    k = (n * (n + 1) // 2) // 2

    # 原逻辑封装
    l = -1
    r = n + 1
    while r - l > 1:
        m = (r + l) // 2
        if (n - m) * (n - m + 1) // 2 - m > k:
            l = m

        else:
            r = m
    # print(r)
    pass
if __name__ == "__main__":
    # 示例：调用 main，n 可按需修改
    main(10)