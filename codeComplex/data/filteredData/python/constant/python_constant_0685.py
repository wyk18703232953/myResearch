import math
import random

def main(n):
    # 根据规模 n 生成测试数据 r，这里示例：r 为 1 到 100 之间的随机整数
    r = random.randint(1, 100)

    x = math.sin(math.pi / n)
    y = (x * r) / (1 - x)

    print(y)

if __name__ == "__main__":
    # 示例调用，按需修改 n
    main(10)