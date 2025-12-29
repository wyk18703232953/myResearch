import math
import random

def main(n):
    # 根据规模 n 生成测试数据
    # 此处设定 r 为 1 到 100 之间的随机整数
    r = random.randint(1, 100)

    t = math.sin(math.pi / n)
    res = r * t / (1 - t)
    print(res)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)