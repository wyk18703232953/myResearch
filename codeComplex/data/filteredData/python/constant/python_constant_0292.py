def main(n):
    # 生成测试数据：
    # 这里示例性地根据 n 构造 k, s, p
    # 可根据需要修改生成逻辑
    k = max(1, n // 3)     # 组数
    s = max(1, n // 5)     # 每本册子能用的页数
    p = max(1, n // 7)     # 每包册子的本数

    # 原逻辑
    L = (n - 1) // s + 1
    L *= k
    result = (L - 1) // p + 1
    print(result)


if __name__ == "__main__":
    # 示例：以 n = 100 为规模运行
    main(100)