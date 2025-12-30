import random

def main(n):
    # 生成测试数据
    # n: 数组 a, b 的长度
    # m: 任意正整数，这里取与 n 同阶的值
    m = max(1, n // 2)

    # 生成数组 a, b 的测试数据（可以根据需要调整生成策略）
    # 这里生成 [1, 10] 范围内的随机整数
    a = [random.randint(1, 10) for _ in range(n)]
    b = [random.randint(1, 10) for _ in range(n)]

    # 原始逻辑开始
    ma = 0
    macount = 0
    mi = 10**30
    su = 0

    for el in a:
        if el > ma:
            ma = el
            macount = 1
        elif el == ma:
            macount += 1

    for el in b:
        mi = min(el, mi)
        su += el

    if ma > mi:
        print(-1)
    elif ma == mi or macount > 1:
        f = True
        for i in range(n):
            if a[i] == ma and f:
                f = False
            else:
                su += a[i] * m
        print(su)
    else:
        secmax = 0
        for el in a:
            if secmax < el < ma:
                secmax = el
        f = True
        for i in range(n):
            if a[i] == ma and f:
                f = False
            else:
                su += a[i] * m
        print(su + ma - secmax)


# 示例调用
if __name__ == "__main__":
    main(5)