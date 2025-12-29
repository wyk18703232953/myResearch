'''
mark-up-1 :hmmge:
'''

import random


def f(ar):
    cmark = 0
    big = [0] * len(ar)
    # 从右往左计算 big
    for i in range(len(ar) - 1, -1, -1):
        cmark = max(cmark - 1, ar[i] + 1, 0)
        big[i] = cmark

    # 从左往右计算总 marks t
    cmark = 0
    t = [0] * len(ar)
    for i in range(len(ar)):
        cmark = max(cmark, big[i])
        t[i] = cmark

    # 计算答案
    for i in range(len(ar)):
        t[i] = t[i] - ar[i] - 1
    return sum(t)


def main(n):
    """
    n 为规模：生成长度为 n 的数组作为测试数据。
    这里示例生成 0~10 之间的随机整数。
    """
    if n <= 0:
        return 0

    # 生成测试数据
    ar = [random.randint(0, 10) for _ in range(n)]

    # 执行原逻辑
    result = f(ar)

    # 输出结果（可以根据需要调整输出形式）
    print(result)
    return result


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)