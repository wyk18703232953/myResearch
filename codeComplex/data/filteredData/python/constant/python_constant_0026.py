import random

def main(n: int):
    # 根据规模 n 生成测试数据，这里示例为随机生成一个 1~n 之间的整数
    test_value = random.randint(1, n)
    
    # 原逻辑：输入为 n，输出为 n // 2 + n
    result = test_value // 2 + test_value
    
    # 输出结果
    print(result)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可根据需要调整
    main(100)