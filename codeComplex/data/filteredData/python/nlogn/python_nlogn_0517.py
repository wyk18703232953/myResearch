import math
from heapq import *
import random

gcd = math.gcd
sqrt = math.sqrt
ceil = math.ceil


def ind(ch):
    return ord(ch) - ord("a")


def cleanarr(arr):
    n = len(arr)
    arr.sort()
    c = []
    curr = [arr[0], 1]
    for i in range(n - 1):
        if arr[i] != arr[i + 1]:
            if curr[1] >= 2:
                c.append(curr)
            curr = [arr[i + 1], 1]
        else:
            curr[1] += 1
    if curr[1] >= 2:
        c.append(curr)
    return c


def solve_one(arr):
    n = len(arr)
    c = cleanarr(arr)

    if n >= 40000:
        f = 0
        for x, cnt in c:
            if cnt >= 4:
                f = x
                break
        return [f, f, f, f]

    INF = 10 ** 18
    mi = INF
    pair = [-1, -1]

    for i in range(len(c)):
        if c[i][1] >= 4:
            pair = [c[i][0], c[i][0]]
            break
        if i == len(c) - 1:
            break
        a = c[i][0]
        b = c[i + 1][0]
        if mi == INF:
            pair = [a, b]
            mi = 0
            continue
        # 比较 (pair[0], pair[1]) 和 (a, b)
        if (((pair[0] + pair[1]) ** 2) * a * b) - (((a + b) ** 2) * pair[0] * pair[1]) > 0:
            pair = [a, b]

    return [pair[0], pair[0], pair[1], pair[1]]


def generate_test_array(n):
    # 生成至少有一对可用的数据
    # 先生成若干随机值，再强制加入两对相同值
    if n < 4:
        n = 4

    arr = [random.randint(1, 10 ** 6) for _ in range(n - 4)]

    # 插入两对相同值，保证 cleanarr 至少有一个元素
    x = random.randint(1, 10 ** 6)
    y = random.randint(1, 10 ** 6)
    arr.extend([x, x, y, y])
    random.shuffle(arr)
    return arr


def main(n):
    """
    n: 规模参数，用来生成一个长度为 n 的测试数组并运行原逻辑。
    返回值为一个列表 [a, a, b, b]，对应原程序的四行输出。
    """
    arr = generate_test_array(n)
    result = solve_one(arr)
    # 按原程序样式打印
    print(result[0], end=" ")
    print(result[1], end=" ")
    print(result[2], end=" ")
    print(result[3])


if __name__ == "__main__":
    # 示例：使用 n = 100 运行一次
    main(100)