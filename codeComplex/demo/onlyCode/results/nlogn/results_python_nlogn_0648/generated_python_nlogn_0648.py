from math import *
import sys

def bin_search(arr, n):
    pos = -1
    for i in range(35, -1, -1):
        jump = (1 << i)
        if (pos + jump) >= len(arr):
            continue
        if arr[pos + jump] <= n - 1:
            pos += jump
    return len(arr) - pos - 1

def main(n):
    m = n
    vert = [i * 2 + 1 for i in range(n)]
    hor = [i * 2 + 2 for i in range(m)]
    vert.append(1000000000)
    vert = sorted(vert)
    hor = sorted(hor)
    best = int(1e10)
    for i in range(len(vert)):
        cur_ans = bin_search(hor, vert[i]) + i
        best = min(best, cur_ans)
    return best

if __name__ == "__main__":
    print(main(10))