from math import factorial
from decimal import Decimal
import random

def main(n: int):
    """
    n 用来控制测试数据规模，这里设为字符串长度。
    生成：
      A: 仅由'+'和'-'组成，长度为 n
      B: 长度为 n，由'+', '-', '?' 组成
    按原逻辑计算并打印结果（保留 12 位小数）。
    """

    # 生成测试数据
    # A: 只允许 '+' 和 '-'
    A = ''.join(random.choice(['+', '-']) for _ in range(n))
    # B: 允许 '+', '-', '?'（对应原程序中除'+'和'-'外的任意字符）
    B = ''.join(random.choice(['+', '-', '?']) for _ in range(n))

    # 以下为原始逻辑的无 input() 封装实现
    a = 0
    cnt2 = 0
    cnt1 = 0
    b = 0

    for i in A:
        if i == '+':
            a += 1
            cnt1 += 1
        else:
            a -= 1
            cnt2 += 1

    cnt3 = 0
    cnt = 0
    cnt4 = 0

    for i in B:
        if i == '+':
            b += 1
            cnt3 += 1
        elif i == '-':
            b -= 1
            cnt4 += 1
        else:
            cnt += 1

    if cnt3 > cnt1 or cnt4 > cnt2:
        print(format(0, '.12f'))
    else:
        No_of_plus = cnt1 - cnt3
        No_of_minus = cnt2 - cnt4
        Total_cases = 2 ** cnt
        Total_No_of_favourable_cases = factorial(cnt) // (
            factorial(No_of_plus) * factorial(No_of_minus)
        )
        print(
            format(
                Decimal(Total_No_of_favourable_cases) / Decimal(Total_cases),
                '.12f'
            )
        )


if __name__ == "__main__":
    # 示例：n = 10，可自行修改
    main(10)