import math
import random

def main(n: int):
    # 生成测试数据：r 为 1 到 100 之间的随机整数
    r = random.randint(1, 100)

    angle = math.pi / n
    s = math.sin(angle)
    print('%.8f' % (r * s / (1 - s)))


if __name__ == "__main__":
    # 示例：调用 main(6)，实际使用时可按需修改 n
    main(6)