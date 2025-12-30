import random

def main(n: int):
    # 生成测试数据：x, y 在 [1, n] 范围内
    x = random.randint(1, n)
    y = random.randint(1, n)

    val1 = max(x, y) - 1
    val2 = n - min(x, y)

    if val1 <= val2:
        print('White')
    else:
        print('Black')


if __name__ == "__main__":
    # 示例：可在此处指定规模 n
    main(10)