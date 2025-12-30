from math import pi, sin
from decimal import Decimal, getcontext
import random


def main(n: int):
    """
    n: 多边形边数规模，由调用者传入
    这里根据 n 自动生成测试数据 r，并输出结果 R
    """
    # 根据需要设置精度
    getcontext().prec = 50

    # 根据 n 生成测试数据 r（示例：1 到 100 之间的随机整数）
    r = random.randint(1, 100)

    alpha = Decimal(pi) / Decimal(n)
    a = Decimal(sin(alpha))
    R = Decimal((r * a) / (1 - a))
    print(R)


if __name__ == "__main__":
    # 示例：调用 main(6) 测试，实际使用时由外部传入 n
    main(6)