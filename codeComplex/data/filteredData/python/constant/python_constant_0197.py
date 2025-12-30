import random

def main(n: int):
    # 根据 n 生成测试数据，这里仅示例生成一个 1..n 的随机整数
    # 但本题原始逻辑与输入值无关，始终输出 25
    _test_value = random.randint(1, max(1, n))

    # 原程序行为：无论输入什么，都输出 25
    print(25)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可在此调整
    main(10)