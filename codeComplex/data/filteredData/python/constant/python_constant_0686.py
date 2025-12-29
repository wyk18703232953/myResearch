import math
import random

def main(n):
    # 生成测试数据：n 边形半径 r，取 1 到 100 的随机整数
    r = random.randint(1, 100)

    angle = math.pi / n
    c = math.sin(angle)
    k = c / (1 - c)
    R = k * r

    # 保留 7 位小数输出
    R = float(format(R, '.7f'))
    print(R)

if __name__ == "__main__":
    # 示例：调用 main(6) 表示 n=6
    main(6)