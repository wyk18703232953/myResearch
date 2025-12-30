#!/usr/bin/env python
import random


def getSum(p, q):
    n = q - p + 1
    temp = (n * (p + q) // 2) - n + 1
    return temp, n


def solve(n, k):
    l = 2
    r = k
    ans = -1

    while l <= r:
        mid = l + (r - l) // 2
        tot, count = getSum(mid, k)
        if tot >= n:
            ans = count
        if tot < n:
            r = mid - 1
        else:
            l = mid + 1

    if n == 1:
        ans = 0
    return ans


def main(n):
    # 根据规模 n 生成测试数据
    # 这里将 n 作为目标值，同时生成 k >= 2 且与 n 同数量级
    if n < 2:
        n = 2
    k = max(2, n + random.randint(0, n))

    result = solve(n, k)
    print(result)


if __name__ == "__main__":
    # 示例：使用某个规模调用 main
    main(10)