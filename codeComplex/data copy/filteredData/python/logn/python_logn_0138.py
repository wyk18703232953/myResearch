def main(n: int):
    # 生成测试数据：根据规模 n 构造一个 k
    # 这里简单设置 k = n（某些情况下答案可能为 -1，保持与原逻辑一致）
    k = n

    k -= 1
    lo, hi = 0, int(1e9)
    while lo < hi:
        m = (lo + hi + 1) // 2
        if 1 + k * (k + 1) // 2 - m * (m + 1) // 2 >= n:
            lo = m

        else:
            hi = m - 1
    if 1 + k * (k + 1) // 2 - lo * (lo + 1) // 2 >= n:
        lo = k - lo

    else:
        lo = -1
    # print(lo)
    pass
if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n
    main(10)