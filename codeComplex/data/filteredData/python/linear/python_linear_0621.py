import sys
import random
from collections import deque
from bisect import *
from heapq import heappush, heappop, heapify

rem = 10 ** 9 + 7
inf = 10 ** 18
sys.setrecursionlimit(10 ** 6 + 7)


def main(n):
    # 生成规模为 n 的测试数据
    # 这里设置 m = n，使总长度为 2n
    m = n

    # 生成 arr，长度为 n + m
    # 使用 1 到 10^9 的随机整数
    arr = [random.randint(1, 10 ** 9) for _ in range(n + m)]

    # 生成 check，长度为 n + m，确保恰好有 m 个 1 和 n 个 0
    check = [1] * m + [0] * n
    random.shuffle(check)

    cnt = [0 for _ in range(n + m)]
    left = [-1 for _ in range(n + m)]
    right = [-1 for _ in range(n + m)]

    prev = -1
    for i in range(n + m):
        if check[i] == 0:
            left[i] = prev
        else:
            prev = i

    prev = -1
    for i in range(n + m - 1, -1, -1):
        if check[i] == 0:
            right[i] = prev
        else:
            prev = i

    for i in range(n + m):
        if check[i] == 1:
            continue
        a = left[i]
        b = right[i]
        if a == -1 and b == -1:
            continue
        if a == -1 and b != -1:
            cnt[b] += 1
        if a != -1 and b == -1:
            cnt[a] += 1
        if a != -1 and b != -1:
            if abs(arr[i] - arr[a]) <= abs(arr[i] - arr[b]):
                cnt[a] += 1
            else:
                cnt[b] += 1

    ans = []
    for i in range(n + m):
        if check[i] == 1:
            ans.append(str(cnt[i]))

    sys.stdout.write(' '.join(ans))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)