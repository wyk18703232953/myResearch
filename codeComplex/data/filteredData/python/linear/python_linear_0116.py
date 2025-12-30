import math
import random

def main(n: int):
    # 生成测试数据，这里简单地使用传入的 n 作为原程序中的输入
    # 如果需要批量测试，可以在此生成多个随机样例
    test_value = n

    result = (math.floor(test_value / 2) + 1) * math.ceil(test_value / 2)
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)