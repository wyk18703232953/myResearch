import math
import random

def main(n: int):
    # 生成测试数据：这里直接把 n 当作原程序中的输入使用
    # 如需随机测试数据，可改为：value = random.randint(1, n)
    value = n

    if value % 2 == 0:
        x = math.floor(value / 2 + 1) * math.floor(value / 2)
    else:
        x = math.ceil(value / 2) * math.ceil(value / 2)
    print(x)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)