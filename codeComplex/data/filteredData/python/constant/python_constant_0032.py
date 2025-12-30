import random

def main(n: int):
    """
    n: 规模参数，这里用来生成一个测试整数 x，
       再按原逻辑计算 a = (x // 2) * 3 并打印结果。
    """
    # 根据规模 n 生成测试数据：
    # 例如在 [0, n] 范围内随机取一个整数作为原来的输入值
    x = random.randint(0, n)

    a = (x // 2) * 3
    print(a)


if __name__ == "__main__":
    # 示例：可自行修改规模 n
    main(10)