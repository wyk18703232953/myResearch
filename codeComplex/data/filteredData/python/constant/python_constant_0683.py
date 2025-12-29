import math
import random

def main(n: int):
    # 生成测试数据：半径 r，取区间 (0, 100] 的随机浮点数
    r = random.uniform(0.1, 100.0)

    # 按原逻辑进行计算
    a = math.pi / n
    s = math.sin(a)
    R = (r * s) / (1 - s)
    print(R)

if __name__ == "__main__":
    # 示例：调用 main，规模 n 自行指定
    main(6)