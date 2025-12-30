from math import sqrt
import random


def main(n):
    # 生成测试数据：根据规模 n 生成一组 (a, v, l, d, w)
    # 可根据需要调整生成规则
    random.seed(n)
    a = random.randint(1, max(1, n))
    v = random.randint(1, max(1, 2 * n))
    l = random.randint(1, max(1, 3 * n))
    d = random.randint(1, max(1, l))
    w = random.randint(1, max(1, 2 * n))

    # 原程序逻辑
    if v > w:
        s1 = w ** 2 / 2 / a
        if d <= s1:
            s = min(v ** 2 / 2 / a, l)
            t = sqrt(2 * s / a) + (l - s) / v
        else:
            t = sqrt(2 * s1 / a)
            s2 = min((d - s1) / 2, (v ** 2 - w ** 2) / (2 * a))
            if s2 == (d - s1) / 2:
                t += 2 * (sqrt(2 * (s1 + s2) / a) - sqrt(2 * s1 / a))
            else:
                t += 2 * (v - w) / a + (d - s1 - 2 * s2) / v
            s3 = min((v ** 2 - w ** 2) / 2 / a, l - d)
            t += sqrt(2 * (s3 + s1) / a) - sqrt(2 * s1 / a) + (l - d - s3) / v
    else:
        s = min(v ** 2 / 2 / a, l)
        t = sqrt(2 * s / a) + (l - s) / v

    print(t)
    return t


if __name__ == "__main__":
    # 示例：运行若干规模的测试
    for n in [1, 5, 10]:
        main(n)