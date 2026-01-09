from math import pi, sin
from decimal import Decimal

def main(n):
    # 映射：原程序中有两个输入 n, r
    # 这里将第一个输入设为 n，第二个输入 r 由 n 确定性生成
    # 例如：r = n + 1，且保证 n >= 3（避免过小导致数值异常）
    if n < 3:
        n_local = 3

    else:
        n_local = n
    r = n_local + 1

    alpha = Decimal(pi) / Decimal(n_local)
    a = Decimal(sin(alpha))
    R = Decimal((r * a) / (1 - a))
    return R

if __name__ == "__main__":
    # 示例：以 n = 10 调用
    result = main(10)
    # print(result)
    pass