import random

def main(n):
    # 生成测试数据
    # 约定：m 与 n 同规模，这里取 m = n
    m = n

    # 生成数组 a 和 b 的测试数据
    # a: n 个整数，范围 1~100
    # b: m 个整数，范围 1~100
    a = sorted(random.randint(1, 100) for _ in range(n))
    b = [random.randint(1, 100) for _ in range(m)]

    # 原逻辑
    if max(a) < min(b):
        ans = sum(a) * m + sum(b) - a[-1] * (m - 1) - a[-2]
    elif max(a) == min(b):
        ans = sum(a) * m + sum(b) - a[-1] * m
    else:
        ans = -1

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，指定规模 n
    main(5)