import random

def main(n: int):
    # 根据 n 生成测试数据：这里直接使用传入的 n 作为测试规模
    # 如果需要批量测试，可自行在外部循环调用 main 不同的 n

    if n == 1 or n == 2:
        print(n)
    elif n % 2 != 0:
        m = n * (n - 1) * (n - 2)
        print(m)
    elif n % 3 != 0:
        m = n * (n - 1) * (n - 3)
        print(m)
    else:
        m = (n - 1) * (n - 2) * (n - 3)
        print(m)


# 示例：自动生成一个测试规模 n 并调用 main
if __name__ == "__main__":
    # 根据 n 生成测试数据的简单方式：随机生成一个正整数 n
    test_n = random.randint(1, 100)
    main(test_n)