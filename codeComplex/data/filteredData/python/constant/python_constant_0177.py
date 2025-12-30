from math import gcd
import random

def func(l, r):
    if l == 1:
        l += 1
    if r - l < 2:
        return -1

    if l & 1:
        if r - l > 2:
            l += 1
            return "{} {} {}".format(l, l + 1, l + 2)
        else:
            if gcd(l, l + 2) != 1:
                return "{} {} {}".format(l, l + 1, l + 2)
            return -1
    return "{} {} {}".format(l, l + 1, l + 2)


def main(n):
    # 根据规模 n 生成测试数据
    # 定义区间长度与 n 相关，这里取长度为 max(3, n)
    length = max(3, n)
    # 随机选择 l，保证 r = l + length - 1 不溢出到负数
    l = random.randint(1, max(1, 10 ** 6 - length))
    r = l + length - 1

    ans = func(l, r)
    print(ans)


if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)