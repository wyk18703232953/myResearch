import random

def main(n):
    # 根据规模 n 生成测试数据，这里示例为：
    # 随机生成一个 0 ~ n 范围内的整数作为原程序中的输入
    x = random.randint(0, n)

    # 原始逻辑：将输入加 1
    val = x + 1

    if val < 2:
        result = 0
    elif val % 2 == 0:
        result = val // 2
    else:
        result = val

    print(result)


if __name__ == "__main__":
    # 这里可以自由指定规模 n
    main(10)