def main(n: int):
    # 根据规模 n 生成测试数据：
    # 这里约定：
    #   0 <= l, r <= 2^n - 1
    #   且让 l, r 尽量“相差较大”，便于测试 bit_length 逻辑
    # 示例：l = 0, r = 2^n - 1
    if n < 0:
        raise ValueError("n must be non-negative")

    l = 0
    r = (1 << n) - 1  # 2^n - 1

    # 保持原逻辑：
    # 输出：2**(l^r).bit_length() - 1
    result = (1 << ((l ^ r).bit_length())) - 1
    print(result)


if __name__ == "__main__":
    # 示例调用，按需修改 n
    main(3)