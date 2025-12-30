from math import sqrt
import random


def main(n: int):
    # 生成测试数据：
    # a: 加速度系数，1~n
    # v: 初速度，1~n
    # l: 总路程，1~(2n)
    # d: 中间距离，1~l
    # w: 速度限制，1~n
    #
    # 可根据需要自行调整生成策略
    a = random.randint(1, max(1, n))
    v = random.randint(1, max(1, n))
    l = random.randint(1, max(2, 2 * n))
    d = random.randint(1, l)
    w = random.randint(1, max(1, n))

    if v > w:
        s1 = w ** 2 / (2 * a)
        if d <= s1:
            s = min(v ** 2 / (2 * a), l)
            t = sqrt(2 * s / a) + (l - s) / v
        else:
            t = sqrt(2 * s1 / a)
            s2 = min((d - s1) / 2, (v ** 2 - w ** 2) / (2 * a))
            if s2 == (d - s1) / 2:
                t += 2 * (sqrt(2 * (s1 + s2) / a) - sqrt(2 * s1 / a))
            else:
                t += 2 * (v - w) / a + (d - s1 - 2 * s2) / v
            s3 = min((v ** 2 - w ** 2) / (2 * a), l - d)
            t += sqrt(2 * (s3 + s1) / a) - sqrt(2 * s1 / a) + (l - d - s3) / v
    else:
        s = min(v ** 2 / (2 * a), l)
        t = sqrt(2 * s / a) + (l - s) / v

    print(t)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)