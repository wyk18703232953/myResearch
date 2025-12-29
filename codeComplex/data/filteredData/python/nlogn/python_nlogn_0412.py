from copy import deepcopy
import itertools
from bisect import bisect_left, bisect_right
import math
from collections import deque
import random


def main(n):
    # 生成测试数据：n 个区间 [l, r]，保证 l <= r
    # 这里示例生成：长度在 [0, 10] 内、起点在 [0, 100] 内的随机区间
    N = n
    intervals = []
    for _ in range(N):
        l = random.randint(0, 100)
        r = l + random.randint(0, 10)
        intervals.append((l, r))

    LIST = []
    left = 0
    right = 1
    for l, r in intervals:
        LIST.append((l, left))
        LIST.append((r, right))

    LIST.sort()

    cnt = [0] * (N + 1)  # DO NOT USE cnt[0]

    if not LIST:
        print("")
        return

    k = 1
    x = LIST[0][0]
    dir = left
    for item in LIST[1:]:
        if item[1] == left:
            if dir == left:
                cnt[k] += item[0] - x
                k += 1
                x = item[0]
                dir = left
            else:
                cnt[k] += item[0] - x - 1
                k += 1
                x = item[0]
                dir = left
        else:
            if dir == left:
                cnt[k] += item[0] - x + 1
                k -= 1
                x = item[0]
                dir = right
            else:
                cnt[k] += item[0] - x
                k -= 1
                x = item[0]
                dir = right

    print(" ".join(map(str, cnt[1:]))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)