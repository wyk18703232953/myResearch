import random

def main(n: int):
    # 根据规模 n 生成测试数据，这里生成一个 1 到 n 之间的整数
    a = random.randint(1, max(1, n))

    # 原逻辑：无论输入是什么，都输出 25
    print(25)


if __name__ == "__main__":
    # 示例：可自行修改 n 测试不同规模
    main(10)