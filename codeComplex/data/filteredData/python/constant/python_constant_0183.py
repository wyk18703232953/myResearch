import random

def main(n: int):
    """
    n 为规模参数，这里用于生成一个测试整数 x（1 <= x <= max(2, n)）。
    然后对原逻辑进行计算并打印结果。
    """
    # 生成测试数据：一个整数 x
    upper = max(2, n)
    x = random.randint(1, upper)

    # 原始逻辑：如果输入为 1 输出 5，否则输出 25
    if x == 1:
        print(5)
    else:
        print(25)


if __name__ == "__main__":
    # 示例：给定规模 n = 10，可以自行修改
    main(10)