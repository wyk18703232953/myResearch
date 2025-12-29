from collections import defaultdict as dd
from collections import deque, Counter
import bisect
import heapq
from math import inf
import random


def mergeSortGoodOrder(arr):
    """
    counts the number of pairs i < j such that arr[i] < arr[j]
    """
    if len(arr) == 1:
        return arr, 0
    else:
        a = arr[:len(arr) // 2]
        b = arr[len(arr) // 2:]

        a, ai = mergeSortGoodOrder(a)
        b, bi = mergeSortGoodOrder(b)
        c = []

        i = 0
        j = 0
        good = ai + bi

        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i += 1
                good += (len(b) - j)
            else:
                c.append(b[j])
                j += 1

        c += a[i:]
        c += b[j:]

        return c, good


def solve_one(n, aa, m):
    # step1: with m
    bb = [-1] * n
    for i in range(n):
        if aa[i] == m:
            bb[i] = 1
        elif aa[i] < m:
            bb[i] = -1
        else:  # aa[i] > m
            bb[i] = 1

    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = bb[i - 1] + prefix_sum[i - 1]

    # find position of one occurrence of m
    idx = 0
    for i in range(n):
        if aa[i] == m:
            idx = i
            break

    _, good = mergeSortGoodOrder(prefix_sum)
    _, bad_left = mergeSortGoodOrder(prefix_sum[:idx + 1])
    _, bad_right = mergeSortGoodOrder(prefix_sum[idx + 1:])
    first_count = good - bad_left - bad_right

    # step2: with m + 1
    bb = [-1] * n
    for i in range(n):
        if aa[i] == m + 1:
            bb[i] = 1
        elif aa[i] < m + 1:
            bb[i] = -1
        else:  # aa[i] > m + 1
            bb[i] = 1

    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = bb[i - 1] + prefix_sum[i - 1]

    # keep same idx (position of value m)
    _, good = mergeSortGoodOrder(prefix_sum)
    _, bad_left = mergeSortGoodOrder(prefix_sum[:idx + 1])
    _, bad_right = mergeSortGoodOrder(prefix_sum[idx + 1:])
    second_count = good - bad_left - bad_right

    ans = first_count - second_count
    return ans


def main(n: int):
    # 生成测试数据：
    # 保证数组中至少有一个 m，以满足原算法对 idx 的需求
    if n <= 0:
        return

    # 随机生成值范围和 m
    value_min, value_max = 1, max(3, n // 2 + 2)
    m = random.randint(value_min, value_max)

    aa = [random.randint(value_min, value_max) for _ in range(n)]
    # 确保至少有一个元素等于 m
    aa[random.randrange(n)] = m

    ans = solve_one(n, aa, m)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)