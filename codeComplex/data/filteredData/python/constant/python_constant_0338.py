import random

def main(n: int):
    # 根据 n 生成测试数据，这里示例为：将 n 作为原程序中的输入
    # 若需要批量测试，也可以随机生成多个样例：
    # test_values = [random.randint(0, 10**6) for _ in range(n)]
    # 这里按题意，规模 n 就是原始输入
    x = n

    x += 1
    if x == 1:
        result = 0
    elif x % 2 == 0:
        result = x // 2
    else:
        result = x

    print(result)


if __name__ == "__main__":
    # 示例：用一个固定的 n 作为测试
    # 可根据需要修改为其他生成方式
    sample_n = random.randint(0, 100)
    main(sample_n)