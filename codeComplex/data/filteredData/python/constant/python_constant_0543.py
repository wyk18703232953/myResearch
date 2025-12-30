import random

def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里约定：s 为 [0, 10*n] 范围内的随机整数
    s = random.randint(0, 10 * n)

    # 原始逻辑：计算 ceil(s / n)
    num_1 = s // n
    if s % n == 0:
        result = num_1
    else:
        result = num_1 + 1

    print(result)


if __name__ == "__main__":
    # 可以在这里指定 n 的测试规模
    main(5)