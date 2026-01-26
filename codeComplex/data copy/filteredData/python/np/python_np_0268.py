import sys
from bisect import bisect_right as rb
from collections import deque
from queue import PriorityQueue
from math import *

mod = 10**9 + 7

def bit(n):
    if n == 0:
        return 0
    val = 1
    while (val & n) == 0:
        val *= 2
    return val

def main(n):
    # 解释规模映射：
    # 使用 n 作为查询数量 q
    # 固定树的规模为 N = 2 * n + 1，保证 N >= 1 且随 n 线性增长
    N = 2 * n + 1
    q = n

    results = []
    for i in range(q):
        # 生成每个查询的初始 t1：
        # 在 [1, N-1] 内循环取值，保证合法且随 i 变化
        t1 = (i % (N - 1)) + 1 if N > 1 else 0

        # 为每个查询生成确定性的操作字符串：
        # 长度随 n 增长，但有上限以控制时间复杂度
        # 这里令操作长度为 min(n, 60)
        length = n if n <= 60 else 60
        ops_chars = []
        for k in range(length):
            r = (i * 131 + k * 17 + n * 7) % 3
            if r == 0:
                ops_chars.append("U")
            elif r == 1:
                ops_chars.append("L")
            else:
                ops_chars.append("R")
        ops = "".join(ops_chars)

        # 保持原算法逻辑
        for j in ops:
            val = bit(t1)
            if j == "U":
                tem = (t1 - val) | (val * 2)
                if tem < N:
                    t1 = tem
            elif j == "L" and val > 1:
                t1 -= val // 2
            elif j == "R" and val > 1:
                t1 += val // 2

        results.append(t1)

    for ans in results:
        print(ans)

if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)