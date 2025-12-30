import math
import random

def main(n: int):
    # 生成测试数据：r 为 1 到 100 的随机整数
    r = random.randint(1, 100)

    # 原逻辑
    l = 2 * r * math.sin(math.pi / n)
    R = l * r / (-l + 2 * r)
    print(R)

if __name__ == "__main__":
    # 示例：调用 main(6)
    main(6)