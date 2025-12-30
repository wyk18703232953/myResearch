import random

def main(n: int):
    # 根据 n 生成测试数据，这里简单取一个与 n 相关的整数
    # 例如：随机生成一个 1 到 n 的整数，作为原程序中的 n
    if n <= 0:
        return 0
    test_n = random.randint(1, n)

    # 原始逻辑：print(int(3 * n / 2))
    result = int(3 * test_n / 2)
    print(result)
    return result

if __name__ == "__main__":
    # 示例：调用 main(10) 进行测试
    main(10)