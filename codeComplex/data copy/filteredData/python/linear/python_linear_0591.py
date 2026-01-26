import math
import sys

sys.setrecursionlimit(1000000)


def core_algorithm(N):
    re = 0
    for i in range(2, N):
        t = N // i - 1
        re += t * i
    return re * 4


def main(n):
    if n < 2:
        N = 2

    else:
        N = n
    result = core_algorithm(N)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)