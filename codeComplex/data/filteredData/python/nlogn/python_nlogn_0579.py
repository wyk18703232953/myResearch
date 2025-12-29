#!/usr/bin/python3

import random

DEBUG = False


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def solve(N):
    ans = []

    end = N
    fac = 1

    while end >= 1:
        if end == 1:
            ans.append(fac)
            end = 0
            break

        if end == 2:
            ans.append(fac)
            ans.append(fac * 2)
            end = 0
            break

        if end == 3:
            ans.append(fac)
            ans.append(fac)
            ans.append(fac * 3)
            end = 0
            break

        ans.extend([fac] * ((end + 1) // 2))
        end //= 2
        fac *= 2

    return ans


def main(n):
    # 根据 n 生成测试数据，这里简单地让 N = n
    # 也可以改为例如：N = random.randint(1, n) 等
    N = n
    result = solve(N)
    print(*result)


if __name__ == '__main__':
    # 示例：当需要实际运行时，可指定一个规模 n
    example_n = 10
    main(example_n)