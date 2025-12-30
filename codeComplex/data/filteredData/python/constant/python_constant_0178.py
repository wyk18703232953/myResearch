from math import gcd
import random


def func(left: int, right: int):
    if left == 1:
        left += 1
    if right - left < 2:
        return -1

    if left & 1:
        if right - left > 2:
            left += 1
            return '{} {} {}'.format(left, left + 1, left + 2)
        else:
            if gcd(left, left + 2) != 1:
                return '{} {} {}'.format(left, left + 1, left + 2)
            return -1
    return '{} {} {}'.format(left, left + 1, left + 2)


def main(n: int):
    """
    n 为规模参数，用于生成测试数据 [left, right] 区间。
    这里简单设定：
      1 <= left < right <= n
    并随机生成一个合法区间。
    """
    if n < 3:
        # 无法形成长度至少为 3 的区间，直接用固定区间测试
        left, right = 1, 3
    else:
        left = random.randint(1, max(1, n - 2))
        right = random.randint(left + 1, n)
        if right - left < 2:
            # 确保 right - left >= 2，尽量满足原函数有意义的输入
            right = min(n, left + 2)

    print(func(left, right))


if __name__ == '__main__':
    # 示例：以 n=100 运行
    main(100)