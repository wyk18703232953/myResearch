import math
import collections
import bisect
import heapq
import time
import itertools
import sys


def main(n):
    if n <= 0:
        return

    N = n

    # 构造一个确定性的 A，然后用题目逻辑反向生成 B
    # 为保证算法中的条件分支都能被触发，构造一个有规律但不完全平滑的 A
    A = [0] * N
    for i in range(N):
        A[i] = (i * 3 + i // 2) % (N + 7)

    B = [0] * N
    for k in range(N):
        if k == 0:
            i, j = N // 2 - 1, N // 2
        else:
            i = N // 2 - 1 - k
            j = N // 2 + k
        if i < 0 or j >= N:
            break
        B[k] = A[i] + A[j]

    A_rec = [0] * N

    i, j = N // 2 - 1, N // 2
    A_rec[i] = B[-1] // 2
    if B[-1] % 2 == 0:
        A_rec[j] = B[-1] // 2
    else:
        A_rec[j] = B[-1] // 2 + 1
    l, r = A_rec[i], A_rec[j]

    for bi in range(len(B) - 2, -1, -1):
        b = B[bi]
        i -= 1
        j += 1

        if b - l >= A_rec[j - 1]:
            A_rec[i] = l
            A_rec[j] = b - l
            r = b - l
        else:
            A_rec[j] = r
            A_rec[i] = b - r
            l = b - r

    print("N =", N)
    print("B:", " ".join(map(str, B)))
    print("A_rec:", " ".join(map(str, A_rec)))


if __name__ == "__main__":
    main(10)