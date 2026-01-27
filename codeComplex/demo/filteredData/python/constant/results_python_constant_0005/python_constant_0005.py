from math import sqrt

def main(n):
    # n 控制输入规模，这里构造一个与 n 相关但固定的输入
    # 保证: a>0, v>0, l>0, d>=0, w>=0
    a = max(1, n % 7 + 1)          # 加速度
    v = max(1, (2 * n) % 10 + 1)   # 初速度
    l = max(1, 5 * n + 10)         # 总路程
    d = max(0, (3 * n) % l)        # 减速/限速区间长度
    w = (n % (v + 1))              # 限速

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

    return t

if __name__ == "__main__":
    # 示例调用: 使用固定的 n 进行一次运行
    result = main(10)
    # print(result)
    pass