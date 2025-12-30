#!/usr/bin/python3

import random

DEBUG = False


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def solve(N, M, A):
    A.sort(reverse=True)

    lh = A[0]
    cnt = 1
    for a in A[1:]:
        if lh == 1:
            cnt += 1
        elif lh - 1 <= a:
            cnt += 1
            lh -= 1
        else:
            cnt += lh - a
            lh = a

    cnt += lh - 1

    return sum(A) - cnt


def main(n):
    # 根据规模 n 生成测试数据
    N = n
    # 这里简单设定 M 为 n 的两倍（可根据需要调整）
    M = max(1, 2 * n)

    # 生成 N 个在 [1, M] 区间的随机整数
    A = [random.randint(1, M) for _ in range(N)]

    result = solve(N, M, A)
    print(result)


if __name__ == '__main__':
    # 示例：调用 main，规模自行设定
    main(10)