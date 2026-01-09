import sys
from heapq import heappush, heappop, heapify
from collections import deque
from bisect import *

rem = 10 ** 9 + 7
inf = 10 ** 18
sys.setrecursionlimit(10 ** 6 + 7)


def main(n):
    m = n
    total = n + m
    arr = [i * 3 + (i // 2) for i in range(total)]
    check = [1 if i % 3 == 0 else 0 for i in range(total)]

    cnt = [0 for _ in range(total)]
    left = [-1 for _ in range(total)]
    right = [-1 for _ in range(total)]

    prev = -1
    for i in range(total):
        if check[i] == 0:
            left[i] = prev

        else:
            prev = i

    prev = -1
    for i in range(total - 1, -1, -1):
        if check[i] == 0:
            right[i] = prev

        else:
            prev = i

    for i in range(total):
        if check[i] == 1:
            continue
        a = left[i]
        b = right[i]
        if a == -1 and b == -1:
            continue
        if a == -1 and b != -1:
            cnt[b] += 1
        elif a != -1 and b == -1:
            cnt[a] += 1

        else:
            if abs(arr[i] - arr[a]) <= abs(arr[i] - arr[b]):
                cnt[a] += 1

            else:
                cnt[b] += 1

    ans = []
    for i in range(total):
        if check[i] == 1:
            ans.append(str(cnt[i]))
    sys.stdout.write(' '.join(ans))


if __name__ == "__main__":
    main(10)