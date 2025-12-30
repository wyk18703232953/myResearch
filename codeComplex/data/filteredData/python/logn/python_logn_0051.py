import random

def main(n: int):
    """
    n 为测试规模，用于控制随机生成数据的范围：
    a, b 在 [0, n] 区间内随机生成
    """
    # 生成测试数据
    a = random.randint(0, n)
    b = random.randint(0, n)

    # 原始逻辑
    k = 2 ** ((a ^ b).bit_length()) - 1
    print(k)

if __name__ == "__main__":
    # 示例：可自行修改 n 的数值进行测试
    main(10)