def main(n: int):
    # 根据规模 n 生成测试数据，这里约定：
    # 生成区间 [l, r]，其中 l = 0，r = 2^n - 1（n 不超过 60 左右）
    # 若 n 过大，则限制在 60 位以内，避免溢出到非常大的整数
    n = max(0, min(n, 60))
    l = 0
    r = (1 << n) - 1 if n > 0 else 0

    x = 64
    while x >= 0 and (l & (1 << x)) == (r & (1 << x)):
        x -= 1
    print((1 << (x + 1)) - 1)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)