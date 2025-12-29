import random

def main(n: int):
    # 根据 n 生成测试数据，这里假设原程序的输入就是一个整数
    # 示例：在 1 到 n 之间随机取一个整数作为测试输入
    test_value = random.randint(1, n)

    # 原始逻辑：输出 n//2 + n，这里用 test_value 代替原来的输入 n
    result = test_value // 2 + test_value
    print(result)


if __name__ == "__main__":
    # 示例调用，规模可以自行调整
    main(10)