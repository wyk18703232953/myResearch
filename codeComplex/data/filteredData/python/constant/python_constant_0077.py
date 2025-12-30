import random

def main(n: int):
    # 根据 n 生成测试数据（这里直接使用传入的 n 作为测试规模）
    if n < 3:
        result = n
    else:
        if n % 2 != 0:
            result = n * (n - 1) * (n - 2)
        elif n % 3 == 0:
            result = (n - 1) * (n - 2) * (n - 3)
        else:
            result = n * (n - 1) * (n - 3)
    print(result)


if __name__ == "__main__":
    # 示例：随机生成一个规模 n 进行测试
    test_n = random.randint(0, 100)
    main(test_n)