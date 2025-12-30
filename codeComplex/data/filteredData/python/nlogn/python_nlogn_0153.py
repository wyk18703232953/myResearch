import random

def func(k, a):
    if len(a) == 1:
        return 1
    if k == 1:
        return len(a)
    s = set(a)
    for x in sorted(a):
        if x in s and k * x in s:
            s.remove(k * x)
    return len(s)


def main(n):
    # 生成测试数据
    # 约定：k >= 1，数组 a 为长度 n 的正整数
    random.seed(0)
    k = random.randint(1, 5)
    a = [random.randint(1, 10 * n + 10) for _ in range(n)]

    # 执行逻辑并打印结果
    print(func(k, a))


if __name__ == '__main__':
    # 示例：规模 n = 10
    main(10)