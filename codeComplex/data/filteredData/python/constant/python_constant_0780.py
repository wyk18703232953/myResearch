#!/usr/bin/env python
from math import sqrt


def check_number(n: int) -> str:
    """
    原逻辑封装：判断 n 是否满足
    1) 是偶数的完全平方数，或
    2) 2*n 是完全平方数
    满足则返回 "YES"，否则返回 "NO"
    """
    if (round(sqrt(n)) ** 2 == n and n % 2 == 0) or round(sqrt(n * 2)) ** 2 == 2 * n:
        return "YES"
    return "NO"


def main(n: int):
    """
    n 为规模参数：
    - 自动生成测试数据：测试 n 个整数，从 1 到 n。
    - 对每个整数调用原逻辑并打印结果。
    """
    for x in range(1, n + 1):
        print(check_number(x))


if __name__ == "__main__":
    # 示例：规模为 10，可根据需要修改
    main(10)