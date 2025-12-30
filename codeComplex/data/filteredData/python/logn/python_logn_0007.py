def main(n: int):
    # 根据规模 n 生成测试数据：
    # 这里假设 a,b 的取值范围与 n 相关，例如：
    # 0 <= a,b < 2^n
    # 可根据实际需要调整生成方式
    a = (1 << n) - 1      # 示例：最大 n 位二进制数
    b = (1 << (n - 1))    # 示例：一个较大的数，约为 2^(n-1)

    # 原逻辑：计算 (1<<(a^b).bit_length())-1
    result = (1 << (a ^ b).bit_length()) - 1
    print(result)


if __name__ == "__main__":
    # 示例：调用 main，规模自行设定
    main(5)