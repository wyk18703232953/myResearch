def main(n: int) -> int:
    """
    根据规模 n 生成测试数据，并计算结果。
    本题逻辑：对测试值 t 计算 (t + t%2) * ((t + 2)//2) // 2
    这里直接令测试数据 t = n。
    """
    t = n  # 测试数据生成逻辑：可按需修改为任意基于 n 的构造
    return (t + t % 2) * ((t + 2) // 2) // 2


if __name__ == "__main__":
    # 示例：自行指定规模 n 测试
    example_n = 10
    # print(main(example_n))
    pass