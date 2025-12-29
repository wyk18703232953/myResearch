from collections import Counter
from math import *
import sys
mod = 1000000007


def pro(arr, q):
    n = len(arr)
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                ans += 1

    res = ans % 2
    for x, y in q:
        k = y - x + 1
        k = k // 2
        k = k % 2
        res = k ^ res
        if res:
            print('odd')
        else:
            print('even')


def main(n):
    # 生成规模为 n 的测试数组和查询
    # 示例：arr 为 1..n 的排列，t 为 n 个查询
    arr = list(range(1, n + 1))

    # 构造一些覆盖不同区间长度的查询
    q = []
    t = n
    for i in range(t):
        l = (i % n) + 1
        r = n
        if l > r:
            l, r = r, l
        q.append([l, r])

    pro(arr, q)


if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要修改 n
    main(5)